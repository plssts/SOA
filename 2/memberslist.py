from flask import Flask, g
from flask_restful import Resource, reqparse
import shelve
import requests

app = Flask(__name__)

class MembersList(Resource):
    def get(self):
        r = requests.get('http://usr:5009/users')
        return r.json()
        
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('firstName', required=True)
        parser.add_argument('lastName', required=True)
        parser.add_argument('email', required=True)
        args = parser.parse_args()
        
        r = requests.post('http://usr:5009/users', data=args)
        
        # response status code gets lost in the process
        if r.json()['message'] == 'Email Already Exists':
            r.status_code = 409
        if r.json()['message'] == 'User created':
            r.status_code = 201
        
        return r.json()
