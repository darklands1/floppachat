from flask import Flask
from flask_restful import Api

import users, messages

if __name__ == '__main__':
    app = Flask('FloppaChat')
    api = Api(app)
    api.add_resource(users.Users, '/users')
    api.add_resource(messages.Messages, '/messages')
    app.run()
