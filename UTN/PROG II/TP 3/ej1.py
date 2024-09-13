'''
Implemente una función que, dada una lista de números, devuelva una nueva lista 
que contenga el cuadrado de cada número utilizando list comprehensions
'''
lista = [1,2,3,4]

def lista_al_cuadrado():
    try:
        nuevalista = [elemento**2 for elemento in lista]
        return print(nuevalista)
    except TypeError:
        print("Ingrese numeros.")

    
lista_al_cuadrado()