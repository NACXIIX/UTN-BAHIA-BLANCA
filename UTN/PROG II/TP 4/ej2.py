class Vinoteca:
    __CAPACIDAD_MAXIMA = 0

    def __ini__(self, cantJugos: int, cantBlancos: int, cantTintosJovenes: int, cantTintosAnejados: int, vinoteca):
        self.__cantJugos = cantJugos
        self.__cantBlancos = cantBlancos
        self.__cantTintosJovenes = cantTintosJovenes
        self.__cantTintosAnejados = cantTintosAnejados
        self.__vinoteca = vinoteca

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
    def venderVinosBLancos(self, unidades: int):
        Vinoteca.__CAPACIDAD_MAXIMA -= unidades
    def venderVinosTintosJovenes(self, unidades: int):
        Vinoteca.__CAPACIDAD_MAXIMA -= unidades
    def venderVinosTintosAnejados(self, unidades: int):
        __CAPACIDAD_MAXIMA -= unidades
    def obtenerCantidadJugos(self)->int:
        return self.__cantJugos
    def obtenerCantidadVinosBlancos(self)->int:
        return self.__cantBlancos
    def obtenerCantidadVinosTintosJovenes(self)->int:
        return self.__cantTintosJovenes
    def obtenerCantidadVinosTintosAnejados(self)->int:
        return self.__cantTintosAnejados
