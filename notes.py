from flask import Flask, g
from flask_restful import Resource, reqparse
import shelve

app = Flask(__name__)

class Notes(Resource):
    def get(self, title):
        entries = database()

        if not (title in entries):
            return {'message': 'Note does not exist', 'data': {}}, 404

        return {'message': 'Note', 'data': entries[title]}, 200

    def put(self, title):
        entries = database()

        if not (title in entries):
            return {'message': 'Note does not exist', 'data': {}}, 404

        parser = reqparse.RequestParser()

        parser.add_argument('title', required=True)
        parser.add_argument('author', required=True)
        parser.add_argument('comment', required=True)
        parser.add_argument('expiration', required=True)

        args = parser.parse_args()

        entries[title] = args

        return {'message': 'Note updated successfully', 'data': args}, 202

    def delete(self, title):
        entries = database()

        if not (title in entries):
            return {'message': 'Note does not exist', 'data': {}}, 404

        del entries[title]

        return '', 204
        
        
# duombazes uzkrovimas
def database():
    if 'db' not in g:
        g.db = shelve.open('notes.db')

    return g.db

# duombazes panaikinimas
@app.teardown_appcontext
def teardown_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()
