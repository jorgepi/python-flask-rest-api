#!/usr/bin/env python

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
users = [
    {
        "name": "Jorge",
        "age": 38,
        "occupatiion": "DevOps Engineer"
    },
    {
        "name": "Carlos",
        "age": 38,
        "occupation": "Transporter"
    },
    {
        "name": "Koldo",
        "age": 39,
        "occupation": "Head of Logistics"
    }
]

class User(Resource):

    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 200

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            print("User from the list {}".format(user["name"]))
            print("User posted {}".format(name))
            if(name == user["name"]):
                return "User with name {} already exist".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

api.add_resource(User, "/user/<string:name>")
app.run(host='0.0.0.0', debug=True)
