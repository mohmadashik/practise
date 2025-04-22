from flask import Flask
app = Flask(__name__)

@app.route('/<string:name>')
def index(name):
    return f'hello world  matter{name}'


app.run(debug=True)
