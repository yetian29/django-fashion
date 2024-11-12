from uuid import UUID

import punq
from django.http import HttpRequest
from ninja import Router

from src.api.v1.products.schemas import ProductOutSchema
from src.api.v1.schemas import ApiResponse
from src.apps.product.domain.commands import GetProductCommand
from src.apps.product.domain.use_cases import GetProductUseCase
from src.core.containers import get_container

router = Router()


@router.get("/{oid}", response=ApiResponse[ProductOutSchema])
def get_product_views(
    request: HttpRequest,
    oid: UUID,
) -> ApiResponse[ProductOutSchema]:
    container: punq.Container = get_container()
    command = GetProductCommand(oid)
    use_case: GetProductUseCase = container.resolve(GetProductUseCase)
    product = use_case.execute(command)
    return ApiResponse(data=ProductOutSchema.from_entity(product))
