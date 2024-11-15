from datetime import date

class Prestamo:
    __ultimoId:int = 0

    @classmethod
    def fromDiccionario(cls, dic:dict)->'Prestamo':
        if isinstance (dic, dict):
            if 'id' not in dic:
                raise ValueError("El json debe tener la clave id")
            if 'socio_dni' not in dic:
                raise ValueError("El json debe tener la clave socio_dni")
            if 'libro_isbn' not in dic:
                raise ValueError("El json debe tener la clave libro_isbn")
            if 'fecha_retiro' not in dic:
                raise ValueError("El json debe tener la clave fecha_retiro")
            if 'cant_dias' not in dic:
                raise ValueError("El json debe tener la clave cant_dias")
            if 'fecha_devolucion' not in dic:
                raise ValueError("El json debe tener la clave fecha_devolucion")
            return Prestamo(dic["id"], dic["socio_dni"], dic["libro_isbn"], dic["fecha_retiro"], dic["cant_dias"], dic["fecha_devolucion"])
        else:
            raise TypeError("El valor ingresado por parametro en dic debe ser de tipo diccionario.")
        
    def __init__(self, id:int, socio_dni:int, libro_isbn:int, fecha_retiro: date, cant_dias:int, fecha_devolucion:date):
        if not isinstance(id, int) and not id > 0:
            raise TypeError("El valor ingresado por parametro en id debe ser un numero entero positivo")
        if not isinstance(socio_dni, int) and not socio_dni > 0:
            raise TypeError("El valor ingresado por parametro en socio_dni debe ser un numero entero positivo")
        if not isinstance(libro_isbn, int) and not libro_isbn > 0:
            raise TypeError("El valor ingresado por parametro en libro_isbn debe ser un numero entero positivo")
        if not isinstance(fecha_retiro, date):
            raise TypeError("El valor ingresado por parametro en fecha_retiro debe ser de tipo date")
        if not isinstance(cant_dias, int) and not cant_dias > 0:
            raise TypeError("El valor ingresado por parametro en cant_dias debe ser un numero entero positivo")
        if not isinstance(fecha_devolucion, date):
            raise TypeError("El valor ingresado por parametro en fecha_devolucion debe ser de tipo date")
        
        self.__id = id
        self.__socio_dni = socio_dni
        self.__libro_isbn = libro_isbn
        self.__fecha_retiro = fecha_retiro
        self.__cant_dias = cant_dias
        self.__fecha_devolucion = fecha_devolucion
        Prestamo.establecerUltimoId(Prestamo.obtenerNuevoId())
        
    @classmethod
    def obtenerNuevoId(cls)->int:
        """_summary_

        Args:
            id (int): Se utiliza para obtener un ID unico para cada nueva instancia.
            Incrementa el atributo de clase ultimoID y lo retorna
        """
        
        cls.__ultimoId += 1
        return cls.__ultimoId
    
    #Falta agregar que cuando no se encuentra el archivo de dato tire una excepcion
    @classmethod
    def establecerUltimoId(cls, id:int):

        cls.__ultimoId = id

    def establecerSocioDNI(self, dni:int):
        self.__dni = dni
    
    def establecerLibroISBN(self, isbn:int):
        self.__libro_isbn = isbn
    
    def establecerFechaRetiro(self, fecha: date):
        self.__fecha_retiro = fecha
    
    def establecerCantDias(self, cant:int):
        self.__cant_dias = cant
    
    def establecerFechaDevolucion(self, fecha:date):
        self.__fecha_devolucion = fecha
    
    def obtenerSocioDNI(self)->int:
        return self.__socio_dni
    
    def obtenerISBN(self)->int:
        return self.__libro_isbn
    
    def obtenerFechaRetiro(self)->date:
        return self.__fecha_retiro
    
    def obtenerCantDias(self)->int:
        return self.__cant_dias
    
    def obtenerFechaDevolucion(self)->date:
        return self.__fecha_devolucion
    
    def esIgual(self, otro:'Prestamo')->bool:
        if isinstance(otro, Prestamo):
            return self.__socio_dni == otro.obtenerSocioDNI() and self.__libro_isbn == otro.obtenerISBN() and self.__fecha_retiro == otro.obtenerFechaRetiro and self.__cant_dias == otro.obtenerCantDias() and self.__fecha_devolucion == otro.obtenerFechaDevolucion
        else:
            raise TypeError("El valor ingresado por parametro debe ser un objeto de tipo Prestamo.")
    
    def __str__(self)->str:
        return f"ID: {self.__id} - Socio_DNI: {self.__socio_dni} - Libro ISBN: {self.__libro_isbn} - Fecha de retiro: {self.__fecha_retiro} - Cantidad de dias: {self.__cant_dias} - Fecha de devolucion: {self.__fecha_devolucion}"
    
    def toDiccionario(self)->dict:
        dic = {
            "id": {self.__id},
            "socio_dni": {self.__socio_dni},
            "libro_isbn": {self.__libro_isbn},
            "fecha_retiro": {self.__fecha_retiro},
            "cant_dias": {self.__cant_dias},
            "fecha_devolucion": {self.__fecha_devolucion}
        }