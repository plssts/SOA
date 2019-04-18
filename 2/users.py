from flask import Flask, g
from flask_restful import Resource, reqparse
import shelve

app = Flask(__name__)

class Users(Resource):
    @app.route('/users')
    def get(self):
        r = requests.get('http://usr:5009/users')
        return r.json()
        
    @app.route('/users/<string:email>')
    def get(self, email):
        r = requests.get('http://usr:5009/users/' + email)
        return r.json()