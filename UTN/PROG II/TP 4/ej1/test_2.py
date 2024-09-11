from empleado import Empleado

class testEmpleadoParametros:
    
    @staticmethod
    def test():
        empleado_1 = Empleado(1, 20, 3000.0)
        empleado_2 = Empleado(110)
        print(empleado_1)
        print(empleado_2)
        print (f"El legajo del empleado 1 es: {empleado_1.obtenerLegajo()}") # legajo = 1
        print (f"El legajo del empleado 2 es: {empleado_2.obtenerLegajo()}") # legajo = 110
        print("\n")

        if empleado_2.establecerHorasTrabajadas(35): # hs trabajadas = 35
            print ("Las horas trabajadas se establecieron correctamente")
        else:
            print ("Las horas trabajadas deben ser un numero entero positivo mayor o igual a 0.")
        if empleado_2.establecerHorasTrabajadas(-35): # hs trabajadas = -35, deberia aparecer error
            print ("Las horas trabajadas se establecieron correctamente")
        else:
            print ("Las horas trabajadas deben ser un numero entero positivo mayor o igual a 0.")
        
        if empleado_2.establecerValorHora(4000.0): #valor hora = 4000.5
            print ("El valor hora se establecio correctamente.")
        else: 
            print ("El valor hora debe ser un numero flotante mayor a 0.")
        if empleado_2.establecerValorHora(-4000.0): #valor hora = -4000.5, deberia aparecer un error
            print ("El valor hora se establecio correctamente.")
        else: 
            print ("El valor hora debe ser un numero flotante mayor a 0.")
            
        print("\n")
        print(empleado_1)
        print(empleado_2)

        print(f"\nDatos del empleado 2\n\tLegajo: {empleado_2.obtenerLegajo()}\n\tHoras trabajadas: {empleado_2.obtenerHorasTrabajadas()} \n\tValor Hora: {empleado_2.obtenerValorHora()} \n\tSueldo: {empleado_2.obtenerSueldo()}")  # Mostrar datos del empleado luego de aplicar los metodos del objeto empleado_2

if __name__ == '__main__':
    testEmpleadoParametros.test()