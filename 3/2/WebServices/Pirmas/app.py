from flask import Flask
from flask_restful import Api
import markdown
from User import Users, UserList, fill_start

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    """Api documentation"""
    #fill_start()
    with open('README.md', 'r') as markdown_file:
        # Read file and convert it to HTML
        content = markdown_file.read()

        return markdown.markdown(content)


# Conference attendees
api.add_resource(UserList, '/<int:cid>/users')
# Specific person
api.add_resource(Users, '/<int:cid>/users/<string:email>')


if __name__ == '__main__':
    try:
        app.run(host="0.0.0.0", port=5009, debug=True)
        
    except:
        print ('')
