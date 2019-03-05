from flask import Flask, render_template, request, g
from flask_restful import Api
import os
import markdown
from noteslist import NotesList

app = Flask(__name__)
progInterface = Api(app)

# index vaizdas
@app.route('/', methods=["GET", "POST"])
def home():
    return markdown.markdown(open('README.md', 'r').read())

progInterface.add_resource(NotesList, '/notes')

# duombazes uzkrovimas
def initDatabase():
    if 'db' not in g:
        g.db = connect_to_database()

    return g.db

# duombazes panaikinimas
@app.teardown_appcontext
def teardown_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
