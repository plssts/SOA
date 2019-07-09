from flask import Flask, g, request
from flask_restful import Resource, reqparse
import shelve
import requests

app = Flask(__name__)

class ConferencesList(Resource):
    def get(self):
        entries = database()
        elements = list(entries.keys())
        
        conferences = []
        for e in elements:
            dataHash = entries[e]
            try:
                r = requests.get('http://usr_s:5009/' + str(e) + '/users')
                
                if not r.json()['message'] == 'No attendees':
                    if 'embedded' in request.args and request.args['embedded'] == 'attendees':
                        dataHash['attendees'] = [r.json()['data'][key] for key in list(r.json()['data'].keys())]
                        
                    else:
                        dataHash['attendees'] = [key for key in list(r.json()['data'].keys())]
                        
                    conferences.append(dataHash)
                    
            except requests.exceptions.ConnectionError:
                conferences.append(dataHash)
                pass

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

        return {'message': 'New conference created', 'data': entries[CID]}, 201

# duombazes uzkrovimas
def database():
    db = getattr(g, '_database', None)
    
    if db is None:
        db = g._database = shelve.open("conferences.db")
        
    return db

# duombazes panaikinimas
@app.teardown_appcontext
def teardown_db():
    db = getattr(g, '_database', None)
    
    if db is not None:
        db.close()
