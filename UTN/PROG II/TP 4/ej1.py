class Empleado:
    def __init__(self,legajo: int, horasTrabajadasMes: int, valorHora: float):
        self.__legajo = legajo
        self.__horasTrabajadasMes = horasTrabajadasMes
        self.__valorHora = valorHora
        
    def establecerHorasTrabajadas(self,cantHoras:int):
        self.__horasTrabajadasMes = cantHoras
    
    def establecerValorHora(self, valorHora:float):
        self.__valorHora = valorHora
    
    def obtenerLegajo(self)-> int:
        return print(f"{int(self.__legajo)}")
    
    def obtenerHorasTrabajadas(self)-> int:
        return print(f"{int(self.__horasTrabajadasMes)}")
    
    def obtenerValorHora(self)-> float: 
        return print(f"{float(self.__valorHora)}")

    def obtenerSueldo(self)-> float:
        sueldo = self.__horasTrabajadasMes * self.__valorHora
        return print(float(sueldo))


empleado_1 = Empleado(3352, 24, 1000)

empleado_1.obtenerLegajo()
empleado_1.obtenerHorasTrabajadas()
empleado_1.obtenerValorHora()
empleado_1.obtenerSueldo()
