class MascotaVirtual:
    __MAX_VALOR = 100
    __MIN_VALOR = 0

    def __init__(self, nombre:str, energia:int =__MAX_VALOR, diversion:int =__MAX_VALOR, higiene:int =__MAX_VALOR, dormido:bool = False, cantActividadesDesgaste:int = 3):
        if isinstance (nombre, str):
            self.__nombre = nombre
        else:
            raise TypeError("El nombre de la mascota debe ser un string")
        if isinstance(energia, (int,float,str)):
            raise TypeError("No se deben ingresar valores, solo se permite ingresar el nombre de la mascota.")
        else:
            self.__energia = energia
        if isinstance(diversion, (int, float, str)):
            raise TypeError("No se deben ingresar valores, solo se permite ingresar el nombre de la mascota.")
        else:
            self.__diversion = diversion
        if isinstance(higiene, (int, float, str)):
            raise TypeError("No se deben ingresar valores, solo se permite ingresar el nombre de la mascota.")
        else:
            self.__higiene = higiene
        if isinstance(dormido, (int,float,str,bool)):
            raise TypeError("No se deben ingresar valores, solo se permite ingresar el nombre de la mascota.")
        else:
            self.__dormido = dormido
        if isinstance (cantActividadesDesgaste, (int,float,str)):
            raise TypeError("No se deben ingresar valores, solo se permite ingresar el nombre de la mascota.")
        else:
            self.__cantActividadesDesgaste = cantActividadesDesgaste


mascota = MascotaVirtual("Panda")