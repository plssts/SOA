from flask import Flask, g
from flask_restful import Resource, reqparse
import shelve

app = Flask(__name__)

class Conferences(Resource):
    def get(self, cid):
        entries = database()
        
        if not (str(cid) in entries):
            return {'message': 'No such conference', 'data': {}}, 404

        return {'message': 'Conference', 'data': entries[str(cid)]}, 200
        
    def put(self, cid):
        entries = database()
    
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('info', required=True)
        parser.add_argument('date', required=True)
        args = parser.parse_args()
        
        args['cid'] = str(cid)
        entries[args['cid']] = args

        return {'message': 'Conference updated', 'data': args}, 202
        
    def delete(self, cid):
        entries = database()

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