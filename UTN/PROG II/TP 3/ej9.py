'''
Dada una lista de números, crea dos listas separadas: una que contenga los 
números pares y otra que contenga los números impares utilizando list 
comprehensions.
'''

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

lista_pares = [elemento for elemento in numeros if elemento % 2 == 0]
lista_impares = [elemento for elemento in numeros if elemento % 2 == 1]

print (lista_pares)
print (lista_impares)