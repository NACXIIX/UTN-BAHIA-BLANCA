class Empleado:
    
    #INSTANCIA DE CLASE CONSTRUCTORES
    def __init__(self, legajo:int, horasTrabajadasMes: int = 0, valorHora: float = 0):
        self.__legajo = legajo
        self.__horasTrabajadasMes = horasTrabajadasMes
        self.__valorHora = valorHora
        if self.__legajo < 0:
            raise ValueError("El numero debe ser mayor a 0")
        if not isinstance(self.__horasTrabajadasMes, int):
            raise TypeError("El valor debe ser un numero entero")
        
    def establecerHorasTrabajadas(self, cantHoras:int):
        self.__horasTrabajadasMes = cantHoras

    def establecerValorHora(self, valorHora: float):
        self.__valorHora = valorHora
    
    def obtenerLegajo(self)->int:
        return f'{self.__legajo}'

    def obtenerHorasTrabajadas(self)->int:
        return f'{self.__horasTrabajadasMes}'

    def obtenerValorHora(self)->float:
        return f'{self.__valorHora}'
    
    def obtenerSueldo(self)->float:
        return float(self.__horasTrabajadasMes * self.__valorHora)
    
    def __str__(self):
        return f'Legajo: {self.__legajo} -- Sueldo calculado: ${self.obtenerSueldo()} '