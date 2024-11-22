import re

from ninja import Schema
from pydantic import field_validator


class AuthorizeUserAuthInSchema(Schema):
    phone_number: str | None = None
    email: str | None = None

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, value: str | None = None) -> str | None:
        value = value.strip()
        if not value:
            return None
        elif not value.isdigit():
            raise ValueError("Invalid phone number. The phone number must be digits.")
        elif len(str) != 10:
            raise ValueError(
                "Invalid phone number. The phone number must has 10 digit."
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
                "Invalid email format. The email must be format 'example@gmail.com'"
            )
        return value


class AuthorizeUserAuthOutSchema(Schema):
    msg: str
