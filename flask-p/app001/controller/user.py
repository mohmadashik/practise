from flask import Blueprint

user_bp = Blueprint(url_prefix='user',name='user')

@user_bp.route('/')
def index():
    return 'user index'