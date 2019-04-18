from flask import Flask, g
from flask_restful import Resource, reqparse
import shelve
import requests

app = Flask(__name__)

class Members(Resource):
    def get(self, email):
        r = requests.get('http://usr:5009/users/' + email)
        return r.json()
        
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