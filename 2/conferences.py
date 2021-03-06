from flask import Flask, g, request
from flask_restful import Resource, reqparse
import shelve
import requests

app = Flask(__name__)

class Conferences(Resource):
    # GET - retrieve a specific conference
    def get(self, cid):
        entries = database()
        
        if not (str(cid) in entries):
            return {'message': 'No such conference', 'data': {}}, 404
        
        dataHash = entries[str(cid)]
        
        try:
            r = requests.get('http://usr_s:5009/' + str(cid) + '/users')
            
            if not r.json()['message'] == 'No attendees':
                if 'embedded' in request.args and request.args['embedded'] == 'attendees':
                    dataHash['attendees'] = [r.json()['data'][key] for key in list(r.json()['data'].keys())]
                else:
                    dataHash['attendees'] = [key for key in list(r.json()['data'].keys())]
                    
        except requests.exceptions.ConnectionError:
            return {'message': 'Conference', 'data': dataHash}, 200
            
        return {'message': 'Conference', 'data': dataHash}, 200
        
    # PUT - edit a specific conference
    def put(self, cid):
        entries = database()
        
        if not (str(cid) in entries):
            return {'message': 'No such conference', 'data': {}}, 404
    
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('info', required=True)
        parser.add_argument('date', required=True)
        args = parser.parse_args()
        
        args['cid'] = str(cid)
        entries[args['cid']] = args

        return {'message': 'Conference updated', 'data': args}, 200
        
    # DELETE - remove a specific conference
    def delete(self, cid):
        entries = database()

        if not (str(cid) in entries):
            return {'message': 'No such conference', 'data': {}}, 404
        
        try:
            r = requests.get('http://usr_s:5009/' + str(cid) + '/users')
            
            if not r.json()['message'] == 'No attendees':
                for key in list(r.json()['data'].keys()):
                    requests.delete('http://usr_s:5009/' + str(cid) + '/users/' + key)
        
            del entries[str(cid)]

            return {'message': 'Conference removed', 'data': str(cid)}, 200
        
        except requests.exceptions.ConnectionError:
            return {'message': 'Conference cannot be removed due to unavailability of attendee service', 'data': {}}, 503
        
        

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
