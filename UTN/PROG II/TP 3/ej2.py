'''
Implemente una función que, dada una lista de nombres, devuelva una nueva lista 
que contenga solo los nombres que tengan una longitud mayor o igual a una 
cantidad de caracteres pasada por parámetro, utilizando list comprehensions.
'''

lista_nombres = ["Nicolas", "Rafa", "Santinin", "Pol", "Rayo"]

def nueva_lista_nombres(numero):

    nueva_lista = [nombres for nombres in lista_nombres if len(nombres) >= numero]
    return nueva_lista

nueva_lista_nombres = nueva_lista_nombres(5)
print(nueva_lista_nombres)