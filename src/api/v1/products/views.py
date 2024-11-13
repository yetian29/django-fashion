from uuid import UUID

from django.http import HttpRequest
from ninja import Query, Router

from src.api.v1.products.schemas import (
    CatalogProductOutSchema,
    FindQueryParams,
    ProductOutSchema,
)
from src.api.v1.schemas import ApiResponse, PaginatedListResponse, PaginationOutSchema
from src.apps.product.domain.commands import GetProductCommand
from src.apps.product.domain.use_cases import GetProductListUseCase, GetProductUseCase
from src.core.containers import get_container

router = Router()


@router.get("/{oid}", response=ApiResponse[ProductOutSchema])
def get_product_views(
    request: HttpRequest,
    oid: UUID,
) -> ApiResponse[ProductOutSchema]:
    container = get_container()
    command = GetProductCommand(oid)
    use_case: GetProductUseCase = container.resolve(GetProductUseCase)
    product = use_case.execute(command)
    return ApiResponse(data=ProductOutSchema.from_entity(product))


@router.get("", response=ApiResponse[PaginatedListResponse[CatalogProductOutSchema]])
def get_product_list_views(
    request: HttpRequest,
    find_in: Query[FindQueryParams],
) -> ApiResponse[PaginatedListResponse[CatalogProductOutSchema]]:
    container = get_container()
    command = find_in.to_command()
    use_case = container.resolve(GetProductListUseCase)
    products, count = use_case.execute(command)
    return ApiResponse(
        data=PaginatedListResponse(
            items=[
                CatalogProductOutSchema.from_entity(product) for product in products
            ],
            pagination=PaginationOutSchema(
                page=command.pagination.page,
                limit=command.pagination.limit,
                total=count,
            ),
        )
    )
