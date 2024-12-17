from flask import request, jsonify, Blueprint
from modelos.repos.repositorios import obtenerRepositorioDesarrolladoras

repo_Desarrolladoras = obtenerRepositorioDesarrolladoras()
bp_desarrolladoras = Blueprint("bp_desarrolladoras", __name__)

@bp_desarrolladoras.route("/desarrolladoras", methods = ["GET"])
def obtenerDesarrolladoras():
    return jsonify ([desarrolladora.toDict() for desarrolladora in repo_Desarrolladoras.obtenerTodas()])

@bp_desarrolladoras.route("/desarrolladoras/<int:id>", methods = ["GET"])
def obtenerDesarrolladora(id):
    videojuego = repo_Desarrolladoras.obtenerPorID(id)
    if repo_Desarrolladoras.existeDesarrollador(id):
        response = jsonify(videojuego.toDict())
        status_code = 200
    else:
        response = jsonify ({"error": "La desarrolladora no existe."})
        status_code = 404
    return response, status_code

@bp_desarrolladoras.route("/desarrolladoras", methods = ["POST"])
def agregarDesarrolladora():
    if request.is_json:
        data = request.get_json()
        if not "id" in data and not "nombre" in data and not "pais" in data:
            response = jsonify ({"error": "Faltan datos"})
            status_code = 400
        else:
            id = data["id"]
            nombre = data["nombre"]
            pais = data["pais"]
            if repo_Desarrolladoras.agregarDesarrolladora(id, nombre, pais):
                response = jsonify({"mensaje": "Desarrolladora agregada satisfactoriamente"})
                status_code = 200
            else:
                response = jsonify({"error": "Error al agregar la desarrolladora."})
                status_code = 400
    else:
        response = jsonify({"error": "El contenido debe ser un json"})
        status_code = 400
    return response, status_code

@bp_desarrolladoras.route("/desarrolladoras/<int:id>", methods = ["PUT"])
def modificarDesarrolladora(id):
    if request.is_json:
        data = request.get_json()
        if not "id" in data and not "nombre" in data and not "pais" in data:
            response = jsonify ({"error": "Faltan datos"})
            status_code = 400
        else:
            nombre = data["nombre"]
            pais = data["pais"]
            if repo_Desarrolladoras.modificarPorID(id,nombre,pais):
                response = jsonify({"mensaje": "Desarrolladora modificada satisfactoriamente"})
                status_code = 200
            else:
                response = jsonify({"error": "Error al modificar la desarrolladora."})
                status_code = 400
    else:
        response = jsonify({"error": "El contenido debe ser un json"})
        status_code = 400
    return response, status_code

@bp_desarrolladoras.route("/desarrolladoras/<int:id>", methods = ["DELETE"])
def eliminarDesarrolladora(id):
    if repo_Desarrolladoras.eliminarPorID(id):
        response = jsonify({"mensaje": "Desarrolladora eliminada satisfactoriamente"})
        status_code = 200
    else:
        response = jsonify({"error": "Error eliminar la desarrolladora."})
        status_code = 400
    return response, status_code