from flask import Flask, g
from flask_restful import Resource, reqparse
from fake_useragent import UserAgent
import shelve
import requests

app = Flask(__name__)

class Members(Resource):
    def get(self, email):
        r = requests.get('http://usr:5009/users/' + email)
        return r.json()
        
    def put(self, email):
        parser = reqparse.RequestParser()
        parser.add_argument('firstName', required=True)
        parser.add_argument('lastName', required=True)
        parser.add_argument('email', required=True)
        args = parser.parse_args()
        
        userAgent = UserAgent()
        headers = { 'User-Agent': str(userAgent.random) }
        
        r = requests.put('http://usr:5009/users/' + email, data=args, headers=headers)
        return r.json()

    def patch(self, email):
        parser = reqparse.RequestParser()
        parser.add_argument('firstName', required=False)
        parser.add_argument('lastName', required=False)
        parser.add_argument('email', required=False)
        args = parser.parse_args()
        
        userAgent = UserAgent()
        headers = { 'User-Agent': str(userAgent.random) }
        
        r = requests.patch('http://usr:5009/users/' + email, data=args, headers=headers)
        return r.json()

    def delete(self, email):
        userAgent = UserAgent()
        headers = { 'User-Agent': str(userAgent.random) }
    
        r = requests.delete('http://usr:5009/users/' + email, headers=headers)
        return r.json()
        
