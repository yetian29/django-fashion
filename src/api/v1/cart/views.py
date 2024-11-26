from uuid import UUID

import punq
from django.http import HttpRequest
from ninja import Header, Router

from src.api.v1.cart.schemas import CartOutSchema
from src.api.v1.schemas import ApiResponse
from src.apps.cart.domain.commands import GetOrCreateCartCommand
from src.apps.cart.domain.use_cases import GetOrCreateCartUseCase
from src.core.containers import get_container

router = Router()


@router.api_operation(
    ["GET", "POST"], "/{customer_oid}", response=ApiResponse[CartOutSchema]
)
def get_or_create_cart_views(
    request: HttpRequest,
    customer_oid: UUID,
    token: UUID = Header(alias="Auth-Token"),
) -> ApiResponse[CartOutSchema]:
    container: punq.Container = get_container()
    command = GetOrCreateCartCommand(customer_oid)
    use_case: GetOrCreateCartUseCase = container.resolve(GetOrCreateCartUseCase)
    cart = use_case.execute(command)
    return ApiResponse(data=CartOutSchema.from_entity(cart))
