'''
Escriba un programa que permita el ingreso de números enteros positivos para 
calcular su promedio, el ingreso finaliza cuando el usuario ingresa un número 
negativo. Luego mostrar el promedio y la cantidad de valores que se ingresaron. Ej: 
“El promedio es ….. con un total de …. ingresos.”
'''

""" cantidad_valores = []
numero = 0

while (numero >= 0):
    numero = int(input("Coloque un numero:"))
    if(numero >= 0):
        cantidad_valores.append(numero)

suma_total = 0
for i in cantidad_valores:
    suma_total += i
    
print (f"La cantidad de valores que se ingresaron fueron: {len(cantidad_valores)}")
print (f"El promedio es de {suma_total / len(cantidad_valores)}")

print (cantidad_valores) """

# Ahora sin lista

numero = 0
suma_total = 0
cantidad_valores = 0

while (numero >= 0):
    numero = int(input("Coloque un numero:"))
    if (numero >=0):
        suma_total += numero
        cantidad_valores +=1
    
print (f"La cantidad de valores que se ingresaron fueron: {cantidad_valores}")
print (f"El promedio es de {suma_total / cantidad_valores}")