'''  
Se desea realizar una aplicación que solicite al usuario un caracter y un número 
natural N, y que la aplicación muestre en pantalla dicho carácter repetido N veces 
consecutivas.
Ej: Ingrese un caracter: +
Ingrese la cantidad de rep
'''

caracter = input("Ingrese un caracter: ")
repeticiones = int(input("Ingrese la cantidad de repeticiones"))

muestra = caracter * repeticiones

print (muestra)