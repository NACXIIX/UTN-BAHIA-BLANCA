from socio import Socio
from fecha import Fecha

class Libro:
    
    def __init__(self, nombre:str, autor:str, editorial:str, categoria:str):
        if not isinstance ((nombre,autor,editorial), str):
            raise TypeError("Los valores ingresados en nombre, autor y editorial deben ser un string.")
        else:
            self.__nombre = nombre
            self.__autor = autor
            self.__editorial = editorial
        if isinstance(categoria, str) and len(categoria) == 1:
            self.__categoria = categoria
        else:
            raise TypeError("El valor ingresado por parametro en categoría debe ser un caracter.")
    
    def obtenerNombre(self):
        return self.__nombre

    def obtenerAutor(self):
        return self.__autor

    def obtenerEditorial(self):
        return self.__editorial
    
    def obtenerCategoria(self):
        return self.__categoria
    
    def __str__(self):
        return f"Nombre del libro: {self.__nombre}\nNombre del autor: {self.__autor}\nNombre de editorial: {self.__editorial}\nCategoria: {self.__categoria}"