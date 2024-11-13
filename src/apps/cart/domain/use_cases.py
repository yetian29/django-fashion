from dataclasses import dataclass

from src.apps.cart.domain.commands import AddProductCommand, GetCartCommand
from src.apps.cart.domain.entities import Cart
from src.apps.cart.domain.services import ICartService
from src.apps.product.domain.entities import Product


@dataclass(frozen=True)
class GetCartUseCase:
    service: ICartService

    def execute(self, command: GetCartCommand) -> Cart:
        return self.service.get_by_oid(oid=command.oid)


@dataclass(frozen=True)
class AddProductUseCase:
    service: ICartService

    def execute(self, command: AddProductCommand) -> Product:
        return self.service.add_product(product=command.product)
