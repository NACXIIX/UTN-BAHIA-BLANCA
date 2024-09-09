from empleado import Empleado

class testEmpleadoParametros:
    @staticmethod
    def test():
        empleado_1 = Empleado(1, 20.8, 3000)
        empleado_2 = Empleado(110)
        print(empleado_1)
        print(empleado_2)

if __name__ == '__main__':
    testEmpleadoParametros.test()