from flask import Flask, render_template, request
from redis import Redis
import os
import markdown

app = Flask(__name__)
redis = Redis(host='redis',port=5000)

# index.html vaizdas
@app.route('/', methods=["GET"])
def home():
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
