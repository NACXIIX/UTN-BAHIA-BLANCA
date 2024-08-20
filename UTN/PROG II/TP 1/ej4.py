'''  Pedir 3 números enteros e implementar un algoritmo para determinar cuál es el 
mayor de los 3 y mostrar un mensaje por pantalla '''

print ("Elija 3 numeros para saber cual es el mayor de los 3.")
numero_1 = input("Numero 1: ")
numero_2 = input("Numero 2: ")
numero_3 = input("Numero 3: ")

if (numero_1 > numero_2 and numero_1 > numero_3):
    print (f"El numero mayor es el {numero_1}")
elif (numero_2 > numero_1 and numero_2 > numero_3):
    print (f"El numero mayor es el {numero_2}")
else:
    print (f"El numero mayor es el {numero_3}")
