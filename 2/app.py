from flask import Flask, render_template, request, g
from flask_restful import Api
import os
import markdown

app = Flask(__name__)
progInterface = Api(app)

# index vaizdas
@app.route('/', methods=["GET", "POST"])
def home():
    return markdown.markdown(open('README.md', 'r').read())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
