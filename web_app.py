from Back_End.sqlite_storage import distance_compare, query_names, query_user_and_order, update_order
from flask import Flask, redirect, url_for, render_template, request
from flask_restful import Api, Resource, reqparse, abort
import sys
sys.path.append("Back_end/")
from sqlite_storage import insert_user, format_order, distance_compare
import json
import mapping

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
        insert_user(request.form)
        if request.form["driver"] == "1":
            return redirect(url_for("driver"))
        else:
            firstName =  request.form['firstName']
            lastName = request.form['lastName']
            print(firstName)
            print(lastName)
            return redirect(url_for("makeList", first = firstName, last = lastName))
    else:
        return render_template("home.html")

#Creating a new list for the database
@app.route("/makeList/<first>?<last>")
def makeList(first, last):
    return render_template("createList.html", first = first, last = last)

#Handles POST request from makeList, where user creates list
@app.route("/getList/", methods = ['POST'])
def getList():    
    #Storing to SQL
    orderToAdd = format_order(request.form)
    print(orderToAdd)
    update_order(orderToAdd, request.form['first'], request.form['last'])
    return ""

#Gets address from driver
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

#Shows all lists in increasing distances
@app.route("/lists/<address>/")
def lists(address):
    user, order = query_user_and_order()
    first, last = query_names(address)
    distance_orders = distance_compare(address, first, last, user, order)

    return render_template("lists.html", orders = distance_orders)

if __name__ == "__main__":
    app.run(debug=True)

