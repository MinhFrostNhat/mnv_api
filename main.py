from fastapi import FastAPI
from routers_API.View import user_main,login_main,product_main,cart_main
from routers_API.models import user_models
from routers_API.database import engine
app = FastAPI(
    title="This is nhattrau"
)

user_models.Base.metadata.create_all(engine)

app.include_router(user_main.router)
app.include_router(login_main.router)
app.include_router(product_main.router)
app.include_router(cart_main.router)