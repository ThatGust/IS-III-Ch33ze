from flask import Flask, request, jsonify, render_template, redirect, flash

import json
import requests

from flask_cors import CORS, cross_origin

from Backend.blueprints.task_blueprint import task_blueprint
from Backend.models.task_model import TaskModel

host = 'http://localhost:5000'

model = TaskModel()

app = Flask(__name__,template_folder='Frontend',static_folder='Frontend/static')
# para que utilice vue compilado ( npm run build ). En la carpeta dist, esta lo compilado de vue
# app = Flask(__name__, template_folder= './Frontend')

app.register_blueprint(task_blueprint)

cors = CORS(app)
app.config['SECRET_KEY'] = 'keyy'

def authenticate_user(username, password):

    user = model.get_user_username(username)
    if user and user['password'] == password:
        return user
    return None

@app.route('/dashboard')
def dashboard():
    return render_template('home/index.html')

@app.route('/profesores')
def teacher():
    return render_template('home/teachers.html')

@app.route('/correos')
def mail():
    return render_template('home/mails.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = authenticate_user(username, password)
        if user:
            return redirect('/dashboard')
        else:
            flash('Error, intentelo de nuevo', 'error')

    return render_template('accounts/login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        data = {
            'username' : username,
            'password' : password
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post(host + '/user/add_user', json=data, headers=headers)

        return redirect('/')
    
    return render_template('accounts/register.html')



if __name__ == "__main__":
    app.run(debug=True)
