from fecha import Fecha

class TestFecha:
    @staticmethod
    def test():
        fecha_1 = Fecha(14,10,2000)
        fecha_2 = Fecha(14,10,2000)

        if fecha_1.esAnterior(fecha_2):
            print("fecha 1 es anterior a fecha 2")
        elif not fecha_1.esAnterior(fecha_2):
            print("fecha 2 es anterior a fecha 1")
            
        fecha_3 = fecha_1.diaSiguiente()
        print(fecha_3)
        fecha_3 = fecha_1.diaSiguiente()
        print(fecha_3)
        fecha_3 = fecha_1.diaSiguiente()
        print(fecha_3)
        print(fecha_1)

if __name__ == '__main__':
    TestFecha.test()