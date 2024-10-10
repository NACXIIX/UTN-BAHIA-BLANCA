from color import Color

class TestColor():
    @staticmethod
    def test():
        
        # Diagrama 4-a
        color_1 = Color()
        color_2 = Color(70,70,70)
        color_3 = Color(255,255,255)
        
        igualdad1 = color_1.esIgualQue(color_2)
        igualdad2 = color_2.esIgualQue(color_3)
        
        if igualdad1:
            print("El color 1 tiene el mismo estado interno(equivalencia) que el color 2.")
        else:
            print("El color 1 y el color 2 no son equivalentes.")
            
        if igualdad2:
            print("El color 2 tiene el mismo estado interno(equivalencia) que el color 3.")
        else:
            print("El color 2 y el color 3 no son equivalentes.")
            
        color_4 = color_1
        color_5 = color_2.clonar()
        
        
        print("punto 4 a)")
        print(f"color 1: {color_1}")
        print(f"color 2: {color_2}")
        print(f"color 3: {color_3}")
        print(f"color 4: {color_4}")
        print(f"color 5: {color_5}")
        
        # Diagrama 4-b
        color_6 = Color(140,250,140)
        color_4 = color_6
        color_2 = color_5.clonar()
        igualdad3 = color_2.esIgualQue(color_5)
        if igualdad3:
            print("El color 2 tiene el mismo estado interno(equivalencia) que el color 5.")
        else:
            print("El color 2 y el color 5 no son equivalentes.")
        color_3 = color_2
        color_1 = color_5.complemento()
        
        print("punto 4 b)")
        print(f"color 1: {color_1}")
        print(f"color 2: {color_2}")
        print(f"color 3: {color_3}")
        print(f"color 4: {color_4}")
        print(f"color 5: {color_5}")
        print(f"color 5: {color_6}")
        
        
        color_1 = color_5.complemento() # Aca lo que sucede es que a la variable color_1 se le asigna un nuevo objeto con el estado interno acorde al  complemento del estado interno que tiene el objeto que hace referencia a la variable color_5, todo esto mediante el metodo llamado complemento.
        color_2 = color_5.clone() # A la variable color_2 se le asigna un objeto nuevo con el mismo estado interno que tiene el objeto al que hace referencia la variable color_5 
        color_3 = color_2 # La variable color_3 toma la misma referencia al objeto al cual la variable color_2 esta referenciando, es decir las 2 variables apuntan al mismo objeto.
        

if __name__ == '__main__':
    TestColor.test()