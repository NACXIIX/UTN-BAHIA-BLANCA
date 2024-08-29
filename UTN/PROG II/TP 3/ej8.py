'''
Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los 
elementos únicos utilizando list comprehensions.
'''


lista = [3, 6, 2, 1, 6, 9, 10, 8, 3, 10]
nuevalista = [elemento for elemento in lista if lista.count(elemento) == 1]

print (nuevalista)