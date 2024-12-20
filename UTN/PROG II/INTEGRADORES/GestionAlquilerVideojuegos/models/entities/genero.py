class Genero:
    @classmethod
    def fromDict(cls, data:dict)->'Genero':
        if not isinstance(data, dict):
            raise TypeError("El valor ingresado por parametro en dict debe ser un diccionario")
        return cls(data["id"], data["nombre"], data["descripcion"])
    
    def __init__(self, id:int, nombre:str, descripcion:str):
        if not isinstance(id, int) or id < 0:
            raise TypeError("El valor ingresdao por parametro en id debe ser un numero entero positivo.")
        if not isinstance(nombre, str) or nombre.isspace() or nombre == "":
            raise TypeError("El valor ingresado por parametro en nombre debe ser un string")
        if not isinstance(descripcion, str) or descripcion.isspace() or descripcion == "":
            raise TypeError("El valor ingresado por parametro en descripcion debe ser un string")
    
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        
    def establecerID(self, id:int):
        self.__id = id
        
    def establecerNombre(self, nombre:str):
        self.__nombre = nombre
        
    def establecerDescripcion(self, descripcion:str):
        self.__descripcion = descripcion
        
    def obtenerID(self)->int:
        return self.__id
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerDescripcion(self)->str:
        return self.__descripcion
    
    def toDict(self)->dict:
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "descripcion": self.__descripcion
        }