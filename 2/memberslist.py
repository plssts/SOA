from flask import Flask, g
from flask_restful import Resource, reqparse
from werkzeug.wrappers import Response
import shelve
import requests

app = Flask(__name__)

class MembersList(Resource):
    def get(self, cid):
        entries = database()
        if not (str(cid) in entries):
            return {'message': 'No such conference', 'data': {}}, 404
        
        r = requests.get('http://usr_s:5009/' + str(cid) + '/users')
        
        # response loses its status somewhere, so
        # it is assembled manually
        resp = Response(str(r.json()).replace("'", '"'))
        if r.json()['message'] == 'No attendees':
            resp.status_code = 404
        else:
            resp.status_code = 200
        
        return resp
        
    def post(self, cid):
        entries = database()
        if not (str(cid) in entries):
            return {'message': 'No such conference', 'data': {}}, 404
        
        parser = reqparse.RequestParser()
        parser.add_argument('firstName', required=True)
        parser.add_argument('lastName', required=True)
        parser.add_argument('email', required=True)
        args = parser.parse_args()
        
        r = requests.post('http://usr_s:5009/' + str(cid) + '/users', data=args)
        
        # response loses its status somewhere, so
        # it is assembled manually
        resp = Response(str(r.json()).replace("'", '"'))
        if r.json()['message'] == 'Email Already Exists':
            resp.status_code = 409
        else:
            resp.status_code = 201
        
        return resp

def database():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("conferences.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
