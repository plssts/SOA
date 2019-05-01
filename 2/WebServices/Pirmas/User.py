import shelve
import requests
from flask import Flask, g
from flask_restful import Resource, reqparse

app = Flask(__name__)

class UserList(Resource):
    def get(self, cid):
        entries = get_db()
        
        if not (str(cid) in entries):
            return {'message': 'No members as of yet', 'data': {}}, 404

        keys = list(entries[str(cid)].keys())
        return {'message': 'Conference members', 'data': entries[str(cid)]}, 200

    def post(self, cid):
        entries = get_db()
        
        previous = list(entries[str(cid)].keys()) if str(cid) in entries else []
        return {'message': previous}
        
        parser = reqparse.RequestParser()
        parser.add_argument('firstName', required=True)
        parser.add_argument('lastName', required=True)
        parser.add_argument('email', required=True)
        args = parser.parse_args()
        
        if args['email'] in previous:
            return {'message': 'This member is already participating', 'data': args['email']}, 409

        entries[str(cid)][args['email']] = args

        return {'message': 'New attendee added', 'data': args['email']}, 201


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
        db = g._database = shelve.open("attendees.db")
    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
