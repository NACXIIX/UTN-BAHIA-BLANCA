from models.entities.desarrollador import Desarrollador
import json

class Repo_desarrolladoras:
    
    __FILE_PATH = "data/desarrolladoras.json"
    
    def __init__(self):
        self.__desarrolladoras = self.__cargarDesarrolladoras()
    
    def __cargarDesarrolladoras(self)->list:
        lista = []
        try:
            with open (Repo_desarrolladoras.__FILE_PATH, "r") as file:
                data = json.load(file)
                for desarrolladora in data:
                    lista.append(Desarrollador.fromDict(desarrolladora))
        except FileNotFoundError:
            print (f"No se encontró el archivo desarrolladoras.json en la ruta {Repo_desarrolladoras.__FILE_PATH}")
        except json.JSONDecodeError as err:
            print(f"El archivo desarrolladoras.json esta vacío o puede tener datos invalidos.\nERROR: {err}")
        except Exception as err:
            print(f"El archivo desarrolladoras.json tiene un error inesperado: {err}")
        return lista
    
    def __guardarDesarrolladoras(self)->list:
        lista = []
        for desarrolladora in self.__desarrolladoras:
            lista.append(desarrolladora.toDict())
            
        try:
            with open(Repo_desarrolladoras.__FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(lista, file, indent=4)
        except FileNotFoundError:
            print ("No se encontró el archivo json.")

    def obtenerTodas(self)->list:
        return self.__desarrolladoras

    def obtenerPorID(self, id:int)->'Desarrollador':
        if not isinstance(id, int) or id < 1:
            raise TypeError("El valor ingresado por parametro en id debe ser un numero mayor o igual a 1.")
        for desarrolladora in self.__desarrolladoras:
            if desarrolladora.obtenerID() == id:
                return desarrolladora
        return None
    
    def existeDesarrollador(self, id:int)->bool:
        if not isinstance(id, int) or id < 1:
            raise TypeError("El valor ingresado por parametro en id debe ser un numero mayor o igual a 1.")
        for desarrolladora in self.__desarrolladoras:
            if desarrolladora.obtenerID() == id:
                return True
        return False
    
    def modificarPorID(self, id:int, nombre:str, pais:str):
        for desarrolladora in self.__desarrolladoras:
            if desarrolladora.obtenerID() == id:
                desarrolladora.establecerNombre(nombre)
                desarrolladora.establecerPais(pais)
                self.__guardarDesarrolladoras()
                return True
        return False

    def agregarDesarrolladora(self, id:int, nombre:str, pais:str):
        if not self.existeDesarrollador(id):
            nuevaDesarrolladora = Desarrollador(id, nombre, pais)
            self.__desarrolladoras.append(nuevaDesarrolladora)
            return True
        return False
    
    def eliminarPorID(self, id:int):
        if not isinstance(id, int) or id < 1:
            raise TypeError("El valor ingresado por parametro en id debe ser un numero mayor o igual a 1.")
        for desarrolladora in self.__desarrolladoras:
            if desarrolladora.obtenerID() == id:
                self.__desarrolladoras.remove(desarrolladora)
                self.__guardarDesarrolladoras()
                return True
        return False

    
    