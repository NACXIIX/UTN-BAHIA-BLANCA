from datetime import date
from modelos.entidades.libro import Libro
from modelos.entidades.prestamo import Prestamo
from modelos.entidades.socio import Socio
import json
class RepositorioPrestamos:
    FILE_PATH = "datos/prestamos.json"
    
    def __init__(self):
        self.__prestamos = self.__cargarTodos()
        
    def __cargarTodos(self):
        lista = []
        try:
            with open (RepositorioPrestamos.FILE_PATH, "r") as file:
                prestamos = json.load(file)
                for prestamo in prestamos:
                    lista.append(Prestamo.fromDiccionario(prestamo))
        except:
            ValueError("No se encontro el archivo json")
            
        return lista
    
    def __guardarTodos(self):
        try:
            lista = []
            for prestamo in self.__prestamos:
                lista.append(prestamo.toDiccionario())
            
            with open(RepositorioPrestamos.FILE_PATH, "w", encoding= "utf-8") as file:
                json.dump(lista,file, indent=4)

        except: FileNotFoundError("No se encontro el archivo json.")
    
    def obtenerTodos(self)->list[Prestamo]:
        return self.__prestamos
    
    def estaDevuelto(self, prestamo:'Prestamo')->bool:
        if prestamo.obtenerFechaDevolucion() is None:
            return False
        return True
    
    def agregar(self, nuevoPrestamo:'Prestamo'):
        if not isinstance(nuevoPrestamo, Prestamo):
            raise TypeError("El valor ingresado por parametro en nuevoPrestamo debe ser un objeto de tipo Prestamo.")
        if self.existe(nuevoPrestamo.obtenerSocioDNI(), nuevoPrestamo.obtenerISBN(), nuevoPrestamo.obtenerFechaRetiro()):
            self.__prestamos.append(nuevoPrestamo)
            self.__guardarTodos()

    def existe(self, socio_dni:int, libro_isbn:int, fecha_retiro: date)->bool:
        if not isinstance (socio_dni, int) and len(str(socio_dni)) != 11:
            raise TypeError("El valor ingresado por parametro en socio_dni debe ser un numero entero positivo de 11 digitos.")
        if not isinstance (libro_isbn, int) and isbn < 0:
            raise TypeError("El valor ingresado por parametro en libro_isbn debe ser un numero entero positivo")
        if not isinstance (fecha_retiro, date):
            raise TypeError("El valor ingresado por parametro en fecha_retiro debe ser una fecha")
        
        for prestamo in self.__prestamos:
            if prestamo.obtenerSocioDNI() == socio_dni and prestamo.obtenerISBN() == libro_isbn and prestamo.obtenerFechaRetiro() == fecha_retiro:
                return True
        return False
        
    def obtenerPrestamo(self, socio_dni:int, libro_isbn:int, fecha_retiro:date)->'Prestamo':
        for prestamo in self.__prestamos:
            if prestamo.obtenerSocioDNI() == socio_dni and prestamo.obtenerISBN() == libro_isbn and prestamo.obtenerFechaRetiro() == fecha_retiro:
                return prestamo
        return None

    def modificarPorID(self, id:int, socio_dni:int, libro_isbn:int, fecha_retiro:date, cant_dias:int, fecha_devolucion:date):
        for prestamo in self.__prestamos:
            if id == prestamo.obtenerID():
                prestamo.establecerSocioDNI(socio_dni)
                prestamo.establecerISBN(libro_isbn)
                prestamo.establecerFechaRetiro(fecha_retiro)
                prestamo.establecerCantDias(cant_dias)
                prestamo.establecerFechaDevolucion(fecha_devolucion)
                self.__guardarTodos()
                return True
        return False
    
    def eliminarPorID(self, id:int):
        for prestamo in self.__prestamos:
            if prestamo.obtenerID() == id:
                self.__prestamos.remove(prestamo)
                self.__guardarTodos()
                return True
        return False
    
    def cantidadLibrosSinDevolver(self, isbn:int)->int:
        cantidad = 0
        for prestamo in self.__prestamos:
            if prestamo.obtenerISBN() == isbn:
                if not self.estaDevuelto(prestamo):
                    cantidad += 1
        return cantidad