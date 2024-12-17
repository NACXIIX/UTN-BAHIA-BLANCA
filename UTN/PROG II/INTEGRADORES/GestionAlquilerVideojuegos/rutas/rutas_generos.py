from flask import request, jsonify, Blueprint
from modelos.repos.repositorios import obtenerRepositorioGeneros

repo_Generos = obtenerRepositorioGeneros()

bp_generos = Blueprint("bp_generos", __name__)

@bp_generos.route("/generos", methods = ["GET"])
def obtenerGeneros():
    return jsonify ([genero.toDict() for genero in repo_Generos.obtenerTodos()]), 200

@bp_generos.route("/generos/<int:id>", methods = ["GET"])
def obtenerGenero(id):
    genero = repo_Generos.obtenerPorID(id)
    if repo_Generos.existeGenero(id):
        response = jsonify([genero.toDict()])
        status_code = 200
    else:
        response = jsonify({"error": "El id del genero no existe"})
        status_code = 404
    return response, status_code

@bp_generos.route("/generos", methods = ["POST"])
def agregarGenero():
    if request.is_json:
        data = request.get_json()
        if not "id" in data and not "nombre" in data and not "descripcion" in data:
            response = jsonify({"error": "Faltan datos"})
            status_code = 404
        else:
            id = data["id"]
            nombre = data["nombre"]
            descripcion = data["descripcion"]
            if repo_Generos.agregarGenero(id,nombre,descripcion):
                response = {"genero": repo_Generos.obtenerPorID(id).toDict(), "mensaje": "Genero agregado satisfactoriamente."}
                status_code = 201
            else:
                response = jsonify ({"error": "Error al agregar el genero"})
                status_code = 400
    else:
        response = jsonify({"error": "El contenido debe ser en formato json."})
        status_code = 400
    return response, status_code

@bp_generos.route("/generos/<int:id>", methods = ["PUT"])
def modificarGenero(id):
    if request.is_json:
        data = request.get_json()
        if not "id" in data and not "nombre" in data and not "descripcion" in data:
            response = jsonify({"error": "Faltan datos"})
            status_code = 404
        else:
            id = data["id"]
            nombre = data["nombre"]
            descripcion = data["descripcion"]
            if repo_Generos.modificarGenero(id, nombre, descripcion):
                response = jsonify({"mensaje": "Genero modificado satisfactoriamente"})
                status_code = 200
            else:
                response = jsonify({"error": "Error al modificar el genero"})
                status_code = 400   
    else:
        response = jsonify({"error": "El contenido debe ser en formato json."})
        status_code = 400
    return response, status_code

@bp_generos.route("/generos/<int:id>", methods = ["DELETE"])
def eliminarGenero(id):
    if repo_Generos.eliminarGenero(id):
        response = jsonify({"mensaje": "Genero eliminado satisfactoriamente"})
        status_code = 200
    else:
        response = jsonify({"error": "Error al eliminar el genero"})
        status_code = 400
    return response, status_code