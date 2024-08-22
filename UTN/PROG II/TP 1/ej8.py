''' Desarrollar un programa que permita al usuario indicar cuantos valores quiere 
ingresar, luego que permita la carga de los valores por teclado y nos muestre 
posteriormente la suma de los valores ingresados y su promedio.
'''

cantidad_valores = int(input("Digite la cantidad de valores a ingresar: "))
contador = 0
valores = []

while (contador < cantidad_valores):
    valor = input("Digite un valor: ")
    valores.append(valor)
    contador+=1

suma_total = 0
cantidad_numeros = 0
for numeros in valores:
    suma_total += int(numeros)
    cantidad_numeros+=1

print (f"El promedio de los numeros es de {suma_total / cantidad_numeros}")