from polyfactory.factories import DataclassFactory

from src.apps.product.domain.commands import GetProductCommand, GetProductListCommand
from src.apps.product.domain.entities import CatalogProduct, Product


class ProductFactory(DataclassFactory[Product]):
    __model__ = Product


class CataLogProductFactory(DataclassFactory[CatalogProduct]):
    __model__ = CatalogProduct


class GetProductCommandFactory(DataclassFactory[GetProductCommand]):
    __model__ = GetProductCommand


class GetProductListCommandFactory(DataclassFactory[GetProductListCommand]):
    __model__ = GetProductListCommand
