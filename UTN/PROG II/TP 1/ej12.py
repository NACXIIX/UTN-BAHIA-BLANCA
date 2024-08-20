'''
Escriba un programa que permita el ingreso de números enteros positivos, 
finalizando el ingreso con 0, y luego indique si la secuencia estaba ordenada de 
menor a mayor.
'''

lista_original = []
lista_copia = []
numero = 0
validacion_positivo = False

while (numero >= 0 or numero <= 0):     
    numero = int(input("Coloque un numero: "))
    if (numero >= 0):
        validacion_positivo = True
    
    if (validacion_positivo and numero > 0):
        lista_original.append(numero)
        lista_copia.append(numero)
    if (numero == 0):
        break
    
lista_original.sort()

if (lista_copia == lista_original):
    print ("La lista esta ordenada de menor a mayor")
else:
    print ("La lista no esta ordenada")
