from flask import Flask, render_template, request, g, jsonify
from flask_restful import Api, Resource, reqparse
import os
import markdown
import requests
import json

app = Flask(__name__)
progInterface = Api(app)

class Conference(Resource):
    def get(self):
        headers = {'Accept': 'application/json'}
        r = requests.get('http://usr:5009/users', headers=headers)
        return json.dumps(r.text)

# index vaizdas
@app.route('/', methods=["GET", "POST"])
def home():
    return markdown.markdown(open('README.md', 'r').read())

progInterface.add_resource(Conference, '/c')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
