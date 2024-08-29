'''
Dado un rango de números, crea una lista que contenga todos los números primos 
dentro de ese rango utilizando list comprehensions
'''

minimo_rango = 2
maximo_rango = 5
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
nuevalista = [elemento for elemento in numeros if elemento / 1 == elemento and elemento / elemento == 1 and elemento % 3 != 0]

print(nuevalista)

""" Los números primos son aquellos números enteros mayores que 1 que solo tienen dos divisores positivos:
    1 y el propio número. En otras palabras, un número primo no puede ser dividido por ningún otro número entero 
    aparte de 1 y él mismo sin dejar un residuo. Aquí tienes algunos ejemplos de números primos:

2 """