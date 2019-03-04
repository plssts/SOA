from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host='redis',port=5000)

@app.route('/')
def hello():
        return "Hello"

if __name__ == "__main__":
        app.run(host="0.0.0.0",debug=True)
