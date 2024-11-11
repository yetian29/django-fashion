from dataclasses import dataclass

from apps.product.domain.commands import GetProductCommand, GetProductListCommand
from apps.product.domain.entities import Product
from apps.product.domain.services import IProductService


@dataclass(frozen=True)
class GetProductUseCase:
    service: IProductService

    def execute(self, command: GetProductCommand) -> Product:
        return self.service.get_by_id(id=command.id)


@dataclass(frozen=True)
class GetProductListUseCase:
    service: IProductService

    def execute(self, command: GetProductListCommand) -> tuple[list[Product], int]:
        products = self.service.find_many(
            sort_field=command.sort.sort_field,
            sort_order=command.sort.sort_order,
            limit=command.pagination.limit,
            offset=command.pagination.offset,
            search=command.search,
        )
        count = self.service.count_many(search=command.search)
        return products, count
