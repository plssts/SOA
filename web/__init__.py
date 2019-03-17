import markdown
import os
import shelve

# Import the framework
from flask import Flask, g, jsonify
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

#duomenu bazes uzkrovimas
def get_db():
    if 'db' not in g:
        g.db = shelve.open("members.db")
    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#README pagrindinis puslapis
@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class MembersList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        members = []

        for key in keys:
            members.append(shelf[key])

        return {'message': 'Success', 'data': members}, 200

    def post(self):
        
        
        parser = reqparse.RequestParser()

        parser.add_argument('name', required=True)
        parser.add_argument('fname', required=True)
        parser.add_argument('phone', required=True)
        parser.add_argument('membership_exp', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()
        
        shelf = get_db()
        if (args['phone'] in shelf):
            return {'message': 'Member already exists', 'data': {}}, 404
            
        
        shelf[args['phone']] = args

        return {'message': 'Member registered', 'data': args}, 201


class Member(Resource):
    def put(self, phone):
        shelf = get_db()
        
        if not (phone in shelf):
            return {'message': 'Member not found', 'data': {}}, 404
            
        parser = reqparse.RequestParser()
    
        parser.add_argument('name', required=True)
        parser.add_argument('fname', required=True)
        parser.add_argument('phone', required=True)
        parser.add_argument('membership_exp', required=True)
    
        # Parse the arguments into an object
        args = parser.parse_args()
    
        shelf = get_db()
        shelf[args['phone']] = args
        del shelf[phone]
        #pakeitimai
    
        return {'message': 'Member registered', 'data': args}, 2012
            
    def get(self, phone):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (phone in shelf):
            return {'message': 'Member not found', 'data': {}}, 404

        return {'message': 'Member found', 'data': shelf[phone]}, 200

    def delete(self, phone):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (phone in shelf):
            return {'message': 'Member not found', 'data': {}}, 404

        del shelf[phone]
        return '', 204

class Name(Resource):#pakeitimas2
     def get(self, name):
        shelf = get_db()

        # Zemiau esancios eilutes israso duombaze tiesiai i GET
        #arr = []
        #for key in shelf.keys():
        #    arr.append(repr(key))
        #    arr.append(repr(shelf[key]))
        #return arr

        # Surenkami elementai su ieskomu name
        arr = [shelf[key] for key in shelf.keys() if name == shelf[key]['name']]
        
        # If the key does not exist in the data store, return a 404 error.
        if arr is None:
            return {'message': 'Member not found', 'data': {}}, 404

        return {'message': 'Member found', 'data': arr}, 200

     
  
class NamesList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        members = []

        for key in keys:
            members.append(shelf[key])

        return {'message': 'Success', 'data': members}, 200
        
api.add_resource(MembersList, '/members')
api.add_resource(Member, '/members/<string:phone>')
api.add_resource(NamesList, '/names')
api.add_resource(Name, '/names/<string:name>')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


