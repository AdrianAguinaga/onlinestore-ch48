from flask import Flask,request
import json


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

@app.post("/api/products")
def save_product():
    newItem=request.get_json()
    print(newItem)
    products.append(newItem)    
    return json.dumps(newItem)

@app.get("/api/products")
def get_product():
    return json.dumps(products)
    

app.run(debug=True)