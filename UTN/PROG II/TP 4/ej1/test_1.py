from empleado import Empleado

class testEmpleadoParametros:
    @staticmethod
    def test():
        empleado_1 = Empleado(1, 20, 3000)
        empleado_2 = Empleado(110)
        print(empleado_1)
        print(empleado_2)
        print (f"El legajo del empleado 1 es: {empleado_1.obtenerLegajo()}")
        print (f"El legajo del empleado 2 es: {empleado_2.obtenerLegajo()}")

        empleado_2.establecerHorasTrabajadas(35)
        empleado_2.establecerValorHora(4000)
        print(empleado_1)
        print(empleado_2)

        print(f"\nDatos del empleado 2\n\tLegajo: {empleado_2.obtenerLegajo()}\n\tHoras trabajadas: {empleado_2.obtenerHorasTrabajadas()} \n\tSueldo: {empleado_2.obtenerSueldo()} \n\tValor Hora: {empleado_2.obtenerValorHora()}") 

if __name__ == '__main__':
    testEmpleadoParametros.test()