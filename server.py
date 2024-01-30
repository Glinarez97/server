from flask import Flask
from data import me
from data import catalog
import json

api = Flask("Store")


@api.get("/")
def root():
    return "Welcome to the API"


@api.get("/home")
def home():
    return "Hello im an API"

@api.get("/name")
def name():
    return json.dumps(me)

@api.get("/api/test")
def test():
    return "API is working"


@api.get("/api/products")
def get_products():
    return json.dumps(catalog) #will parse the [] to json



# start the api/server
api.run(debug=True)