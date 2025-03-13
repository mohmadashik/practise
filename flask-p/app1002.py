from flask import Flask 
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self,user_id):
        return 'User Get API'
    
api.add_resource('/<user_id>')