class Atleta:
    __MAX_VALOR:int = 100
    __MIN_VALOR:int = 1
    __CONTADOR_ENTRENAMIENTOS = 0
    
    def __init__(self, atleta:str):
        if isinstance(atleta, str):
            self.__atleta = atleta
        else:
            raise TypeError("El nombre del atleta debe ser un string.")
        
        self.__energia = self.__MAX_VALOR
        self.__destreza = self.__MIN_VALOR
    
    def entrenar(self):
        self.__energia -= 5
        self.contadorEntrenamientos(1)
        
    def descansar(self):
        self.__energia + 20
    
    def obtenerDestreza(self):
        return self.__destreza
    
    def obtenerEnergia(self):
        return self.__energia
    
    def obtenerNombre(self):
        return self.__atleta
    
    def mismaDestrezaQue(self, otroAtleta: 'Atleta')-> bool:
        if isinstance(otroAtleta, (object,str)):
            return self.obtenerDestreza == otroAtleta.obtenerDestreza()
        else:
            raise TypeError("El nombre ingresado por parametro debe ser un string.")
        
    def mayorDestrezaQue(self, otroAtleta: 'Atleta')-> bool:
        if isinstance(otroAtleta, (object,str)):
            self_destreza_es_mayor = False
        
            if self.__destreza > otroAtleta.obtenerDestreza():
                self_destreza_es_mayor = True
            else:
                self_destreza_es_mayor = False
                
            return self_destreza_es_mayor
        else:
            raise TypeError("El nombre ingresado por parametro debe ser un string.")
    
    def contadorEntrenamientos(self, entrenamiento:int):
        self.__CONTADOR_ENTRENAMIENTOS += entrenamiento
        if self.__CONTADOR_ENTRENAMIENTOS == 5:
            self.__destreza += 1 
            self.__CONTADOR_ENTRENAMIENTOS = 0
    
    def __str__(self):
        return f" - Nombre: {self.__atleta} - Energia: {self.__energia} - Destreza: {self.__destreza}\n"

