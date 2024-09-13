class Automovil:
    # ATRIBUTOS DE INSTANCIA
    def __init__(self, marca:str, modelo:str, anio:int, velocidadMaxima:float, velocidadActual:float):
        if isinstance(marca, (str)):
            self.__marca = marca
        else:
            raise TypeError("La marca del auto debe ser un string.")
        if isinstance(modelo, str):
            self.__modelo = modelo
        else:
            raise TypeError("El modelo del auto debe ser un string.")
        if isinstance(anio, int) and anio > 0: 
            self.__anio = anio
        else:
            raise TypeError("El anio del auto debe ser un numero entero positivo.")
        if isinstance(velocidadMaxima, (int,float)) and velocidadMaxima >= 0:
            self.__velocidadMaxima = velocidadMaxima
        else:
            raise TypeError("La velocidad maxima del auto debe ser un numero positivo.")
        if isinstance(velocidadActual, (int, float)):
            self.__velocidadActual = velocidadActual
        else:
            raise TypeError("La velocidad actual del auto debe ser un numero positivo.")

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
                print ("Se esta intentando acelerar a una velocidad maxima permitida por el auto. La velocidad se ajustó a la velocidad maxima del auto. ")
                return False 
            puede_acelerar = True
        else:
            self.__velocidadActual = self.__velocidadActual - (self.__velocidadActual - self.__velocidadMaxima)
            puede_acelerar = False

        return puede_acelerar

    def desacelerar(self, decrementoVelocidad:int):
        puede_desacelerar: False

        if self.__velocidadActual > 0:
            self.__velocidadActual -= decrementoVelocidad
            if self.__velocidadActual < 0:
                self.__velocidadActual = 0
                print ("Se esta intentando desacelerar por de mas. ")
                return False
            puede_desacelerar = True
        else:
            self.__velocidadActual = 0
            puede_desacelerar = False
        
        return puede_desacelerar

    def frenarPorCompleto(self):
        auto_detenido = False
        if self.__velocidadActual == 0:
            auto_detenido = True
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
        return float(f'{self.__velocidadActual}')

    def calcularMinutosParaLlegar(self, distanciaKM:float)-> int:
        if self.__velocidadActual > 0 :
            minutos_para_llegar = (distanciaKM // self.obtenerVelocidadActual()) * 60
            return int(minutos_para_llegar)
        else:
            print ("El auto se encuentra detenido y no se puede calcular el tiempo para llegar")
