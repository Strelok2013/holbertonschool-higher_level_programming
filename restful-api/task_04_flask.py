#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
""""""


app = Flask(__name__)

if __name__ == "__main__": app.run()
users = {}
newUser = {"username": "john", "name": "John", "age": 30, "city": "New York"}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def json_data():
    return jsonify(list(users.keys()))

@app.route("/status")
def return_status():
    return "OK"

@app.route("/users/<username>")
def return_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username]) 

@app.route("/add_user", methods=["POST"])
def add_user(user):
    """"""

    if request.get_json is None:
        abort(400, "Not a Json")

    req_data = request.get_json()

    if "username" not in req_data:
        return jsonify({"error": "Username is Required"}), 400

    users[req_data["username"]] = {
        "name": req_data["name"],
        "age": req_data["age"],
        "city": req_data["city"]
    }

    usr = {
        "username": req_data["username"],
        "name": req_data["name"],
        "age": req_data["age"],
        "city": req_data["city"]
    }
    message = {"Message": "User added", "User": usr}
    return jsonify(message), 201

