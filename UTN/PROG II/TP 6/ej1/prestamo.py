from fecha import Fecha
from libro import Libro
from socio import Socio

class Prestamo():
    
    def __init__(self, libro:'Libro', socio:'Socio', fechaPrestamo:'Fecha', dias:int, fechaDevolucion:'Fecha'):
        if isinstance(libro, Libro):
            self.__libro = libro
        else:
            raise TypeError("El valor ingresado por parametro debe ser un objeto de tipo Libro")
        self.__socio = socio
        self.__fechaPrestamo = fechaPrestamo
        self.__dias = dias
        self.__fechaDevolucion = fechaDevolucion
    
    def establecerFechaDevolucion(self, fechaDev: 'Fecha'):
        pass
    def obtenerLibro(self)->'Libro':
        pass
    
    def obtenerFechaPrestamo(self)->'Fecha':
        pass
    
    def obtenerFechaDevolucion(self)->'Fecha':
        pass
    
    def estaAtrasado(fecha: 'Fecha')->bool:
        pass
    
    def penalizacion(self)->Fecha:
        pass
    
    def __str__(self):
        pass