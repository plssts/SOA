from flask import Flask, g, request
from flask_restful import Resource, reqparse
import shelve

app = Flask(__name__)

# Valdo uzrasu saraso gyvavima
class NotesList(Resource):
    # GET - grazinimas
    def get(self):
        entries = database()
        elements = list(entries.keys())
        
        # Parametrizuotas grazinimas
        import urllib.parse as urlparse
        return (request.args)
        parsed = urlparse.urlparse(request.data)
        print (urlparse.parse_qs(parsed.query))

        notes = [entries[e] for e in elements]

        return {'message': 'All notes returned', 'data': notes}, 200
    
    # POST - kurimas
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('title', required=True)
        parser.add_argument('author', required=True)
        parser.add_argument('comment', required=True)
        parser.add_argument('expiration', required=True)

        args = parser.parse_args()

        entries = database()
        entries[args['title']] = args

        return {'message': 'New note added', 'data': args}, 201

    
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
