from modelos.entidades.libro import Libro
from modelos.entidades.prestamo import Prestamo
from modelos.entidades.socio import Socio
import json
class RepositorioPrestamos:
    FILE_PATH = "datos/prestamos.json"
    
    def __init__(self):
        self.__prestamos = self.__cargarTodos()
        
    def __cargar_todos(self):
        lista = []
        try:
            with open (RepositorioPrestamos.FILE_PATH, "r") as file:
                prestamos = json.load(file)
                for prestamo in prestamos:
                    lista.append(Prestamo.fromDiccionario(prestamo))
        except:
            ValueError("No se encontro el archivo json")
            
        return lista