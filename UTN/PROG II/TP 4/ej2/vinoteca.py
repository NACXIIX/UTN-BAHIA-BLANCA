class Vinoteca:
    """ Si la cantidad en deposito
        No es suficiente se vende lo que se puede.
        
        Cada vez que se repone un producto se llena en su capacidad maxima.
    """
    #ATRIBUTO DE CLASE
    __CAPACIDAD_MAXIMA:int = 5000

    #ATRIBUTOS DE INSTANCIA
    def __init__(self, cantJugos:int = __CAPACIDAD_MAXIMA, cantBlancos:int = __CAPACIDAD_MAXIMA, cantTintosJovenes:int = __CAPACIDAD_MAXIMA, cantTintosAnejados:int = __CAPACIDAD_MAXIMA):
        if cantJugos == 5000 and isinstance(cantJugos, int):
            self.__cantJugos = cantJugos
        else:
            raise TypeError("No se debe ingresar valores")
        
        if cantBlancos == 5000 and isinstance(cantBlancos, int):
            self.__cantBlancos = cantBlancos
        else:
            raise TypeError("No se deben ingresar valores")
        
        if cantTintosJovenes == 5000 and isinstance(cantTintosJovenes, int):
            self.__cantTintosJovenes = cantTintosJovenes
        else:
            raise TypeError("No se deben ingresar valores")
        
        if cantTintosAnejados == 5000 and isinstance(cantTintosAnejados, int):
            self.__cantTintosAnejados = cantTintosAnejados
        else:
            raise TypeError("No se deben ingresar valores")

    # COMANDOS
    def reponerJugos(self):
        diferencia = self.__CAPACIDAD_MAXIMA - self.__cantJugos
        if self.__cantJugos != self.__CAPACIDAD_MAXIMA:
            self.__cantJugos += diferencia
        
    def reponerVinosBlancos(self):
        diferencia = self.__CAPACIDAD_MAXIMA - self.__cantBlancos
        if self.__cantBlancos != self.__CAPACIDAD_MAXIMA:
            self.__cantBlancos += diferencia

    def reponerVinosTintoJoven(self):
        diferencia = self.__CAPACIDAD_MAXIMA - self.__cantTintosJovenes
        if self.__cantTintosJovenes != self.__CAPACIDAD_MAXIMA:
            self.__cantTintosJovenes += diferencia

    def reponerVinosTintoAnejado(self):
        diferencia = self.__CAPACIDAD_MAXIMA - self.__cantTintosAnejados
        if self.__cantTintosAnejados != self.__CAPACIDAD_MAXIMA:
            self.__cantTintosAnejados += diferencia

    def venderJugos(self, unidades: int):
        if isinstance(unidades, int):
            puede_vender = False
            
            if self.__CAPACIDAD_MAXIMA >= unidades:
                self.__cantJugos -= unidades
                puede_vender = True
            if self.__CAPACIDAD_MAXIMA < unidades:
                self.__cantJugos -= self.__CAPACIDAD_MAXIMA
                puede_vender = False
                
            return puede_vender
        else:
            raise TypeError("El valor ingresado debe ser un numero entero.")
            
    def venderVinosBLancos(self, unidades:int):
        if isinstance(unidades, int):
            puede_vender = False
            
            if self.__CAPACIDAD_MAXIMA >= unidades:
                self.__cantBlancos -= unidades
                puede_vender = True
            if self.__CAPACIDAD_MAXIMA < unidades:
                self.__cantBlancos -= self.__CAPACIDAD_MAXIMA
                puede_vender = False
                
            return puede_vender
        else:
            raise TypeError("El valor ingresado debe ser un numero entero.")
        
    def venderVinosTintosJovenes(self, unidades:int):
        if isinstance (unidades, int):
            puede_vender = False
            
            if self.__CAPACIDAD_MAXIMA >= unidades:
                self.__cantTintosJovenes -= unidades
                puede_vender = True
            if self.__CAPACIDAD_MAXIMA < unidades:
                self.__cantTintosJovenes -= self.__CAPACIDAD_MAXIMA
                puede_vender = False
                
            return puede_vender
        else:
            raise TypeError("El valor ingresado debe ser un numero entero.")
        
    def venderVinosTintosAnejados(self, unidades:int):
        if isinstance (unidades, int):
            puede_vender = False
            
            if self.__CAPACIDAD_MAXIMA >= unidades:
                self.__cantTintosAnejados-= unidades
                puede_vender = True
            if self.__CAPACIDAD_MAXIMA < unidades:
                self.__cantTintosAnejados -= self.__CAPACIDAD_MAXIMA
                puede_vender = False
                
            return puede_vender
        else:
            raise TypeError("El valor ingresado debe ser un numero entero.")

    # CONSULTAS
    def obtenerCantidadJugos(self)->int:
        return int(f'{self.__cantJugos}')

    def obtenerCantidadVinosBlancos(self)->int:
        return int(f'{self.__cantBlancos}')

    def obtenerCantidadVinosTintosJovenes(self)->int:
        return int(f'{self.__cantTintosJovenes}')

    def obtenerCantidadVinosTintosAnejados(self)->int:
        return int(f'{self.__cantTintosAnejados}')
