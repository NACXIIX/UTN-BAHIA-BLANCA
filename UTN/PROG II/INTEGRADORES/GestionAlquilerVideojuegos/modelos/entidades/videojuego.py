class Videojuego:
    @classmethod
    def fromDict(cls, data:dict)->'Videojuego':
        if not isinstance (data, dict):
            raise TypeError ("El valor ingresado por parametro en data debe ser un diccionario.")
        return cls(data["id"],data["titulo"], data["desarrollador_id"], data["fecha_lanzamiento"], data["genero_id"])
    
    def __init__(self, id:int, titulo:str, desarrollador_id:int, fecha_lanzamiento:str, genero_id:int):
        if not isinstance (id, int) or id < 0:
            raise TypeError("El valor ingresado por parametro en id debe ser un numero entero positivo.")
        if not isinstance (titulo, str) or titulo.isspace() or titulo == "":
            raise TypeError("El valor ingresado por parametro en titulo debe ser un string.")
        if not isinstance (desarrollador_id, int) or id < 0:
            raise TypeError("El valor ingresado por parametro en desarrollador_id debe ser un numero entero positivo.")
        if not isinstance (fecha_lanzamiento, str) or fecha_lanzamiento.isspace() or fecha_lanzamiento == "":
            raise TypeError("El valor ingresado por parametro en fecha_lanzamiento debe ser string.")
        if not isinstance (genero_id, int) or genero_id < 0:
            raise TypeError("El valor ingresado por parametro en genero_id debe ser un numero entero positivo.")
        
        self.__id = id
        self.__titulo = titulo
        self.__desarrollador_id = desarrollador_id
        self.__fecha_lanzamiento = fecha_lanzamiento
        self.__genero_id = genero_id
    
    def obtenerID(self)->int:
        return self.__id
    
    def obtenerTitulo(self)->str:
        return self.__titulo
    
    def obtenerDesarrolladorID(self)->int:
        return self.__desarrollador_id
    
    def obtenerFechaLanzamiento(self)->str:
        return self.__fecha_lanzamiento
    
    def genero_id(self)->int:
        return self.__genero_id
    
    def establecerID(self, id:int):
        self.__id = id
    
    def establecerTitulo(self, titulo:str):
        self.__titulo = titulo
        
    def establecerDesarrolladorID(self, desarrollador_id:int):
        self.__desarrollador_id = desarrollador_id
    
    def establecerFechaLanzamiento(self, fecha_lanzamiento:str):
        self.__fecha_lanzamiento = fecha_lanzamiento
    
    def establecerGeneroID(self, genero_id:int):
        self.__genero_id = genero_id
    
    def toDict(self)->dict:
        return {
            "id" : self.__id,
            "titulo" : self.__titulo,
            "desarrollador_id" : self.__desarrollador_id,
            "fecha_lanzamiento" : self.__fecha_lanzamiento,
            "genero_id" : self.__genero_id
        }