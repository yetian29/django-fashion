from ninja import NinjaAPI

from src.api.v1.products.views import router as products_router

api = NinjaAPI(docs_url="/api/v1/docs")

api.add_router("/product", products_router, tags=["Products"])
