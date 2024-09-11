from empleado import Empleado

class testEmpleado:

    @staticmethod
    def test():
        legajo = int(input("Legajo: "))
        horas_trabajadas_mes = int(input("Horas trabajadas mes:"))
        valor_hora = int(input("Valor hora:"))
        
        empleado_1 = Empleado(legajo, horas_trabajadas_mes,valor_hora)
        print(empleado_1) 

        if legajo == empleado_1.obtenerLegajo():
            print ("El legajo fue guardado correctamente.")
        else:
            print ("El Legajo ingresado no se guardaron correctamente.")
        if horas_trabajadas_mes == empleado_1.obtenerHorasTrabajadas():
            print ("Las horas trabajadas fueron guardadas correctamente")
        else:
            print ("Las horas trabajadas no se guardaron correctamente.")
        if valor_hora == empleado_1.obtenerValorHora():
            print ("El valor hora fue guardado correctamente.")
        else:
            print ("El valor hora no se guardo correctamente.")

if __name__ == '__main__':
    testEmpleado.test()