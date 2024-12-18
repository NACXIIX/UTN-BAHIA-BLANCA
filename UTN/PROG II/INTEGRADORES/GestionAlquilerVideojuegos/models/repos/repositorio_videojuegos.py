from models.entidades.videojuego import Videojuego
import json
import os

class Repo_videojuegos:
    __FILE_PATH = "data/videojuegos.json"
    
    def __init__(self):
        self.__videojuegos = self.__cargarTodos()
        
    def __cargarTodos(self):
        lista = []
        
        try:
            with open (Repo_videojuegos.__FILE_PATH, "r") as file:
                data = json.load(file)
                for videojuego in data:
                    lista.append(Videojuego.fromDict(videojuego))
        except FileNotFoundError:
            print (f"No se encontró el archivo videojuegos.json en la ruta {Repo_videojuegos.__FILE_PATH}")
        except json.JSONDecodeError as err:
            print(f"El archivo videojuegos.json esta vacío o puede tener datos invalidos.\nERROR: {err}")
        except Exception as err:
            print(f"El archivo videojuegos.json tiene un error inesperado: {err}")
        return lista
    
    def __guardarTodos(self):
        lista = []
        for videojuego in self.__videojuegos:
            lista.append(videojuego.toDict())
        
        try:
            with open(Repo_videojuegos.__FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(lista, file, indent=4)
        except FileNotFoundError:
            print ("No se encontró el archivo json.")
        
    def obtenerPorID(self, id):
        for videojuego in self.__videojuegos:
            if videojuego.obtenerID() == id:
                return videojuego
        return None
    
    def existeID(self, id):
        for videojuego in self.__videojuegos:
            if videojuego.obtenerID() == id:
                return True
        return False
    
    def obtenerTodos(self):
        return self.__videojuegos
    
    # POST
    def agregarVideojuego(self, id, titulo, desarrollador_id, fecha_lanzamiento, genero):
        if not self.existeID(id):
            self.__videojuegos.append(Videojuego(id, titulo, desarrollador_id, fecha_lanzamiento, genero))
            self.__guardarTodos()
            return True
        return False
    
    # DELETE
    def eliminarVideojuego(self, id):
        for videojuego in self.__videojuegos:
            if videojuego.obtenerID() == id:
                self.__videojuegos.remove(videojuego)
                self.__guardarTodos()
                return True
        return False
    
    # UPDATE
    def modificarVideojuego(self, id, titulo, desarrollador_id, fecha_lanzamiento, genero):
        for videojuego in self.__videojuegos:
            if videojuego.obtenerID() == id:
                videojuego.establecerTitulo(titulo)
                videojuego.establecerDesarrolladorID(desarrollador_id)
                videojuego.establecerFechaLanzamiento(fecha_lanzamiento)
                videojuego.establecerGeneroID(genero)
                self.__guardarTodos()
                return True
        return False
