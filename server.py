from email.headerregistry import Address
from flask import Flask, abort
from mock_data import catalog
import json
from about_me import me



def address_page():
    address=me["address"]
    print(address["street"] + " " + address["city"] + " " + address["state"])

# create the server/app
app = Flask("server")

@app.route("/", methods=["get"])
def home_page():
    return "Under Construction!"

@app.route("/test")
def test():
    return "Test Page" 

@app.route("/about")
def about_me():
    return "This Page is All About Me"

@app.route("/myaddress")
def address_page():
    address=me["address"]
    return f'Send Mail Here {address["street"]} {address["city"]} {address["state"]}'

# ########################################
# ########### API ENDPOINT ###############
# ########################################

@app.route("/api/catalog")
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/catalog/count")
def get_count():
    count=len(catalog)
    return json.dumps(count)

#get api/catalog/sum
# sum of all prices
@app.route("/api/catalog/sum")
def get_sum():
    total=0
    for product in catalog:
        total += product["price"]

    result = f'$ {total}'
    return json.dumps(result)

# GET API/PRODUCT/<ID>
# GET A PRODUCT BY ITS ID
@app.route("/api/product/<id>")
def get_product(id):
    for product in catalog:
        if id == product["_id"]:
            return json.dumps(product)

    return abort(404) #404 NOT FOUND

# GET API/PRODUCT/MOST_EXPENSIVE
# 
@app.route("/api/product/price")
def get_most_expensive():
    pivot = catalog[0]
    for product in catalog:
        if pivot["price"] < product["price"]:
            pivot = product
    return json.dumps(pivot)

# start the server
app.run(debug=True)
