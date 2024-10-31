import json

class Libro:
    @classmethod
    def deserializarLibro(cls, json_data:dict)->"Libro":
        if isinstance(json_data, dict):
            datos = json.loads(json_data)
            return cls(datos["nombre"], datos["autor"], datos["genero"], datos["año"], datos["ISBN"])
        else:
            raise TypeError("El valor ingresado por parametro en json_data debe ser de tipo diccionario.")
    
    def __init__(self, nombre:str, autor:str, genero:str, anio:int, ISBN:int):
        if isinstance (nombre, str):
            self.__nombre = nombre
        else:
            raise TypeError("El valor ingresado por parametro en nombre debe ser un string.")
        if isinstance (autor, str):
            self.__autor = autor
        else:
            raise TypeError("El valor ingresado por parametro en autor debe ser un string.")
        if isinstance (genero, str):
            self.__genero = genero
        else:
            raise TypeError("El valor ingresado por parametro en el genero debe ser un string.")
        if isinstance(anio, int) and anio > 0 :
            self.__anio = anio
        else:
            raise TypeError("El valor ingresado por parametro en el año debe ser un numero entero positivo.")
        if isinstance(ISBN, int) and ISBN > 0:
            ISBN_string = str(ISBN)
            if self.__anio < 2007:
                if not len(ISBN_string) == 10:
                    raise ValueError("El ISBN antes del 2007 debe ser un numero de 10 digitos")
            else:
                if not len(ISBN_string) == 13:
                    raise ValueError("El ISBN antes del 2007 debe ser un numero de 13 digitos")
            self.__ISBN = ISBN
        else:
            raise TypeError("El valor ingresado por parametro en ISBN debe ser de tipo entero.")
        
    def serializarLibro(self)->dict:
        diccLibro = {
            "nombre": self.__nombre, 
            "autor": self.__autor, 
            "genero": self.__genero, 
            "año": self.__anio, 
            "ISBN": self.__ISBN
            }
        
        return diccLibro

class TesterLibro:
    @staticmethod
    def test():
        
        with open("libros.json", "r", encoding="utf-8") as file:
            archivo = json.load(file)

        pedir_anio = int(input("Digite un año y le daremos los libros de ese año: "))
        lista_pedido = [libro for libro in archivo if libro["año"] == pedir_anio]

        print(lista_pedido)

TesterLibro.test()