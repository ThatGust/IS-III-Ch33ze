from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from Backend.models.task_model import TaskModel

task_blueprint = Blueprint('task_blueprint', __name__)

model = TaskModel()

################## USUARIO ##################################


@task_blueprint.route('/user/add_user', methods=['POST'])
@cross_origin()
def create_user():
    content = model.add_user(request.json['username'], request.json['password'])
    return jsonify(content)

@task_blueprint.route('/user/delete_user', methods=['POST'])
@cross_origin()
def delete_user():
    return jsonify(model.delete_user(int(request.json['iduser'])))

@task_blueprint.route('/user/get_user', methods=['POST'])
@cross_origin()
def user():
    return jsonify(model.get_user(int(request.json['iduser'])))

@task_blueprint.route('/user/get_users', methods=['POST'])
@cross_origin()
def users():
    return jsonify(model.get_users())


################# Administrador ################################

@task_blueprint.route('/administrador/add_administrador', methods=['POST'])
@cross_origin()
def create_administrador():
    content = model.add_administrador(request.json['rol']) 
    return jsonify(content)    

@task_blueprint.route('/administrador/delete_administrador', methods=['POST'])
@cross_origin()
def delete_administrador():
    return jsonify(model.delete_administrador(int(request.json['ID_Administrador'])))

@task_blueprint.route('/administrador/get_administrador', methods=['POST'])
@cross_origin()
def administrador():
    return jsonify(model.get_administrador(int(request.json['ID_Administrador'])))

@task_blueprint.route('/administrador/get_administradors', methods=['POST'])
@cross_origin()
def administradors():
    return jsonify(model.get_administradors())



################# Contribuidor ################################

@task_blueprint.route('/contribuidor/add_contribuidor', methods=['POST'])
@cross_origin()
def create_contribuidor():
    content = model.add_contribuidor(request.json['nombre'], request.json['universidad'], request.json['especialidad'], request.json['descripcion'], request.json['facebool'], request.json['email'], request.json['linkedin'], request.json['rol']) 
    return jsonify(content)

@task_blueprint.route('/contribuidor/delete_contribuidor', methods=['POST'])
@cross_origin()
def delete_contribuidor():
    return jsonify(model.delete_contribuidor(int(request.json['ID_Contribuidor'])))

@task_blueprint.route('/contribuidor/get_contribuidor', methods=['POST'])
@cross_origin()
def contribuidor():
    return jsonify(model.get_contribuidor(int(request.json['ID_Contribuidor'])))

@task_blueprint.route('/contribuidor/get_contribuidors', methods=['POST'])
@cross_origin()
def contribuidors():
    return jsonify(model.get_contribuidors())

