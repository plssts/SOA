from flask import Flask, g
from flask_restful import Resource, reqparse
from werkzeug.wrappers import Response
import shelve
import requests
import json

app = Flask(__name__)

class Members(Resource):
    def get(self, cid, email):
        r = requests.get('http://usr_s:5009/' + str(cid) + '/users/' + email)
        
        # response loses its status somewhere, so
        # it is assembled manually
        resp = Response(str(r.json()).replace("'", '"'))
        if r.json()['message'] == 'User not found':
            resp.status_code = 404
        else:
            resp.status_code = 200
        
        return resp
        
    def put(self, email):
        parser = reqparse.RequestParser()
        parser.add_argument('firstName', required=True)
        parser.add_argument('lastName', required=True)
        parser.add_argument('email', required=True)
        args = parser.parse_args()
        r = requests.put('http://usr_s:5009/users/' + email, data=args)
        
        # response loses its status somewhere, so
        # it is assembled manually
        resp = Response(str(r.json()).replace("'", '"'))
        if r.json()['message'] == 'User not found':
            resp.status_code = 404
        elif r.json()['message'] == 'Email Already Exists':
            resp.status_code = 409
        else:
            resp.status_code = 202
        
        return resp

    def patch(self, email):
        parser = reqparse.RequestParser()
        parser.add_argument('firstName', required=False)
        parser.add_argument('lastName', required=False)
        parser.add_argument('email', required=False)
        args = parser.parse_args()
        r = requests.patch('http://usr_s:5009/users/' + email, data=args)
        
        # response loses its status somewhere, so
        # it is assembled manually
        resp = Response(str(r.json()).replace("'", '"'))
        if r.json()['message'] == 'User not found':
            resp.status_code = 404
        elif r.json()['message'] == 'Email Already Exists':
            resp.status_code = 409
        else:
            resp.status_code = 202
        
        return resp

    def delete(self, email):
        r = requests.delete('http://usr_s:5009/users/' + email)
        
        # response loses its status somewhere, so
        # it is assembled manually
        try:
            resp = Response(str(r.json()).replace("'", '"'))
            resp.status_code = 404
        except:
            return '', 204
        
        return resp
        
