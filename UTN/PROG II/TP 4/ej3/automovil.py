class Automovil:
    # ATRIBUTOS DE INSTANCIA
    def __init__(self, marca:str, modelo:str, anio:int, velocidadMaxima:float, velocidadActual:float):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__velocidadMaxima = velocidadMaxima
        self.__velocidadActual = velocidadActual

    # COMANDOS
    def establecerMarca(self, marca:str):
        self.__marca = marca
    
    def establecerModelo(self, modelo:str):
        self.__modelo = modelo

    def establecerAnio(self, anio:int):
        self.__anio = anio
    
    def establecerVelocidadMaxima(self, velocidadMax:float):
        self.__velocidadMaxima = velocidadMax
    
    def establecerVelocidadActual(self, velocidad:float):
        self.__velocidadActual = velocidad

    def acelerar(self, incrementoVelocidad:int):
        puede_acelerar = False
        
        if self.__velocidadActual < self.__velocidadMaxima and self.__velocidadActual < incrementoVelocidad + self.__velocidadActual:
            self.__velocidadActual += incrementoVelocidad
            if self.__velocidadActual > self.__velocidadMaxima:
                self.__velocidadActual = self.__velocidadActual - (self.__velocidadActual - self.__velocidadMaxima)
                return False # Funciona bien pero acelera, hasta la velocidad maxima. Buscar la forma de printear que acelero pero no del todo
            puede_acelerar = True
        else:
            self.__velocidadActual = self.__velocidadActual - (self.__velocidadActual - self.__velocidadMaxima)
            puede_acelerar = False
        return puede_acelerar

    def desacelerar(self, decrementoVelocidad:int):
        puede_desaceler: False

        if self.__velocidadActual > 0:
            self.__velocidadActual -= decrementoVelocidad
            if self.__velocidadActual < 0:
                self.__velocidadActual = 0
                return False #Funciona bien pero si desacelera, hasta 0. buscar la forma de printear que desacelero pero no del todo
            puede_desaceler = True
        else:
            self.__velocidadActual = 0
            puede_desaceler = False
        
        return puede_desaceler

    def frenarPorCompleto(self):
        auto_detenido = False
        if self.__velocidadActual > 0:
            self.__velocidadActual = 0
            auto_detenido = True
        return auto_detenido

    #CONSULTAS
    def obtenerMarca(self):
        return f'{self.__marca}'
    
    def obtenerModelo(self):
        return f'{self.__modelo}'

    def obtenerAnio(self):
        return f'{self.__anio}'

    def obtenerVelocidadMaxima(self):
        return f'{self.__velocidadMaxima}'

    def obtenerVelocidadActual(self):
        return f'{self.__velocidadActual}'

    def calcularMinutosParaLlegar(self, distanciaKM:float)-> int:
        pass
