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

        print (atleta_2)
        print (f"El atleta {atleta_2.obtenerNombre()} tiene {atleta_2.obtenerDestreza()} de destreza")

        print ()

        #Se verifica la asociacion entre el atleta 1 y el atleta 2
        if atleta_1.mayorDestrezaQue(atleta_2):
            print (f"El atleta {atleta_1.obtenerNombre()} tiene mas destreza que el atleta {atleta_2.obtenerNombre()} ")
        else:
            print (f"El atleta {atleta_2.obtenerNombre()} tiene mas destreza que el atleta {atleta_1.obtenerNombre()} ")

        if atleta_1.mismaDestrezaQue(atleta_2):
            print (f"El atleta {atleta_1.obtenerNombre()} tiene la misma destreza que el atleta {atleta_2.obtenerNombre()} ")
        else:
            print (f"El atleta {atleta_1.obtenerNombre()} no tiene tiene la misma destreza que el atleta {atleta_2.obtenerNombre()} ")

        print ()
        
        # El atleta descansa 5 veces, se verifica que la energia aumente en 20 y no supere el maximo de energia.
        print (atleta_1)
        atleta_1.descansar()
        print (atleta_1)
        atleta_1.descansar()
        print (atleta_1)
        atleta_1.descansar()
        print (atleta_1)
        atleta_1.descansar()
        print (atleta_1)
        atleta_1.descansar()
        print (atleta_1)
        
        print ()
        
        #El atleta 2 entrena 20 veces, se verifica que al quedarse sin energia no pueda entrenar mas y la energia quede en 0, por ende no consigue destreza
        print (atleta_2)
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        print (atleta_2)
        atleta_2.entrenar()
        print (atleta_2)

        atleta_2.entrenar()
        atleta_2.entrenar()
        atleta_2.entrenar()
        print (atleta_2)
        

        #Se verifica la asociacion entre el atleta 2 y el atleta 1
        if atleta_2.mayorDestrezaQue(atleta_1):
            print (f"El atleta {atleta_2.obtenerNombre()} tiene mas destreza que el atleta {atleta_1.obtenerNombre()} ")
        else:
            print (f"El atleta {atleta_1.obtenerNombre()} tiene mas destreza que el atleta {atleta_2.obtenerNombre()} ")

        if atleta_2.mismaDestrezaQue(atleta_1):
            print (f"El atleta {atleta_2.obtenerNombre()} tiene la misma destreza que el atleta {atleta_1.obtenerNombre()} ")
        else:
            print (f"El atleta {atleta_2.obtenerNombre()} no tiene la misma destreza que el atleta {atleta_1.obtenerNombre()} ")

if __name__ == '__main__':
    TestAtleta.test()