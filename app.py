from flask import Flask, render_template, request
from redis import Redis
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
import os
import markdown

app = Flask(__name__)
redis = Redis(host='redis',port=5000)

#from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    age = InterField('age', validators=[DataRequired()])

# index.html vaizdas
@app.route('/', methods=["GET", "POST"])
def home():
    form = MyForm(request.form)
 
    print (form.errors)
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        print (name, age)
    return render_template('home.html')

@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == 'POST':
        return 'All tasks here'

#def index():
#        indFile = open('README.md', 'r')
#        content = indFile.read()
#        return markdown.markdown(content)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
