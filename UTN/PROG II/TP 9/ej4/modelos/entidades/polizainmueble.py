from abc import ABC

class PolizaInmueble(ABC):
    @classmethod
    def fromDiccionario(cls, dic:dict):
        if isinstance(dic, dict):
            return cls(dic["numero"], dic["incendio"], dic["explosion"], dic["robo"])
        else:
            raise ValueError("El valor ingresado por parametro debe ser un diccionario.")
        
    def __init__(self, numero:int, incendio:float, explosion: float, robo:float):


        if not isinstance(numero, int):
            raise TypeError("El valor ingresado por parametro en numero debe ser un numero entero")
        if not isinstance(incendio, (float, int)):
            raise TypeError("El valor ingresado por parametro en incendio debe ser un numero positivo")
        if not isinstance(explosion, (float, int)):
            raise TypeError("El valor ingresado por parametro en explosion debe ser un numero positivo")
        if not isinstance(robo, (float, int)):
            raise TypeError("El valor ingresado por parametro en robo debe ser un numero positivo")
        
        self._numero = numero
        self._incendio = incendio
        self._explosion = explosion
        self._robo = robo

