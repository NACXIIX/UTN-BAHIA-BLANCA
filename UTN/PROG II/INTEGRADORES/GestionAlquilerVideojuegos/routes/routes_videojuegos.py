from flask import request, jsonify, Blueprint, render_template
from models.repos.repositorios import obtenerRepositorioVideojuegos

repo_Videojuegos = obtenerRepositorioVideojuegos()

bp_videojuegos = Blueprint("bp_videojuegos", __name__)

@bp_videojuegos.route("/videojuegos", methods = ["GET"])
def obtenerVideojuegos():
    response = [videojuego.toDict() for videojuego in repo_Videojuegos.obtenerTodos()]
    
    is_navigator = "Mozilla" in request.user_agent.string or "Chrome" in request.user_agent.string
    if not is_navigator:
        return jsonify(response), 200
    
    return render_template("videojuegos.html", videojuegos=response, contador_videojuegos = 1)

@bp_videojuegos.route("/videojuegos/<int:id>", methods = ["GET"])
def obtenerVideojuego(id):
    videojuego = repo_Videojuegos.obtenerPorID(id)
    is_navigator = 'Mozilla' in request.user_agent.string or 'Chrome' in request.user_agent.string
    
    if repo_Videojuegos.existeID(id):
        response = jsonify([videojuego.toDict()])
        status_code = 200
        if is_navigator:
            return render_template(f"/videojuegos.html", videojuego=repo_Videojuegos.obtenerPorID(id))
    else:
        response = jsonify({"mensaje": "El videojuegojuego no existe"})
        status_code = 404
    return response, status_code

@bp_videojuegos.route("/videojuegos", methods = ["POST"])
def agregarVideojuego():
    if request.is_json:
        data = request.get_json()
        if not "id" in data and "titulo" in data and "desarrollador_id" in data and "fecha_lanzamiento" in data and "genero_id" in data:
            response = jsonify ({"error": "Faltan datos"})
            status_code = 400
        else:
            id = data["id"]
            titulo = data["titulo"]
            desarrollador_id = data["desarrollador_id"]
            fecha_lanzamiento = data["fecha_lanzamiento"]
            genero_id = data["genero_id"]
            if repo_Videojuegos.agregarVideojuego(id, titulo, desarrollador_id,fecha_lanzamiento,genero_id):
                response = jsonify({"mensaje": "Juego agregado satisfactoriamente."})
                status_code = 201
            else:
                response = jsonify({"error": "El videojuego ya existe."})
                status_code = 400
    else:
        response = jsonify({"error": "Debe ser en formato json"})
        status_code = 400
    return response, status_code

@bp_videojuegos.route("/videojuegos/<int:id>", methods = ["PUT"])
def modificarVideojuego(id):
    if request.is_json:
        data = request.get_json()
        if not "id" in data and "titulo" in data and "desarrollador_id" in data and "fecha_lanzamiento" in data and "genero_id" in data:
            response = jsonify ({"error": "Faltan datos"})
            status_code = 400
        else:
            id = data["id"]
            titulo = data["titulo"]
            desarrollador_id = data["desarrollador_id"]
            fecha_lanzamiento = data["fecha_lanzamiento"]
            genero_id = data["genero_id"]
            if repo_Videojuegos.modificarVideojuego(id, titulo, desarrollador_id, fecha_lanzamiento, genero_id):
                response = jsonify({"error": "Videojuego modificado satisfactoriamente"})
                status_code = 200
            else:
                response = jsonify({"error": "No se encontró el videojuego"})
                status_code = 404
    else:
        response = jsonify({"error": "Debe ser en formato json"})
        status_code = 400
    return response, status_code

@bp_videojuegos.route("/videojuegos/<int:id>", methods = ["DELETE"])
def eliminarVideojuego(id):
    if repo_Videojuegos.existeID(id):
        if repo_Videojuegos.eliminarVideojuego(id):
            response = jsonify({"mensaje": "Videojuego eliminado satisfactoriamente"})
            status_code = 200
        else:
            response = jsonify({"error": "No se pudo eliminar el videojuego."})
            status_code = 400
    else:
        response = jsonify({"error": "No se encontró el videojuego"})
        status_code = 404
    return response, status_code