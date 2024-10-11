from fecha import Fecha

class Socio:
    def __init__(self, nombre:str, fechaNacimiento:'Fecha', fechaPenalizacion:'Fecha' = None):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise TypeError("El valor ingresado por parametro debe ser un string.")
        
        if isinstance(fechaNacimiento, Fecha):
            self.__fechaNacimiento = fechaNacimiento
        else:
            raise TypeError("El valor ingresado por parametro debe ser un objeto de tipo Fecha.")
        
        if fechaPenalizacion != None:
            if isinstance(fechaPenalizacion, Fecha):
                self.__fechaPenalizacion = fechaPenalizacion
            else:
                raise TypeError("El valor ingresado por parametro debe ser un objeto de tipo Fecha.")
        
    def establecerNombre(self, nombre:str):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise TypeError()

    def establecerFechaNacimiento(self, fecha:'Fecha'):
        if isinstance(fecha, Fecha):
            self.__fechaNacimiento = fecha
        else:
            raise TypeError("El valor ingresado por parametro debe ser un objeto de tipo Fecha")
        
    def establecerPenalizacion(self, fechaHasta:Fecha):
        if isinstance(fechaHasta, Fecha):
            self.__fechaNacimiento = fechaHasta
        else:
            raise TypeError("El valor ingresado por parametro debe ser un objeto de tipo Fecha")
        
    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerFechaNacimiento(self):
        return self.__fechaNacimiento

    def obtenerFechaPenalizacion(self):
        return self.__fechaPenalizacion
    
    def estaHabilitado(self, fecha:'Fecha')->bool:
        return self.__fechaPenalizacion == None or self.__fechaPenalizacion.esAnterior(fecha)
    
    def __str__(self):
        return f"Nombre del socio: {self.__nombre}\nFecha de nacimiento: {self.__fechaNacimiento}"


socio_1 = Socio("bigote", Fecha(21,10,1993))
print(socio_1)
