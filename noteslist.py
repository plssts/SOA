from flask import Flask, g
from flask_restful import Resource, reqparse
import shelve

app = Flask(__name__)

class NotesList(Resource):
    def get(self):
        entries = initDatabase()
        elements = list(entries.keys())

        notes = [entries[e] for e in elements]

        return {'message': 'Success', 'data': notes}, 200
    
# duombazes uzkrovimas
def initDatabase():
    if 'db' not in g:
        g.db = shelve.open('notes.db')

    return g.db

# duombazes panaikinimas
@app.teardown_appcontext
def teardown_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()
