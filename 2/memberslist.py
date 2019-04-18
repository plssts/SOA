from flask import Flask, g
from flask_restful import Resource, reqparse
import shelve

app = Flask(__name__)

class MembersList(Resource):
    def get(self):
        r = requests.get('http://usr:5009/users')
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