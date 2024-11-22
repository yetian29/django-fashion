import re
from uuid import UUID

from ninja import Schema
from pydantic import field_validator, model_validator

from src.apps.user_auth.domain.entities import UserAuth


class BaseValidateSchema(Schema):
    phone_number: str | None = None
    email: str | None = None

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, value: str | None = None) -> str | None:
        value = value.strip()
        if not value:
            return None
        elif not value.isdigit():
            raise ValueError("Invalid phone number. The phone number has to be digits.")
        elif len(value) != 10:
            raise ValueError(
                "Invalid phone number. The phone number has to be 10 digit."
            )
        return value

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str | None = None) -> str | None:
        value = value.strip()
        if not value:
            return None
        pattern = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, value):
            raise ValueError(
                "Invalid email format. The email has to be format 'example@gmail.com'."
            )
        return value

    @model_validator(mode="after")
    def validate_model(self) -> "BaseValidateSchema":
        phone_number = self.phone_number
        email = self.email
        if not phone_number and not email:
            raise ValueError("Invalid. The phone number or email have to be provided.")
        elif phone_number and email:
            raise ValueError("Invalid. Not allowed has both phone number and email.")
        return self


class AuthorizeUserAuthInSchema(BaseValidateSchema):
    def to_entity(self) -> UserAuth:
        return UserAuth(
            phone_number=self.phone_number,
            email=self.email,
        )


class AuthorizeUserAuthOutSchema(Schema):
    msg: str


class LoginUserAuthInSchema(BaseValidateSchema):
    code: str

    @field_validator("code")
    @classmethod
    def validate_code(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Invalid code. The code has to be required.")
        elif not value.isdigit():
            raise ValueError("Invalid code format. The code has to be digits.")
        elif len(value) != 6:
            raise ValueError("Invalide code. The code has to be 6 digit.")
        return value


class LoginUserAuthOutSchema(Schema):
    token: UUID

    @field_validator("token")
    @classmethod
    def validate_token(cls, value: UUID) -> UUID:
        value_str = str(value)
        if not UUID(value_str, version=4):
            raise ValueError("Invalid token.")
        return value
