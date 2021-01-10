from flask import Flask, redirect, url_for, render_template, request
from flask_restful import Api, Resource, reqparse, abort

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
        print(request.form["driver"])
        if request.form["driver"] == "1":
            return redirect(url_for("driver"))
        else:
            return redirect(url_for("lists"))
    else:
        return render_template("home.html")


@app.route("/driver/")
def driver():
    return render_template("driver.html", orders=orders)

@app.route("/lists/")
def lists():
    return render_template("lists.html", orders = orders)

if __name__ == "__main__":
    app.run(debug=True)

