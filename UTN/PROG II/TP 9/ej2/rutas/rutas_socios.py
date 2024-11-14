from flask import jsonify, Blueprint, request
from modelos.entidades.socio import Socio
from modelos.repos.repositorios import obtenerRepositorioSocios

repo_Socios = obtenerRepositorioSocios()

bp_socios = Blueprint("bp_socios", __name__)

@bp_socios.route("/socios", methods = ["GET"])
def obtener_socios():
    return jsonify([socio.toDiccionario() for socio in repo_Socios.obtenerTodos()])

@bp_socios.route("/socios/<int:DNI>", methods = ["GET"])
def obtener_socio(DNI):
        socio_encontrado = repo_Socios.obtenerPorDNI(DNI)
        if isinstance(socio_encontrado, Socio):
            return jsonify(socio_encontrado.toDiccionario()), 200
        else:
            return jsonify({"mensaje": "Socio no encontrado"}), 400

@bp_socios.route("/socios", methods = ["POST"])
def agregar_socio():
    if request.is_json:
        datos = request.get_json()
        try:
            socio = Socio.fromDiccionario(datos)
            if not repo_Socios.existeDNI(socio.obtenerDNI()):
                repo_Socios.agregar(socio)
                return jsonify(socio.toDiccionario()), 201
            else:
                return jsonify({"error": "Socio ya existente"})
        except ValueError as err:
            return jsonify({"error": str(err)}), 400
    else:
        return jsonify({"mensaje": "el contenido debe ser un JSON"})

@bp_socios.route("/socios/<int:DNI>", methods= ["PUT"])
def actualizar_socio(DNI):
    if request.is_json:
        datos = request.get_json()
        if "nombre" in datos and "apellido" in datos and "mail" in datos and "fecha_nacimiento" in datos:
            nombre = datos["nombre"]
            apellido = datos["apellido"]
            mail = datos["mail"]
            fechaNacimiento = datos["fecha_nacimiento"]
            if repo_Socios.modificarPorDNI(DNI, nombre, apellido, mail, fechaNacimiento):
                return jsonify({"mensaje": "Socio modificado"}), 200
            else:
                return jsonify({"error": "No se encontro el socio"}), 404
        else:
            return jsonify({"error": "Faltan datos"})
    else:
        return jsonify({"error": "El contenido debe ser un json"})
    
@bp_socios.route("/socios/<int:DNI>", methods= ["DELETE"])
def eliminar_socio(DNI):
    if repo_Socios.eliminarPorDNI(DNI):
        return jsonify({"mensaje": "Socio eliminado"}), 200
    else:
        return jsonify({"error": "Socio no encontrado"}), 404
