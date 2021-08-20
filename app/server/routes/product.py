from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_product,
    get_product_by_id,
    get_products,
    get_product_by_name,
    get_product_by_params,

)
from server.models.product import (
    ErrorResponseModel,
    ProductModel,
)

router = APIRouter()


@router.post("/", response_description="New product added into the database")
def post_product_data(product: ProductModel = Body(...)):
    product = jsonable_encoder(product)
    new_prod = add_product(product)
    return new_prod


@router.get("/", response_description="Products retrieved")
def get_all_products_data():
    products = get_products()
    return products


@router.get("/{id}", response_description="Product retrieved")
def get_product(id):
    product = get_product_by_id(id)
    if product:
        return product
    return ErrorResponseModel("An error occurred.", 404, "Product with such ID doesn't exist.")



@router.get("/name/{name}", response_description="Product retrieved")
def get_product_name(name):
    product = get_product_by_name(name)
    if product:
        return product
    return ErrorResponseModel("An error occurred.", 404, "Products with such name doesn't exists.")


@router.get("/params/get", response_description="Product retrieved")
def get_product_params(params):
    product = get_product_by_params(params)
    if product:
        return product
    return ErrorResponseModel("An error occurred.", 404, "Products with such parameters doesn't exists.")

