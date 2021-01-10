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
    if request.method == "POST":
        first = request.form["firstName"]
        # last = request.form["lastName"]
        # driver = 
        # print(user)
        print(request.get_data())
        return redirect(url_for("user", usr=first))
    return render_template("home.html")

@app.route("/<usr>/")
def user(usr):
    return f"<h1>{usr}</h1>"


@app.route("/<usr>/driver")
def driver(usr):
    return render_template("driver.html", orders=orders)

if __name__ == "__main__":
    app.run(debug=True)
# users = [
#         {  "firstName" : "Ted",
#             "lastName" : "GStone",
#             "driver" : True,
#             "timeStart": {"09/01/21": "09:00"},
#             "phoneNumber" : 1234567890,
#             "orderID" : None
#         },
#         {
#             "firstName" : "Brenda",
#             "lastName" : "Woo",
#             "driver" : False,
#             "timeStart": {"09/01/21": "11:00"},
#             "phoneNumber" : 1234567890,
#             "orderID" : 123
#         },

#         {
#             "firstName" : "Sally",
#             "lastName" : "May",
#             "driver" : True,
#             "timeStart": {"09/01/21": "09:00"},
#             "phoneNumber" : 1234567890,
#             "orderID" : None
#         }
# ]
