from datetime import datetime
from datetime import date
class Socio:
    @classmethod
    def fromDiccionario(cls, dic: dict)->'Socio':
        if isinstance(dic, dict):
            return cls(dic["DNI"], dic["nombre"], dic["apellido"], dic["mail"], dic["fecha_nacimiento"])
    
    def __init__(self, DNI:int, nombre:str, apellido:str, mail:str, fecha_nacimiento:datetime):
        if not isinstance (DNI, int) and DNI < 0:
            raise TypeError("El valor ingresado por parametro en DNI no debe ser negativo")
        if not isinstance (nombre, str) or nombre.isspace() or nombre == "":
            raise TypeError("El valor ingresado por parametro en nombre debe ser un string")
        if not isinstance (apellido, str) or apellido.isspace() or apellido == "":
            raise TypeError("El valor ingresado por parametro en apellido debe ser un string")
        if not isinstance (mail, str) or mail.isspace() or mail == "":
            raise TypeError("El valor ingresado por parametro en mail debe ser un string")
        try:
            self.__fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
        except ValueError: ("El formato en fecha debe ser dd-mm-aa")

        self.__DNI = DNI
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail = mail
        self.__fecha_nacimiento = fecha_nacimiento
    
    def obtenerDNI(self):
        return self.__DNI
    
    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerApellido(self):
        return self.__apellido
    
    def obtenerMail(self):
        return self.__mail
    
    def obtenerFechaNacimiento(self):
        return self.__fecha_nacimiento
    
    def establecerDNI(self, DNI):
        if not isinstance (DNI, int) and DNI < 0:
            raise TypeError("El valor ingresado por parametro en DNI no debe ser negativo")
        else:
            self.__DNI = DNI
        
    def establecerNombre(self, nombre):
        if not isinstance (nombre, str) or nombre.isspace() or nombre == "":
            raise TypeError("El valor ingresado por parametro en nombre debe ser un string")
        else:
            self.__nombre = nombre
        
    def establecerApellido(self, apellido):
        if not isinstance (apellido, str) or apellido.isspace() or apellido == "":
            raise TypeError("El valor ingresado por parametro en apellido debe ser un string")
        else:
            self.__apellido = apellido
        
    def establecerMail(self, mail):
        if not isinstance (mail, str) or mail.isspace() or mail == "":
            raise TypeError("El valor ingresado por parametro en mail debe ser un string")
        else:
            self.__mail = mail
        
    def establecerFechaNacimiento(self, fecha_nacimiento):
        try:
            self.__fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
        except ValueError: ("El formato ingresado por parametro en fecha de nacimiento debe ser dd-mm-aa")
        
    def esIgual(self, otro: 'Socio')->bool:
        return self.__DNI == otro.obtenerDNI() and self.__nombre == otro.obtenerNombre() and self.__apellido == otro.obtenerApellido() and self.__mail == otro.obtenerMail() and self.__fecha_nacimiento == otro.obtenerFechaNacimiento()
    
    def __str__(self)->str:
        return f"DNI Socio: {self.__DNI} - Nombre: {self.__nombre} - Apellido: {self.__apellido} - Mail: {self.__mail} - Fecha de nacimiento: {self.__fecha_nacimiento}"
    
    def toDiccionario(self)->dict:
        dicc = {
            "dni": self.__DNI,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "mail": self.__mail,
            "fechaNacimiento": self.__fecha_nacimiento
        }
        return dicc
    