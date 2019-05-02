import shelve
from flask import Flask, g
from flask_restful import Resource, reqparse

app = Flask(__name__)

class UserList(Resource):
    def get(self, cid):
        shelf = get_mem()
        
        if not (str(cid) in shelf):
            return {'message': 'No members as of yet', 'data': {}}, 404

        return {'message': 'Attendees', 'data': shelf[str(cid)]}, 200

    def post(self, cid):
        shelf = get_mem()
        
        previous = shelf[str(cid)] if str(cid) in shelf else []
        
        parser = reqparse.RequestParser()
        parser.add_argument('firstName', required=True)
        parser.add_argument('lastName', required=True)
        parser.add_argument('email', required=True)

        # Parser arguments into obj
        args = parser.parse_args()

        if args['email'] in shelf[str(cid)]:
            return {'message': 'Email Already Exists', 'data': {}}, 409
        
        args['email'] = args
    
        previous.append(args)
        shelf[str(cid)] = previous
        #shelf[args['email']] = args

        return {'message': 'User created', 'data': args}, 201, {'Location': '/users/' + args['email']}


class Users(Resource):
    def get(self, email):
        shelf = get_db()

        if not (email in shelf):
            return {'message': 'User not found', 'data': {}}, 404

        return {'message': 'User', 'data': shelf[email]}, 200

    def put(self, email):
        shelf = get_db()

        if not (email in shelf):
            return {'message': 'User not found', 'data': {}}, 404

        parser = reqparse.RequestParser()

        parser.add_argument('firstName', required=True)
        parser.add_argument('lastName', required=True)
        parser.add_argument('email', required=True)

        # Parser arguments into obj
        args = parser.parse_args()

        if (args['email'] in shelf) and (args['email'] != email):
            return {'message': 'Email Already Exists', 'data': {}}, 409

        del shelf[email]
        shelf[args['email']] = args

        return {'message': 'User updated successfully', 'data': args}, 202

    def patch(self, email):
        parser = reqparse.RequestParser()
        shelf = get_db()

        if not (email in shelf):
            return {'message': 'User not found', 'data': {}}, 404

        parser.add_argument('firstName', required=False)
        parser.add_argument('lastName', required=False)
        parser.add_argument('email', required=False)

        args = parser.parse_args()

        user = shelf[email]

        if not (args['firstName'] is None):
            user['firstName'] = args['firstName']

        if not (args['lastName'] is None):
            user['lastName'] = args['lastName']

        if not (args['email'] is None):
            user['email'] = args['email']
            if args['email'] in shelf:
                return {'message': 'Email Already Exists', 'data': {}}, 409

        del shelf[email]

        if not (args['email'] is None):
            shelf[args['email']] = user
        else:
            shelf[email] = user

        return {'message': 'User updated successfully', 'data': user}, 202, {'Location': '/users/' + email}
        # EDIT: at 104 args['email'] replaced by email

    def delete(self, email):
        shelf = get_db()

        if not (email in shelf):
            return {'message': 'User not found', 'data': {}}, 404

        del shelf[email]

        return '', 204


def fill_start():
    shelf = get_db()
    test_user1 = \
        {
            'firstName': 'Seras',
            'lastName': 'Meras',
            'email': 'eskaferas@gmail.com'
        }
    test_user2 = \
        {
            'firstName': 'Oras',
            'lastName': 'Moras',
            'email': 'Soras@gmail.com'
        }

    if test_user1['email'] in shelf:
        return

    shelf[test_user1['email']] = test_user1
    shelf[test_user2['email']] = test_user2


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("conferences.db")
    return db

def get_mem():
    db = getattr(g, '_members', None)
    if db is None:
        db = g._database = shelve.open("attendees.db")
    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
    db = getattr(g, '_members', None)
    if db is not None:
        db.close()
