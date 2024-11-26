from uuid import UUID

import punq
from django.http import HttpRequest
from ninja import Header, Router

from src.api.v1.cart.schemas import CartOutSchema
from src.api.v1.schemas import ApiResponse
from src.apps.cart.domain.commands import GetOrCreateCartCommand
from src.apps.cart.domain.use_cases import GetOrCreateCartUseCase
from src.apps.customer.domain.commands import GetCustomerCommand
from src.apps.customer.domain.use_cases import GetCustomerUseCase
from src.core.containers import get_container

router = Router()


@router.api_operation(["GET", "POST"], path="", response=ApiResponse[CartOutSchema])
def get_or_create_cart_views(
    request: HttpRequest,
    token: UUID = Header(alias="Auth-Token"),
) -> ApiResponse[CartOutSchema]:
    container: punq.Container = get_container()
    command1 = GetCustomerCommand(token)
    use_case1: GetCustomerUseCase = container.resolve(GetCustomerUseCase)
    customer = use_case1.execute(command1)
    command2 = GetOrCreateCartCommand(customer_oid=customer.oid)
    use_case2: GetOrCreateCartUseCase = container.resolve(GetOrCreateCartUseCase)
    cart = use_case2.execute(command2)
    return ApiResponse(data=CartOutSchema.to_entity(cart))
