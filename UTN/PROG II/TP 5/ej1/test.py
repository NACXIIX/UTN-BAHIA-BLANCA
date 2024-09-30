from atleta import Atleta

class TestAtleta:
    
    @staticmethod
    def test():
        atleta_1 = Atleta("Blat")
        atleta_2 = Atleta("Panda")

        atleta_1.entrenar()
        atleta_1.entrenar()
        atleta_1.entrenar()
        atleta_1.entrenar()
        atleta_1.entrenar()
        print (atleta_1)
        print (f"El atleta {atleta_1.obtenerNombre()} tiene {atleta_1.obtenerDestreza()} de destreza")
        
        atleta_2.entrenar()
        print (atleta_2)
        print (f"El atleta {atleta_2.obtenerNombre()} tiene {atleta_2.obtenerDestreza()} de destreza")

        print ("")
        
        if atleta_1.mayorDestrezaQue(atleta_2):
            print (f"El atleta {atleta_1.obtenerNombre()} tiene mas destreza que el atleta {atleta_2.obtenerNombre()} ")
        else:
            print (f"El atleta {atleta_2.obtenerNombre()} tiene mas destreza que el atleta {atleta_1.obtenerNombre()} ")

        if atleta_1.mismaDestrezaQue(atleta_2):
            print (f"El atleta {atleta_1.obtenerNombre()} tiene la misma destreza que el atleta {atleta_2.obtenerNombre()} ")
        else:
            print (f"El atleta {atleta_1.obtenerNombre()} no tiene tiene mas destreza que el atleta {atleta_2.obtenerNombre()} ")

if __name__ == '__main__':
    TestAtleta.test()