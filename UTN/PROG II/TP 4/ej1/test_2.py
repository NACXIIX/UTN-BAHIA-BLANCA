from empleado import Empleado

class testEmpleado:

    @staticmethod
    def test():
        legajo = int(input("Legajo: "))
        horas_trabajadas_mes = int(input("Horas trabajadas mes:"))
        valor_hora = int(input("Valor hora:"))
        empleado_1 = Empleado(legajo, horas_trabajadas_mes,valor_hora)
        print(empleado_1)

        empleado_1.establecerHorasTrabajadas(34)
        empleado_1.establecerValorHora(5000)
        print(empleado_1)

if __name__ == '__main__':
    testEmpleado.test()