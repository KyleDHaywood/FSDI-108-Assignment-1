from flask import Flask

# create the server/app
app = Flask("server")

def print_name():
    print("Kyle")

def test_dict():
    print("-----Dictionary-----")

    me = {
        "first": "Kyle",
        "last": "Haywood",
        "age": 35,
        "hobbies": ["Livin' large, livin' so large", "Gettin' swole"],
        "address": {
            "street": "Golf View",
            "City": "Maryville",
            "state": "TN"
        }
    }

    print(me["first"] + " " + me["last"])

    address = me["address"]
    print(address["street"])

def younger_person():
    ages = [12,42,32,50,56,14,78,30,51,89,12,38,67,10]
    pivot=ages[0]
    for num in ages:
        if num < pivot:
            pivot = num
    print(f'{pivot}')

print_name()
test_dict()

younger_person()

# @app.route("/", methods=["get"])
# def home_page():
#     return "This is a page"
    




# # start the server
# app.run(debug=True)