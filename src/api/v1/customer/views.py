import punq
from django.http import HttpRequest
from ninja import Router

from src.api.v1.customer.schemas import (
    AuthorizeCustomerInSchema,
    AuthorizeCustomerOutSchema,
    LoginCustomerInSchema,
    LoginCustomerOutSchema,
)
from src.api.v1.schemas import ApiResponse
from src.apps.customer.domain.commands import (
    AuthorizeCustomerCommand,
    LoginCustomerCommand,
)
from src.apps.customer.domain.use_cases import (
    AuthorizeCustomerUseCase,
    LoginCustomerUseCase,
)
from src.core.containers import get_container

router = Router()


@router.post("/authorize", response=ApiResponse[AuthorizeCustomerOutSchema])
def authorize_customer_views(
    request: HttpRequest, authorize_in: AuthorizeCustomerInSchema
) -> ApiResponse[AuthorizeCustomerOutSchema]:
    container: punq.Container = get_container()
    command = AuthorizeCustomerCommand(customer=authorize_in.to_entity())

    use_case: AuthorizeCustomerUseCase = container.resolve(AuthorizeCustomerUseCase)
    code = use_case.execute(command)
    phone_number = command.customer.phone_number
    email = command.customer.email
    key = phone_number if phone_number else email
    return ApiResponse(
        data=AuthorizeCustomerOutSchema(
            msg=f"The code <{code}> has been sent to phone number or email <{key}>"
        )
    )


@router.post("/login", response=ApiResponse[LoginCustomerOutSchema])
def login_customer_views(
    request: HttpRequest, login_in: LoginCustomerInSchema
) -> ApiResponse[LoginCustomerOutSchema]:
    container: punq.Container = get_container()
    command = LoginCustomerCommand(
        phone_number=login_in.phone_number, email=login_in.email, code=login_in.code
    )
    use_case: LoginCustomerUseCase = container.resolve(LoginCustomerUseCase)
    token = use_case.execute(command)
    return ApiResponse(data=LoginCustomerOutSchema(token=token))
