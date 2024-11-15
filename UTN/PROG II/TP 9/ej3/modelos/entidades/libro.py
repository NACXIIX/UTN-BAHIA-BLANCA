
class Libro:
    # METODO DE CLASE
    @classmethod
    def fromDiccionario(cls, dic:dict)->"Libro":
        if not isinstance(dic, dict):
            raise TypeError("El valor ingresado por parametro en json_data debe ser de tipo diccionario.")
        if 'ISBN' not in dic:
            raise TypeError("El json debe tener la clave ISBN")
        if 'titulo' not in dic:
            raise TypeError("El json debe tener la clave titulo")
        if 'autor' not in dic:
            raise TypeError("El json debe tener la clave autor")
        if 'genero' not in dic:
            raise TypeError("El json debe tener la clave genero")
        if 'anioPublicacion' not in dic:
            raise TypeError("El json debe tener la clave anioPublicacion")
        if 'cantidadEjemplares' not in dic:
            raise TypeError("El json debe tener la clave cantidadEjemplares")
        return cls(dic['ISBN'], dic['titulo'], dic['autor'], dic['genero'], dic['anioPublicacion'], dic['cantidadEjemplares'])
        
    # METODO DE INSTANCIA
    def __init__(self, ISBN:int, titulo:str, autor:str, genero:str, anioPublicacion:int, cantidadEjemplares:int = 0):
        if isinstance (titulo, str) and not titulo.isspace() and not titulo == "":
            self.__titulo = titulo
        else:
            raise TypeError("El valor ingresado por parametro en titulo debe ser un string.")
        
        if isinstance (autor, str) and not autor.isspace() and not autor == "":
            self.__autor = autor
        else:
            raise TypeError("El valor ingresado por parametro en autor debe ser un string.")
        
        if isinstance (genero, str) and not genero.isspace() and not genero == "":
            self.__genero = genero
        else:
            raise TypeError("El valor ingresado por parametro en el genero debe ser un string.")
        
        if isinstance(anioPublicacion, int) and anioPublicacion > 0 :
            self.__anioPublicacion = anioPublicacion
        else:
            raise TypeError("El valor ingresado por parametro en el año de publicacion debe ser un numero entero positivo.")
        
        if isinstance(ISBN, int) and ISBN > 0:
            ISBN_string = str(ISBN)
            if self.__anioPublicacion < 2007:
                if not len(ISBN_string) == 10:
                    raise ValueError("El ISBN antes del 2007 debe ser un numero de 10 digitos")
            else:
                if not len(ISBN_string) == 13:
                    raise ValueError("El ISBN antes del 2007 debe ser un numero de 13 digitos")
            self.__ISBN = ISBN
        else:
            raise TypeError("El valor ingresado por parametro en ISBN debe ser de tipo entero.")
        
        if isinstance(cantidadEjemplares, int) and cantidadEjemplares > 0:
            self.__cantidadEjemplares = cantidadEjemplares
        else:
            raise TypeError("El valor ingresado por parametro en la cantidad de ejemplares debe ser un numero entero positivo.")
    
    def establecerTitulo(self, titulo):
        self.__titulo = titulo
        
    def establecerAutor(self, autor):
        self.__autor = autor
        
    def establecerGenero(self, genero):
        self.__genero = genero
        
    def establecerAnioPublicacion(self, anioPublicacion):
        self.__anioPublicacion = anioPublicacion
        
    def establecerCantidadEjemplares(self, cantidadEjemplares):
        self.__cantidadEjemplares = cantidadEjemplares
        
    def obtenerISBN(self):
        return self.__ISBN
    
    def obtenerTitulo(self):
        return self.__titulo
    
    def obtenerAutor(self):
        return self.__autor
    
    def obtenerGenero(self):
        return self.__genero
    
    def obtenerAnioPublicacion(self):
        return self.__anioPublicacion

    def obtenerCantidadEjemplares(self):
        return self.__cantidadEjemplares
    
    def esIgual(self, otro:'Libro')->bool:
        if isinstance(otro, Libro):
            return self.__ISBN == otro.obtenerISBN() and self.__titulo == otro.obtenerTitulo() and self.__autor == otro.obtenerAutor() and self.__genero == otro.obtenerGenero() and self.__anioPublicacion == otro.obtenerAnioPublicacion() and self.__cantidadEjemplares == otro.obtenerCantidadEjemplares
        else:
            raise TypeError("El valor ingresado por parametro debe ser un objeto de tipo Libro.")
        
    def toDiccionario(self)->dict:
        diccLibro = {
            "ISBN": self.__ISBN,
            "titulo": self.__titulo, 
            "autor": self.__autor, 
            "genero": self.__genero, 
            "anioPublicacion": self.__anioPublicacion, 
            "cantidadEjemplares": self.__cantidadEjemplares
            }
        return diccLibro
    
    def __str__(self):
        return f"ISBN del libro: {self.__ISBN} - Titulo: {self.__titulo} - Autor: {self.__autor} - Genero: {self.__genero} - Año de Publicacion: {self.__anioPublicacion} - Cantidad de ejemplares: {self.__cantidadEjemplares}"
