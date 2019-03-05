from flask import Flask, g
from flask_restful import Resource, reqparse
import shelve

app = Flask(__name__)

class NotesList(Resource):
    def get(self):
        entries = get_db()
        elements = list(entries.keys())

        notes = [entries[e] for e in elements]

        return {'message': 'Success', 'data': notes}, 200
