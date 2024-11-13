from flask import Blueprint, request, jsonify
from modelos.entidades.libro import Libro
from modelos.repo.repositorios import obtenerRepositorioLibros

repo_Libros = obtenerRepositorioLibros()

bp_libros = Blueprint('bp_libros', __name__)

@bp_libros.route('/libros', methods=['GET'])
def obtener_libros():
    if len(repo_Libros.obtenerTodos()) == 0:
        return jsonify({"mensaje": "No hay ningun libro cargado."})
    else:
        return jsonify([libro.toDiccionario() for libro in repo_Libros.obtenerTodos()])

@bp_libros.route("/libros/<int:ISBN>", methods=["GET"])
def obtener_libro(ISBN):
    libro_encontrado = repo_Libros.obtenerPorISBN(ISBN)
    if isinstance(libro_encontrado, Libro):
        return jsonify(libro_encontrado.toDiccionario())
    else:
        return jsonify({'error':'Libro no encontrado'}), 404

@bp_libros.route("/libros", methods=["POST"])
def agregar_libro():
    if request.is_json:
        data = request.get_json()
        try:
            libro = Libro.fromDiccionario(data)
            repo_Libros.agregar(libro)
            return jsonify(libro.toDiccionario()), 201
        except ValueError as err:
            return jsonify({'error': str(err)}), 400
    else:
        return jsonify({'error': 'el contenido debe ser un JSON'})

@bp_libros.route("/libros/<int:ISBN>", methods=["PUT"])
def modificar_libro(ISBN):
    if request.is_json:
        datos = request.get_json()
        if "titulo" in datos and "autor" in datos and "genero" in datos and "anioPublicacion" in datos:
            titulo = datos['titulo']
            autor = datos['autor']
            genero = datos['genero']
            anioPublicacion = datos ['anioPublicacion']
            if repo_Libros.modificarPorISBN(ISBN, titulo, autor, genero, anioPublicacion):
                return jsonify({"mensaje":"Libro modificado"}), 200
            else:
                return jsonify({"mensaje": "No se encontró el libro"})
        else:
            return jsonify({"error": "Faltan datos"}), 400
    else:
        return jsonify({"error": "El contenido debe ser JSON."})

@bp_libros.route("/libros/<int:ISBN>", methods = ["DELETE"])
def eliminar_libro(ISBN):
    if repo_Libros.obtenerPorISBN(ISBN):
        if repo_Libros.eliminarPorISBN(ISBN):
            return jsonify({"mensaje": "El libro fue eliminado con exito"}), 200
        else:
            return jsonify({"error": "No se encontró el libro"}), 400
    else:
        return jsonify({"error": "No se encontró el libro"}), 400
