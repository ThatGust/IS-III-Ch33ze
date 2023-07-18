from flask import Flask, request, jsonify, render_template, redirect, flash, session
from flask_session import Session

import json
import requests

from flask_cors import CORS, cross_origin

from Backend.blueprints.task_blueprint import task_blueprint
from Backend.models.task_model import TaskModel

host = 'http://localhost:5000'

model = TaskModel()

app = Flask(__name__, template_folder='Frontend',
            static_folder='Frontend/static')

app.register_blueprint(task_blueprint) 

cors = CORS(app)

app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'h2g3h32gh2'

Session(app)
#################### ERRORES ########################

# Manejador de error para el código de respuesta 403

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

def get_user_role(iduser):
    # Verificar si el ID se encuentra en la tabla profesor
    if model.get_profesor(iduser):
        return 'profesor'

    # Verificar si el ID se encuentra en la tabla estudiante
    if model.get_estudiante(iduser):
        return 'estudiante'

    # Verificar si el ID se encuentra en la tabla administrador
    if model.get_administrador(iduser):
        return 'admin'

    # El ID no se encuentra en ninguna de las tablas secundarias
    return 'usuario'

###################### RUTAS ########################


@app.route('/')
def index():
    return render_template('home/index.html')


# @app.route('/dashboard')
# def dashboard():
#     return render_template('home/dashboard.html')


@app.route('/dashboard')
def dashboard():
    if 'username' in session and 'role' in session and 'iduser' in session:
        username = session['username']
        role = session['role']
        
        if role == 'admin':
            # Mostrar página de administrador
            return render_template('home/admin/Adashboard.html', username=username)
        elif role == 'estudiante':
            # Mostrar página de usuario normal
            return render_template('home/student/Sdashboard.html', username=username)
        elif role == 'profesor':
            # Mostrar página de profesor
            return render_template('home/teacher/Tdashboard.html', username=username)
        elif role == 'usuario':
            # Mostrar página de usuario
            return render_template('home/index.html', username=username)
    
    # Redirigir a la página de inicio de sesión si no hay sesión válida
    return redirect('/login')


@app.route('/profesores')
def teacher():
    return render_template('home/teachers.html')


@app.route('/correos')
def mail():
    return render_template('home/mails.html')


@app.route('/profile')
def profile():
    return render_template('/home/profile.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = authenticate_user(username, password)

        if user:
            # Establecer los datos de sesión para el usuario
            session['username'] = user['username']
            session['role'] = get_user_role(user['iduser'])
            session['iduser'] = user['iduser']

            return redirect('/')
        else:
            flash('Error, intentelo de nuevo', 'error')

    return render_template('accounts/login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        data = {
            'username': username,
            'password': password
        }

        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            host + '/user/add_user', json=data, headers=headers)

        return redirect('/')

    return render_template('accounts/register.html')

@app.route('/postulacion')
def postulacion():
    
    return render_template('/home/postulant.html')


@app.route('/registerteacher', methods=['GET', 'POST'])
def register_teacher():
    if 'username' in session and 'role' in session and 'iduser' in session:
        username_ = session['username']
        iduser_ = session['iduser']

        if request.method == 'POST':
            nombre = request.form['first_name']
            apellidoP = request.form['apellido_paterno']
            apellidoM = request.form['apellido_materno']
            dni = request.form['dni']
            mail = request.form['mail']
            celular = request.form['telefono_celular']
            ciudad = request.form['city']
            datePos = request.form['datef']
            curso = request.form['course']
            data = {
                'iduser': iduser_,
                'nombre': nombre,
                'apellidoP': apellidoP,
                'apellidoM': apellidoM,
                'dni': dni,
                'correo': mail,
                'celular': celular,
                'ciudad': ciudad,
                'datePos': datePos,
                'curso': curso,
                'estado': "Pendiente"
            }

            headers = {'Content-Type': 'application/json'}
            response = requests.post(
                host + '/postulant/add_postulant', json=data, headers=headers)

            return redirect('/dashboard')

        return render_template('home/register-teacher.html', username=username_)
    else:
        return redirect('/login')

@app.route('/postulant')
def postulant():
    data_ = model.get_postulants()
    return render_template('/home/postulant.html', data=data_)

@app.route('/logout')
def logout():
    # Eliminar la información de sesión del usuario
    session.pop('username', None)
    session.pop('role', None)

    # Redirigir al usuario a la página de inicio
    return render_template('home/index.html')

if __name__ == "__main__":
      app.run(debug=True)
