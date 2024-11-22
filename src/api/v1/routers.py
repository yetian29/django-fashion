from ninja import NinjaAPI

from src.api.v1.product.views import router as product_router
from src.api.v1.user_auth.views import router as user_auth_router

api = NinjaAPI(docs_url="/api/v1/docs")

api.add_router("/product", product_router, tags=["Product"])
api.add_router("/user_auth", user_auth_router, tags=["User Auth"])
