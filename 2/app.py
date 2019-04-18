from flask import Flask, render_template, request, g, jsonify
from flask_restful import Api, Resource, reqparse
from conferences import Conferences
from members import Members
from memberslist import MembersList
import os
import markdown
import requests
import json

app = Flask(__name__)
progInterface = Api(app)

@app.route('/', methods=["GET", "POST"])
def home():
    requests.get('http://usr:5009/') # Initial call to fill DB
    return markdown.markdown(open('README.md', 'r').read())

progInterface.add_resource(Conferences, '/conferences')
progInterface.add_resource(MembersList, '/members')
progInterface.add_resource(Members, '/members/<string:email>')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
