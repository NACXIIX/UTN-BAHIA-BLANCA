class Empleado:
    
    #INSTANCIA DE CLASE CONSTRUCTORES
    def __init__(self, legajo:int, horasTrabajadasMes: int = 0, valorHora: float = 0.0):

        if legajo > 0 and isinstance(legajo, int):
            self.__legajo = legajo
        else:
            raise ValueError("El numero del legajo debe ser un numero entero positivo")
        
        if horasTrabajadasMes >= 0 and isinstance(horasTrabajadasMes, int):
            self.__horasTrabajadasMes = horasTrabajadasMes
        else:
            raise TypeError("Las horas trabajadas deben ser un numero entero positivo mayor o igual a 0")

        if valorHora >= 0 and isinstance(valorHora, (int, float)):
            self.__valorHora = valorHora
        else:
            raise TypeError("El numero valor hora debe ser un numero positivo mayor o igual a 0")
        
    def establecerHorasTrabajadas(self, cantHoras:int):
        horas_trabajadas_is_int = False
        if isinstance(cantHoras, int) and cantHoras >= 0:
            self.__horasTrabajadasMes = cantHoras
            horas_trabajadas_is_int = True
        else:
            horas_trabajadas_is_int = False
        return horas_trabajadas_is_int

    def establecerValorHora(self, valorHora: float):
        valor_hora_is_float = False
        if isinstance(valorHora, float) and valorHora >= 0:
            self.__valorHora = valorHora
            valor_hora_is_float = True
        else:
            valor_hora_is_float = False
        return valor_hora_is_float
    
    def obtenerLegajo(self)->int:
        return int(f'{self.__legajo}')

    def obtenerHorasTrabajadas(self)->int:
        return int(f'{self.__horasTrabajadasMes}')

    def obtenerValorHora(self)->float:
        return float(f'{self.__valorHora}')
    
    def obtenerSueldo(self)->float:
        return float(self.__horasTrabajadasMes * self.__valorHora)
    
    def __str__(self):
        return f'Legajo: {self.__legajo} -- Sueldo calculado: ${self.obtenerSueldo()} '

