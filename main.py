from flask import Flask, render_template
import json
from model.User import User

app = Flask(__name__)


@app.route('/')
def index():
    return 'index page'


@app.route('/hello')
def hello():
    return 'hello page'


@app.route('/members')
def get_members():
    return 'members'


@app.route('/members/<string:name>/')
def get_one_member(name):
    user = User('chris', 'jones', 'password')
    return render_template('hello.html', **locals())


@app.route('/users', methods=['POST'])
def get_user_json():
    user = User('chris', 'jones', 'password')
    return json.dumps(user.__dict__)


if __name__ == '__main__':
    app.run()
