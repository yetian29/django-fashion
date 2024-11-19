from polyfactory.factories import DataclassFactory

from src.apps.product.domain.commands import GetProductCommand, GetProductListCommand
from src.apps.product.domain.entities import CatalogProduct, DetailProduct


class CatalogProductFactory(DataclassFactory[CatalogProduct]):
    __model__ = CatalogProduct


class DetailProductFactory(DataclassFactory[DetailProduct]):
    __model__ = DetailProduct


class GetProductCommandFactory(DataclassFactory[GetProductCommand]):
    __model__ = GetProductCommand


class GetProductListCommandFactory(DataclassFactory[GetProductListCommand]):
    __model__ = GetProductListCommand
