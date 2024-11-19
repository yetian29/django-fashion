from uuid import UUID

import punq
from django.http import HttpRequest
from ninja import Query, Router

from src.api.v1.product.schemas import (
    CatalogProductOutSchema,
    DetailProductOutSchema,
    FindInQueryParams,
)
from src.api.v1.schemas import ApiResponse, PaginatedResponse, PaginationOutSchema
from src.apps.product.domain.commands import GetProductCommand
from src.apps.product.domain.use_cases import GetProductListUseCase, GetProductUseCase
from src.core.containers import get_container

router = Router()


@router.get("/{oid}", response=ApiResponse[DetailProductOutSchema])
def get_product_views(
    request: HttpRequest, oid: UUID
) -> ApiResponse[DetailProductOutSchema]:
    container: punq.Container = get_container()
    command = GetProductCommand(oid)
    use_case: GetProductUseCase = container.resolve(GetProductUseCase)
    product = use_case.execute(command)
    return ApiResponse(data=DetailProductOutSchema.from_entity(product))


@router.get("", response=ApiResponse[PaginatedResponse[CatalogProductOutSchema]])
def get_product_list_views(
    request: HttpRequest, find_in: Query[FindInQueryParams]
) -> ApiResponse[PaginatedResponse[CatalogProductOutSchema]]:
    container: punq.Container = get_container()
    command = find_in.to_command()
    use_case: GetProductListUseCase = container.resolve(GetProductListUseCase)
    products, count = use_case.execute(command)
    return ApiResponse(
        data=PaginatedResponse(
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
