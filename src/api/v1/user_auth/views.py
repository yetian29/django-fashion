import punq
from django.http import HttpRequest
from ninja import Router

from src.api.v1.schemas import ApiResponse
from src.api.v1.user_auth.schemas import (
    AuthorizeUserAuthInSchema,
    AuthorizeUserAuthOutSchema,
)
from src.apps.user_auth.domain.commands import AuthorizeUserAuthCommand
from src.apps.user_auth.domain.use_cases import AuthorizeUserAuthUseCase
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
