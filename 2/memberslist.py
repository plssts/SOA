from flask import Flask, g
from flask_restful import Resource, reqparse
from fake_useragent import UserAgent
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
        
        userAgent = UserAgent()
        headers = { 'User-Agent': str(userAgent.random) }
        
        r = requests.post('http://usr:5009/users', data=args, headers=headers)
        return r.json()
        
