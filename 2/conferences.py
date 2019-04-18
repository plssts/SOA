from flask import Flask, g
from flask_restful import Resource, reqparse
import shelve

class Conference(Resource):
    def get(self):
        headers = {'Accept': 'application/json'}
        r = requests.get('http://usr:5009/users', headers=headers)
        return json.dumps(r.text)
