from flask import Flask
from redis import Redis
import os
import markdown

app = Flask(__name__)
redis = Redis(host='redis',port=5000)

# index.html vaizdas
@app.route('/')
def index():
        indFile = open('README.md', 'r')
        content = indFile.read()
        return markdown.markdown(content)

if __name__ == "__main__":
        app.run(host="0.0.0.0",debug=True)
