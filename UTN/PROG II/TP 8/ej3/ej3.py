import json

class Ciudad:
    pass
class PaqueteGrupal:

    def __init__(self, ciudad:'Ciudad', fechaIda:str, fechaVuelta:str, descripcionViaje:str, tipoViaje:str, precio:float, cupoMaximo: int, cupoMinimo:int, ID:int):
        if not isinstance(ciudad, Ciudad):
            raise TypeError("El valor ingresado por parametro en ciudad debe ser un objeto de tipo Ciudad")
        if not isinstance(fechaIda, str):
            raise TypeError("El valor ingresado por parametro en fechaIda debe ser un string")
        if not isinstance(fechaVuelta, str):
            raise TypeError("El valor ingresado por parametro en fechaVuelta debe ser un string")
        if not isinstance(descripcionViaje, str):
            raise TypeError("El valor ingresado por parametro en descripcionViaje debe ser un string")
        if not isinstance(tipoViaje, str):
            raise TypeError("El valor ingresado por parametro en tipoViaje debe ser un string")
        if not isinstance(precio, (int, float)) and precio < 0:
            raise TypeError("El valor ingresado por parametro en precio debe ser un numero positivo.")
        if not isinstance(cupoMaximo, int) and cupoMaximo < 0:
            raise TypeError("El valor ingresado por parametro en cupoMaximo debe ser un numero entero positivo.")
        if not isinstance(cupoMinimo, int) and cupoMinimo < 0:
            raise TypeError("El valor ingresado por parametro en cupoMinimo debe ser un numero entero positivo.")
        if not isinstance(ID, int) and ID < 0:
            raise TypeError("El valor ingresado por parametro en ID debe ser un numero entero positivo.")
        
        self.__ciudad = ciudad
        self.__fechaIda = fechaIda
        self.__fechaVuelta = fechaVuelta
        self.__descripcionViaje = descripcionViaje
        self.__tipoViaje = tipoViaje
        self.__precio = precio
        self.__cupoMaximo = cupoMaximo
        self.__cupoMinimo = cupoMinimo
        self.__ID = ID
        