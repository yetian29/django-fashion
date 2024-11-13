from dataclasses import dataclass

from src.apps.cart.domain.commands import GetCartCommand
from src.apps.cart.domain.entities import Cart
from src.apps.cart.domain.services import ICartService


@dataclass(frozen=True)
class GetCartUseCase:
    service: ICartService

    def execute(self, command: GetCartCommand) -> Cart:
        return self.service.get_by_oid(oid=command.oid)
