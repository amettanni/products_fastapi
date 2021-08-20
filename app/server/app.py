from fastapi import FastAPI
from server.routes.product import router as ProductRouter

app = FastAPI()

app.include_router(ProductRouter, tags=["Product"], prefix="/product")


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Hello, Smart Design!"}
