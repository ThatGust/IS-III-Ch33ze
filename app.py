from flask import Flask, request, jsonify, render_template, redirect, flash

import json
import requests

from flask_cors import CORS, cross_origin

from Backend.blueprints.task_blueprint import task_blueprint
from Backend.models.task_model import TaskModel

host = 'http://localhost:5000'

model = TaskModel()

app = Flask(__name__,template_folder='Frontend',static_folder='Frontend/static')

app.register_blueprint(task_blueprint)

cors = CORS(app)

app.config['SECRET_KEY'] = 'keyy'

#################### ERRORES ########################

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('home/page-403.html'), 403

# Manejador de error para el código de respuesta 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404

# Manejador de error para el código de respuesta 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500

##################### FUNCIONES ######################

def authenticate_user(username, password):

    user = model.get_user_username(username)
    if user and user['password'] == password:
        return user
    return None

###################### RUTAS ########################

@app.route('/')
def index():
    return render_template('home/indextest.html')

@app.route('/dashboard')
def dashboard():
    return render_template('home/index.html')

@app.route('/profesores')
def teacher():
    return render_template('home/teachers.html')

@app.route('/correos')
def mail():
    return render_template('home/mails.html')

@app.route('/login', methods=['GET', 'POST'])
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

@app.route('/profile')
def profile():
    return render_template('/home/profile.html')
 
@app.route('/registerteacher', methods =['GET', 'POST'])
def register_teacher():
    if request.method == 'POST':

        first_name = request.form['first_name']
        dni = request.form['dni']
        mail = request.form['mail']
        datef = request.form['datef']
        course = request.form['course']

        data = {
            'first_name' : first_name,
            'dni' : dni,
            'mail' : mail,
            'datef' : datef,
            'course' : course
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post(host + '/user/add_postulant', json=data, headers=headers)

        return redirect('/postulant')
    return render_template('home/register-teacher.html')

@app.route('/postulant')
def postulant():
    return render_template('/home/postulant.html')

if __name__ == "__main__":
    app.run(debug=True)
