from models.entities.genero import Genero
import json

class Repo_Generos:
    __FILE_PATH = "data/generos.json"
    
    def __init__(self):
        self.__generos = self.__cargarTodos()
    
    def __cargarTodos(self):
        lista = []
        
        try:
            with open(Repo_Generos.__FILE_PATH, "r") as file:
                data = json.load(file)
                for genero in data:
                    lista.append(Genero.fromDict(genero))
        except FileNotFoundError:
            print (f"No se encontró el archivo generos.json en la ruta {Repo_Generos.__FILE_PATH}")
        except json.JSONDecodeError as err:
            print (f"El archivo json no tiene formato json. ERROR {str(err)}")
        except Exception as err:
            print (f"Hubo un error. ERROR: {str(err)}")
        return lista
    
    def __guardarTodos(self):
        lista = []
        for genero in self.__generos:
            lista.append(genero.toDict())
            
        try:
            with open(Repo_Generos.__FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(lista, file, indent=4)
        except FileNotFoundError:
            print ("No se encontró el archivo json")

    def obtenerTodos(self):
        return self.__generos
    
    def obtenerPorID(self, id):
        for genero in self.__generos:
            if genero.obtenerID() == id:
                return genero
        return None
    
    def existeGenero(self, id):
        for genero in self.__generos:
            if genero.obtenerID() == id:
                return True
        return False
    
    # POST
    def agregarGenero(self, id, nombre, descripcion):
        if not self.existeGenero(id):
            self.__generos.append(Genero(id, nombre, descripcion))
            self.__guardarTodos()
            return True
        return False

    # DELETE
    def eliminarGenero(self, id):
        for genero in self.__generos:
            if genero.obtenerID() == id:
                self.__generos.remove(genero)
                self.__guardarTodos()
                return True
        return False
    
    # UPDATE
    def modificarGenero(self, id, nombre, descripcion):
        for genero in self.__generos:
            if genero.obtenerID() == id:
                genero.establecerNombre(nombre)
                genero.establecerDescripcion(descripcion)
                self.__guardarTodos()
                return True
        return False
    