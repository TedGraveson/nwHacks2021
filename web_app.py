from flask import Flask, redirect, url_for, render_template, request
from flask_restful import Api, Resource, reqparse, abort
import sys
sys.path.append("Back_end/")
from sqlite_storage import insert_user

app = Flask (__name__)
api = Api(app)

orders = [
        {
            "id" : 123,
            "items" : ["bread", "eggs", "milk", "batteries", "toaster"],
            "tip": 10,
            "address" : "8989 documentation lane"
        },
        {   "id" : 456,
            "items" : ["OJ", "milk"],
            "tip": 1000,
            "address" : "8989 documentation lane"
        },
        {   "id" : 456,
            "items" : ["OJ", "milk"],
            "tip": 1000,
            "address" : "8989 documentation lane"
        }
]

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/login/", methods =['GET', 'POST'])
def login():
    #User form submission on home page
    if request.method == "POST":
        print(request.form['driver'])
        insert_user(request.form)
        if request.form["driver"] == "1":
            
            return redirect(url_for("driver"))
        else:
            return redirect(url_for("makeList"))
    else:
        return render_template("home.html")

@app.route("/makeList/")
def makeList():
    return render_template("createList.html")

#Handles POST request from makeList, where user creates list
@app.route("/getList/", methods = ['POST'])
def getList():    
    #Storing to SQL
    insert_user(request.form)
    return request.form['items']

@app.route("/driver/", methods=["GET", "POST"])
def driver():
    if request.method == "POST":
        addr = request.form["address"]
        return redirect(url_for("lists", address=addr))
    else:
        return render_template("driver.html", orders=orders)

# #Will be used for ordering by distance
# @app.route("/getDistance/")
# def getDistance():
#     print(request.form)
#     redirect(url_for("lists"), address=request.form['address'])

@app.route("/lists/<address>/")
def lists(address):
    return render_template("lists.html", orders = orders)

if __name__ == "__main__":
    app.run(debug=True)

