from flask import Flask, render_template, request
from redis import Redis
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import os
import markdown

app = Flask(__name__)
redis = Redis(host='redis',port=5000)

#from wtforms.validators import DataRequired

class ReusableForm(Form):
    name = TextField('Name:', validators=[])

# index.html vaizdas
@app.route('/', methods=["GET", "POST"])
def home():
    form = ReusableForm(request.form)
 
    print (form.errors)
    if request.method == 'POST':
        if 'new_task' in request.form:
            name = request.form['name']
            print (name)
            return 'post request - creating new entry'
        
    #if request.method == 'GET':
    #    if 'all_tasks' in request.form:
    #        return 'all jsons here'
    
    return render_template('home.html', form=form)

@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == 'GET':
        return 'All tasks here'
    return 'all tasks here'

#def index():
#        indFile = open('README.md', 'r')
#        content = indFile.read()
#        return markdown.markdown(content)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
