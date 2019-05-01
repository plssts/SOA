from flask import Flask, g
from flask_restful import Resource, reqparse
import shelve

app = Flask(__name__)

class ConferencesList(Resource):
    def get(self):
        entries = database()
        elements = list(entries.keys())
        
        conferences = [entries[e] for e in elements]

        return {'message': 'Conferences', 'data': conferences}, 200
        
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('title', required=True)
        parser.add_argument('info', required=True)
        parser.add_argument('date', required=True)

        args = parser.parse_args()
        
        CID = ''                        # used as a new id
        entries = database()
        
        CID = [str(i) for i in range(1, 100) if not (str(i) in entries)][0]
        
        if CID == '':
            return {'message': 'Database filled', 'data': {}}, 500
        
        args['cid'] = CID
        entries[args['cid']] = args
        
        # Assigning an empty list as members
        shelve.open(attendees.db')[CID] = []

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
