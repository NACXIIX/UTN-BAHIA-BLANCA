'''
Implemente una función que, dada una lista de números, devuelva una nueva lista 
que contenga el cuadrado de cada número utilizando list comprehensions
'''
listasauria = "risas"

def lista_al_cuadrado(lista):
    while True:
        try:
            nuevalista = [elemento**2 for elemento in lista]
            return nuevalista
        except TypeError:
            print ("Ingrese una lista.")

lista_al_cuadrado = lista_al_cuadrado(listasauria)
print(lista_al_cuadrado)