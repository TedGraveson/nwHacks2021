from flask import Flask, redirect, url_for, render_template, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask (__name__)
api = Api(app)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/login/", methods =['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form["firstName"]
        print(user)
    return render_template("home.html")



if __name__ == "__main__":
    app.run(debug=True)