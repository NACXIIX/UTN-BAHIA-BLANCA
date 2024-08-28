'''
Escriba un programa que permita ingresar un número, se debe validar que 
realmente se haya ingresado un número, y crear una lista para almacenar por 
separado los dígitos del número. Luego recorrer la lista y mostrar el índice que 
contiene el dígito mayor. 
'''

def pedir_numero():    
    try:
        numero = int(input("Ingrese un numero: "))
        numero = str(numero)
        lista_numeros = [elemento for elemento in numero]
    except ValueError:
        print ("Se debe ingresar un numero.")
    return lista_numeros


def mostrar_mayor_indice():
    lista = []
    for i in pedir_numero():
        i = int(i)
        lista.append(i)

    for i in range(len(lista)):
        mayor = 0
        if (lista[i] > mayor):
            mayor = lista[i]
            indice = i
    print (f"El numero mayor es: {mayor} y su indice: {indice}")
mostrar_mayor_indice()