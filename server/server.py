
"""
Simple Flask rest-api that can read/write to a dictionary stored permanently
in a pickle-file. Very WIP
"""

from flask import Flask
from flask_restful import Api, Resource, reqparse

import pickle
import os

app = Flask(__name__)
api = Api(app)

SID = ['asd123', 'bcd456', 'dsa321', 'ged512']
NP = 5


def initialize_data(student_id_list, n_problems):
    data = {k: {n+1: False for n in range(n_problems)} for k in student_id_list}
    return data


def data_to_file(data):
    with open('userdata.pckl', 'wb') as f:
        pickle.dump(data, f)


def data_from_file():
    with open('userdata.pckl', 'rb') as f:
        data = pickle.load(f)
    return data



class Student(Resource):

    def get(self, ident):
        data = data_from_file()

        try:
            status = data[ident]
        except KeyError:
            return "User not found", 404        
        return status, 200


    def post(self, ident):
        parser = reqparse.RequestParser()
        parser.add_argument("problem")
        parser.add_argument("status")
        args = parser.parse_args()

        data = data_from_file()

        problem_no = int(args["problem"])
        status = bool(args["status"])

        try:
            problem_completed = data[ident][problem_no]
        except KeyError:
            return "This problem ID is invalid", 404
        
        # Only update if problem was preciously unanswered
        if not problem_completed:
            data[ident][problem_no] = status 
            data_to_file(data)

        return data[ident], 201



if __name__ == '__main__':

    if not os.path.exists('userdata.pckl'):
        data = initialize_data(SID, NP)
        data_to_file(data)

    api.add_resource(Student, "/student/<string:ident>")
    app.run(debug=True)