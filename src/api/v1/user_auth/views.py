import punq
from django.http import HttpRequest
from ninja import Router

from src.api.v1.schemas import ApiResponse
from src.api.v1.user_auth.schemas import (
    AuthorizeUserAuthInSchema,
    AuthorizeUserAuthOutSchema,
    LoginUserAuthInSchema,
    LoginUserAuthOutSchema,
)
from src.apps.user_auth.domain.commands import (
    AuthorizeUserAuthCommand,
    LoginUserAuthCommand,
)
from src.apps.user_auth.domain.use_cases import (
    AuthorizeUserAuthUseCase,
    LoginUserAuthUseCase,
)
from src.core.containers import get_container

router = Router()


@router.post("/authorize", response=ApiResponse[AuthorizeUserAuthOutSchema])
def authorize_user_auth_views(
    request: HttpRequest, authorize_in: AuthorizeUserAuthInSchema
) -> ApiResponse[AuthorizeUserAuthOutSchema]:
    container: punq.Container = get_container()
    command = AuthorizeUserAuthCommand(user_auth=authorize_in.to_entity())

    use_case: AuthorizeUserAuthUseCase = container.resolve(AuthorizeUserAuthUseCase)
    code = use_case.execute(command)
    phone_number = command.user_auth.phone_number
    email = command.user_auth.email
    key = phone_number if phone_number else email
    return ApiResponse(
        data=AuthorizeUserAuthOutSchema(
            msg=f"The code <{code}> has been sent to phone number or email <{key}>"
        )
    )


@router.post("/login", response=ApiResponse[LoginUserAuthOutSchema])
def login_user_auth_views(
    request: HttpRequest, login_in: LoginUserAuthInSchema
) -> ApiResponse[LoginUserAuthOutSchema]:
    container: punq.Container = get_container()
    command = LoginUserAuthCommand(
        phone_number=login_in.phone_number, email=login_in.email, code=login_in.code
    )
    use_case: LoginUserAuthUseCase = container.resolve(LoginUserAuthUseCase)
    token = use_case.execute(command)
    return ApiResponse(data=LoginUserAuthOutSchema(token=token))
