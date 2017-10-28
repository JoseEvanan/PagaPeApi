"""
import os
import requests
from flask import Flask, render_template, request
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/', methods=['GET', 'POST'])
def send_mail():
    errors = []
    results = {}
    if request.method == "POST":
        # get url that the person has entered
        try:
            url = request.form['url']
            print(url)
        except Exception as e:
            print(e)
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
            return render_template('index.html', errors=errors)
    return render_template('index.html', errors=errors)

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()

"""
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from utils import _send_email
app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('task')


# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return None, 202 

    def post(self):
        email = request.form['email']
        status = _send_email(email, name|, )
        return True, 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/')


if __name__ == '__main__':
    app.run(debug=True)