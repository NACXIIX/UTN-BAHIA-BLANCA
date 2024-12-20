class Desarrollador:
    @classmethod
    def fromDict(cls, data:dict)->'Desarrollador':
        if not isinstance (data, dict):
            raise TypeError("El valor ingresado por parametro en data debe ser un diccionario.")
        return cls(data["id"], data["nombre"], data["pais"])
    
    def __init__(self, id:int, nombre:str, pais:str):
        if not isinstance (id, int) or id < 0:
            raise TypeError("El valor ingresado por parametro en id debe ser un numero entero positivo.")
        if not isinstance (nombre, str) or nombre.isspace() or nombre == "":
            raise TypeError("El valor ingresado por parametro en nombre debe ser un string.")
        if not isinstance (pais, str) or pais.isspace() or pais == "":
            raise TypeError("El valor ingresado por parametro en pais debe ser un string.")

        self.__id = id
        self.__nombre = nombre
        self.__pais = pais
    
    def obtenerID(self)->int:
        return self.__id
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerPais(self)->str:
        return self.__pais
    
    def establecerID(self, id:int):
        self.__id = id
        
    def establecerNombre(self, nombre:str):
        self.__nombre = nombre
        
    def establecerPais(self, pais:str):
        self.__pais = pais
        
    def toDict(self)->dict:
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "pais": self.__pais
        }