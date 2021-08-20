
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', port=27017)
#db name - product
db = client['product']
products_collection = db['user']


def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product["description"],
        "parameters": product["parameters"],
    }



#get all products from db
def get_products():
    products = []
    for prod in products_collection.find():
        products.append(product_helper(prod))
    return products


#add new product into db
def add_product(product_data: dict) -> dict:
    product = products_collection.insert_one(product_data)
    new_prod = products_collection.find_one({"_id": product.inserted_id})
    return product_helper(new_prod)


#get product from db by ID
def get_product_by_id(id: str) -> dict:
    product = products_collection.find_one({"_id": ObjectId(id)})
    if product:
        return product_helper(product)


#get products from db by name
def get_product_by_name(name: str) -> dict:
    products = []
    for prod in products_collection.find({"name": name}):
        products.append(product_helper(prod))
    return products


#get products from db by parameters
#{"key":"value"}
def get_product_by_params(params: dict) -> dict:
    params = eval(params)
    key = str(list(params.keys())[0])
    products = []
    for prod in products_collection.find({"parameters."+ key: params[key]}):
        products.append(product_helper(prod))
    return products

