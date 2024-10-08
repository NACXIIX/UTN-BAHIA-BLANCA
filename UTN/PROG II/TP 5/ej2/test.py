from fecha import Fecha

class TestFecha:
    @staticmethod
    def test():
        fecha_1 = Fecha(31,10,2000)
        fecha_2 = Fecha(14,10,2000)
        print (f"Fecha 1: {fecha_1}")
        print (f"Fecha 2: {fecha_2}")

        if fecha_1.esAnterior(fecha_2):
            print("fecha 1 es anterior a fecha 2")
        elif not fecha_1.esAnterior(fecha_2):
            print("fecha 1 no es anterior a fecha 2")

        if fecha_2.esIgualQue(fecha_1):
            print("Fecha 2 es equivalente a Fecha 1")
        else:
            print("Fecha 2 no es equivalente a Fecha 1")


        fecha_3 = fecha_1.diaSiguiente()
        print(f"Fecha 3, con un dia mas que la Fecha 1: {fecha_3}")

        fecha_4 = Fecha(12,12,2024)
        fecha_5 = Fecha(12,12,2024)
        print (f"Fecha 4: {fecha_4}")
        print (f"Fecha 5: {fecha_5}")

        if fecha_4.esIgualQue(fecha_5):
            print("Fecha 4 es equivalente a Fecha 5")
        else:
            print("Fecha 4 no es equivalente a Fecha 5")

if __name__ == '__main__':
    TestFecha.test()