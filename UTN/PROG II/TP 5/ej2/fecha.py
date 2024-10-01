class Fecha:
    
    def __init__(self, dia:int, mes:int, anio:int):
        if isinstance(dia, int) and 0 < dia <= 31:
            self.__dia = dia
        else:
            raise TypeError("El valor del parametro dia debe ser un numero entero positivo entre 0 y 31 inclusive.")
        
        if isinstance(mes, int) and 0 < mes <= 12:
            self.__mes = mes
        else:
            raise TypeError("El valor del parametro mes debe ser un numero entero positivo entre 0 y 12 inclusive.")
        
        if isinstance(anio, int) and 0 < anio <= 2024:
            self.__anio = anio
        else:
            raise TypeError("El valor del parametro anio debe ser un numero entero positivo entre 0 y 2024 inclusive.")
    
    def establecerDia(self, dia:int):
        if isinstance(dia, int) and 0 < dia <= 31:
            self.__dia = dia
        else:
            raise TypeError("El valor del parametro dia debe ser un numero entero positivo entre 0 y 31 inclusive.")
        
    
    def establecerMes(self, mes:int):
        if isinstance(mes, int) and 0 < mes <= 12:
            self.__mes = mes
        else:
            raise TypeError("El valor del parametro mes debe ser un numero entero positivo entre 0 y 12 inclusive.")
    
    def establecerAnio(self, anio:int):
        if isinstance(anio, int) and 0 < anio <= 2024:
            self.__anio = anio
        else:
            raise TypeError("El valor del parametro anio debe ser un numero entero positivo entre 0 y 2024 inclusive.")
    
    def obtenerDia(self)->int:
        return self.__dia
    
    def obtenerMes(self)->int:
        return self.__mes
    
    def obtenerAnio(self)->int:
        return self.__anio
    
    def esAnterior(self, otraFecha:'Fecha')->bool:
        pass
    
    def sumaDias(self, cantDias:int)->'Fecha':
        pass
    
    def diaSiguiente(self)->'Fecha':
        pass
    
    def esIgualQue(self, otraFecha:'Fecha')->bool:
        pass

fechita = Fecha(12,10,1993)
fechita_2 = Fecha(14,10,2024)