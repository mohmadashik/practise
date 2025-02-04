from flask import Flask ,request
from functools import wraps

app = Flask(__name__)

def token_required(func):
    @wraps(func)
    def check_token(*args,**kwargs):
        data = request.get_json()
        print(f'data : {data}')
        token = data.get('token')
        if token =='valid':
            return func(*args,**kwargs)
        else:
            return 'Invalid token', 403
    return check_token

@app.route('/profile')
@token_required
def profile():
    return 'profile page'


# if __name__ =='__main__':
#     app.run(debug=True)

app.run(debug=True)



