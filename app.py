import json
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from utils import _send_email
from pprint import pprint
app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('task')


# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class SendEmail(Resource):
    def get(self):
        return None, 202 

    def post(self):
        print("post")
        d = request.form
        #d = {'{"_id":"59f444e1e2bb163439f9cf3f","updatedAt":"2017-10-28T08:50:41.418Z","createdAt":"2017-10-28T08:50:41.418Z","debted":{"_id":"59f431d93a25a3202f86aa04","updatedAt":"2017-10-28T07:29:29.526Z","createdAt":"2017-10-28T07:29:29.526Z","email":"evertdiazb@pagape.com","password":"$2a$10$Z.rHnTVqm/QeWq1.oGngZe5uwax1Ngu5yQXtCDk.vUfuP0IJl5ZG.","__v":0,"tokens":[],"active":false},"debtor":{"_id":"59f44375b675e9332c7f5bac","updatedAt":"2017-10-28T08:44:37.760Z","createdAt":"2017-10-28T08:44:37.760Z","password":"$2a$10$/ci2p166jrAeEr6NyST8xO0RQM.Ou9n5VKYxUWezea79kR7P0xeH2","__v":0,"tokens":[],"active":true},"description":"Deuda de un cuy","endDate":"2017-11-24T00:00:00.000Z","amount":10000,"__v":0,"accepted":false,"status":0}': ''}
        print(d.keys())
        data = None
        for d in d.keys():
            data = d
        data = json.loads(data)
        pprint(data)
        email = data['debtor']['email']
        description = data['description']
        endDate = data['endDate']
        amount = data['amount']
        name = data['debtor']['profile']['name']
        confirmation = data['_id']
        status = _send_email(email, name, description,
                             endDate, amount, confirmation)
        return status, 201


##
## Actually setup the Api resource routing here
##
api.add_resource(SendEmail, '/')


if __name__ == '__main__':
    app.run(debug=True)