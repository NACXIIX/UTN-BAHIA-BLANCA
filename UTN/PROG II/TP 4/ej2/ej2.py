class Vinoteca:
    """ Si la cantidad en deposito
        No es suficiente se vende lo que se puede.
        
        Cada vez que se repone un producto se llena en su capacidad maxima.
    """
    __CAPACIDAD_MAXIMA:int = 0

    def __init__(self, cantJugos:int = 5000, cantBlancos:int = 5000, cantTintosJovenes:int = 5000, cantTintosAnejados:int = 5000, vinoteca =""):
        self.__cantJugos = cantJugos
        self.__cantBlancos = cantBlancos
        self.__cantTintosJovenes = cantTintosJovenes
        self.__cantTintosAnejados = cantTintosAnejados
        self.vinoteca = vinoteca

    # COMANDOS
    def reponerJugos(self):
        reponer = int(input("Cantidad jugos a reponer: "))
        Vinoteca.__CAPACIDAD_MAXIMA += reponer
        
    def reponerVinosBlancos(self):
        reponer = int(input("Cantidad vinos blancos a reponer: "))
        Vinoteca.__CAPACIDAD_MAXIMA += reponer

    def reponerVinosTintoJoven(self):
        reponer = int(input("Cantidad vinos tinto joven a reponer: "))
        Vinoteca.__CAPACIDAD_MAXIMA += reponer

    def reponerVinosTintoAnejado(self):
        reponer = int(input("Cantidad vinos anejados a reponer: "))
        Vinoteca.__CAPACIDAD_MAXIMA += reponer

    def venderJugos(self, unidades: int):
        Vinoteca.__CAPACIDAD_MAXIMA -= unidades

    def venderVinosBLancos(self, unidades:int):
        Vinoteca.__CAPACIDAD_MAXIMA -= unidades

    def venderVinosTintosJovenes(self, unidades:int):
        Vinoteca.__CAPACIDAD_MAXIMA -= unidades

    def venderVinosTintosAnejados(self, unidades:int):
        __CAPACIDAD_MAXIMA -= unidades

    # CONSULTAS
    def obtenerCantidadJugos(self)->int:
        return self.__cantJugos

    def obtenerCantidadVinosBlancos(self)->int:
        return self.__cantBlancos

    def obtenerCantidadVinosTintosJovenes(self)->int:
        return self.__cantTintosJovenes

    def obtenerCantidadVinosTintosAnejados(self)->int:
        return self.__cantTintosAnejados


vinoteca_1 = Vinoteca()
vinoteca_2 = Vinoteca()
print (vinoteca_1.obtenerCantidadJugos())
print (vinoteca_2.obtenerCantidadJugos())
