from flask import Flask,request
import json
from config import db

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from flask"


# create another API that redirets you to a test

@app.get("/test")
def test():
    return "Hello from the test"


@app.get("/api/about")
def about():
    myname ={"name": "adrian aguinaga"}
    return json.dumps(myname)

products = []

def fix_id(obj):
    obj["_id"]=str(obj["_id"])
    return obj

@app.post("/api/products")
def save_product():
    newItem=request.get_json()
    print(newItem)
    db.products.insert_one(newItem)
    #products.append(newItem)    
    return json.dumps(fix_id(newItem))

@app.get("/api/products")
def get_product():
    return json.dumps(products)
    

app.run(debug=True)