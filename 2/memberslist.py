from flask import Flask, g
from flask_restful import Resource, reqparse
from werkzeug.wrappers import Response
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
        
        # response loses its status somewhere, so
        # it is assembled manually
        resp = Response(str(r.json()).replace("'", '"'))
        if r.json()['message'] == 'Email Already Exists':
            resp.status_code = 409
        else:
            resp.status_code = 201
        
        return resp
