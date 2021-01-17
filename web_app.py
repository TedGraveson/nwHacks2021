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
            "address" : "8989 documentation lane",
            "size": 5,
            "distance":0.5
        },
        {   "id" : 456,
            "items" : ["OJ", "milk"],
            "tip": 1000,
            "address" : "8989 documentation lane",
            "size" : 3,
            "distance": 0.7
        },
        {   "id" : 456,
            "items" : ["OJ", "milk"],
            "tip": 1000,
            "address" : "8989 documentation lane",
            "size" : 7,
            "distance": 1.2
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
            userName = firstName + " " + lastName
            print(userName)
            return redirect(url_for("makeList", user = userName))
    else:
        return render_template("home.html")

#Creating a new list for the database
@app.route("/<user>/makeList/", methods = ['GET', 'POST'])
def makeList(user):
    first_name = user.split()[0]
    last_name = user.split()[1]
    if request.method == 'POST':
        print(request.get_json())
        # orderToAdd = request.form.to_dict()
        # orderToAdd = format_order(orderToAdd)
        # update_order(orderToAdd, first_name, last_name)
        return redirect(url_for("login"))
    else:
        return render_template("createList.html", first = first_name, last = last_name)


#Gets address from driver
@app.route("/driver/", methods=["GET", "POST"])
def driver():
    if request.method == "POST":
        addr = request.form["address"]
        return redirect(url_for("lists", address=addr))
    else:
        return render_template("driver.html", orders=orders)


#Shows all lists in increasing distances
@app.route("/lists/<address>/")
def lists(address):
    # user, order = query_user_and_order()
    # first, last = query_names(address)
    # distance_orders = distance_compare(address, first, last, user, order)
    return render_template("lists.html", orders = orders)

if __name__ == "__main__":
    app.run(debug=True)

