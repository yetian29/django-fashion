from ninja import NinjaAPI

from src.api.v1.customer.views import router as customer_router
from src.api.v1.product.views import router as product_router

api = NinjaAPI(docs_url="/api/v1/docs")

api.add_router("/product", product_router, tags=["Product"])
api.add_router("/customer", customer_router, tags=["User Auth"])
