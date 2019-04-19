from flask import Flask, g, request
from flask_restful import Resource, reqparse
import shelve

app = Flask(__name__)

class ConferenceAttendees(Resource):
    def get(self, cid):
        entries = database()
        
        if not (str(cid) in entries):
            return {'message': 'No members as of yet', 'data': {}}, 200

        return {'message': 'Conference', 'data': entries[str(cid)]}, 200
        
    def post(self, cid):
        entries = database()

        #email = request.values.get('email')
        
        previous = entries[str(cid)]['attendees'] if str(cid) in entries else []
        
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True)
        args = parser.parse_args()
        
        if not args['email']:
            return {'message': 'No such member', 'data': email}, 404
        
        # args = {'cid': '', 'attendees': []}
        args['cid'] = str(cid)
        
        previous.append(args['email'])
        args['attendees'] = previous
        args.pop('email', None)
        entries[args['cid']] = args

        return {'message': 'New attendee added', 'data': args}, 201
        
    def delete(self, cid):
        entries = database()

        if not (str(cid) in entries):
            return {'message': 'No members anyway', 'data': {}}, 404
        
        # email = request.values.get('email')
        
        previous = entries[str(cid)]['attendees']
        
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True)
        args = parser.parse_args()
        # args = {'cid': '', 'attendees': []}
        args['cid'] = str(cid)
        previous.remove(args['email'])
        args['attendees'] = previous
        args.pop('email', None)
        entries[args['cid']] = args
        
        if not previous:
            del entries[str(cid)]   # removing empty list

        return {'message': 'Attendee removed', 'data': email}, 200
        

# duombazes uzkrovimas
def database():
    if 'db' not in g:
        g.db = shelve.open('attendees.db')

    return g.db

# duombazes panaikinimas
@app.teardown_appcontext
def teardown_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()