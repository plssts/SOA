from flask import Flask, g
from flask_restful import Resource, reqparse
import shelve
import requests

app = Flask(__name__)

class ConferencesList(Resource):
    def get(self):
        # headers = {'Accept': 'application/json'}
        r = requests.get('http://usr:5009/users')
        return r.json()
        
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('title', required=True)
        parser.add_argument('info', required=True)
        parser.add_argument('date', required=True)

        args = parser.parse_args()
        
        nextCID = 1                     # used for looping through primary keys
        CID = 0                         # used as a new id
        entries = database()
        
        while nextCID < 100: CID = nextCID if not (nextCID in entries) else 0
        if CID == 0:
            return {'message': 'Database filled', 'data': {}}, 500
        
        entries[CID] = args

        return {'message': 'New conference created', 'data': entries[CID]}, 201

# duombazes uzkrovimas
def database():
    if 'db' not in g:
        g.db = shelve.open('conferences.db')

    return g.db

# duombazes panaikinimas
@app.teardown_appcontext
def teardown_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()