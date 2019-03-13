import markdown
import os
import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

#duomenu bazes uzkrovimas
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("members.db")
    return db

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

class NamesList(Resource):#pakeitimas2
    def get(self, let):
        shelf = get_db()
        keys = list(shelf.keys())
        
        kazkas = [shelve[i] for i in shelf]
        members = []

        for i in shelf:
            
            #if shelve[i].name.cointais(let)
            if let in shelve[i].name: 
                return {'message': 'Member found', 'data': shelf[phone]}, 200
        

        return {'message': 'Member not found', 'data': {}}, 404
     
  
        
        
api.add_resource(MembersList, '/members')
api.add_resource(Member, '/members/<string:phone>')
api.add_resource(NamesList, '/names/<string:let>')#pakeitimas 2




