from abc import ABC, abstractmethod

from src.apps.user_auth.domain.entities import UserAuth


class ICodeService(ABC):
    @abstractmethod
    def generate_code(self, phone_number: str | None, email: str | None = None) -> str:
        pass

    @abstractmethod
    def validate_code(
        self, code: str, phone_number: str | None = None, email: str | None = None
    ) -> None:
        pass


class ISendCodeService(ABC):
    @abstractmethod
    def send_code(
        self, code: str, phone_number: str | None = None, email: str | None = None
    ) -> None:
        pass


class ILoginService(ABC):
    @abstractmethod
    def active_and_generate_token(self, user_auth: UserAuth) -> str:
        pass


class IUserAuthService(ABC):
    @abstractmethod
    def get_by_phone_number_or_email(
        self, phone_number: str | None = None, email: str | None = None
    ) -> UserAuth:
        pass

    @abstractmethod
    def get_or_create(self, user_auth: UserAuth) -> UserAuth:
        pass

    @abstractmethod
    def update(self, user_auth: UserAuth) -> UserAuth:
        pass
