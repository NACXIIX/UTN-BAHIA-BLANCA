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
                raise TypeError("El valor ingresado por parametro debe ser de tipo Fecha.")

socio_1 = Socio("Bigotin", Fecha(15,10,205),"je")