from flask import Flask, g, request
from flask_restful import Resource, reqparse
import shelve
import requests

app = Flask(__name__)

class Conferences(Resource):
    def get(self, cid):
        entries = database()
        
        if not (str(cid) in entries):
            return {'message': 'No such conference', 'data': {}}, 404
        
        dataHash = entries[str(cid)]
        
        if 'embedded' in request.args:
            dataHash['attendees'] = shelve.open('attendees.db')[str(cid)]['attendees']

        return {'message': 'Conference', 'data': dataHash}, 200
    
    def post(self, cid):
        entries = database()
        
        if not (str(cid) in entries):
            return {'message': 'No such conference', 'data': {}}, 404
        
        if 'embedded' in request.args:
            previous = shelve.open('attendees.db')[str(cid)]['attendees']
            
            parser = reqparse.RequestParser()
            parser.add_argument('email', required=True)
            args = parser.parse_args()
        
            if args['email'] in previous:
                return {'message': 'This member is already participating', 'data': args['email']}, 409
        
            r = requests.get('http://usr:5009/users/' + args['email'])
            if r.status_code == 404:
                return {'message': 'No such member', 'data': args['email']}, 404
            
            args['cid'] = str(cid)
            previous.append(args['email'])
            args['attendees'] = previous
            email = args.pop('email', None)
            shelve.open('attendees.db')[args['cid']] = args
            return {'message': 'New attendee added', 'data': email}, 201
        else:
            return {'message': 'POST on /conferences/cid is for adding attendees only', 'data': {}}, 405
        
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
        
    def delete(self, cid):
        entries = database()

        if 'embedded' in request.args:
            previous = shelve.open('attendees.db')[str(cid)]['attendees']
            
            parser = reqparse.RequestParser()
            parser.add_argument('email', required=True)
            args = parser.parse_args()
        
            r = requests.get('http://usr:5009/users/' + args['email'])
            if r.status_code == 404:
                return {'message': 'No such member', 'data': args['email']}, 404
            
            if not args['email'] in previous:
                return {'message': 'This member is not attending the conference', 'data': args['email']}, 404
            
            args['cid'] = str(cid)
            previous.remove(args['email'])
            args['attendees'] = previous
            email = args.pop('email', None)
            shelve.open('attendees.db')[args['cid']] = args
            return {'message': 'Attendee removed', 'data': email}, 200

        if not (str(cid) in entries):
            return {'message': 'No such conference', 'data': {}}, 404
        
        del entries[str(cid)]

        return {'message': 'Conference removed', 'data': str(cid)}, 200
        

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
