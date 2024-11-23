from abc import ABC, abstractmethod

from src.apps.customer.domain.entities import Customer


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
    def active_and_generate_token(self, customer: Customer) -> str:
        pass


class ICustomerService(ABC):
    @abstractmethod
    def get_by_phone_number_or_email(
        self, phone_number: str | None = None, email: str | None = None
    ) -> Customer:
        pass

    @abstractmethod
    def get_or_create(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def update(self, customer: Customer) -> Customer:
        pass
