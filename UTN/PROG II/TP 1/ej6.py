''' Realizar un programa que solicite al usuario un número entero positivo, y luego en 
pantalla muestre la secuencia de números desde el 1 hasta el número ingresado.
Ej: usuario ingresa 10, en pantalla se mostrará 1 2 3 4 5 6 7 8 9 10 '''

numero_solicitado = int(input("Coloque un numero entero positivo: "))
validacion_numero_positivo = False
contador = 0
listado_secuencia = []

if (numero_solicitado > 0):
    validacion_numero_positivo = True

if (validacion_numero_positivo == True):
    while (contador < numero_solicitado):
        contador += 1
        listado_secuencia.append(contador)
else:
    print("El numero ingresado debe ser positivo.")

string_numeros = ''
for i in listado_secuencia:
    i = str(i)
    string_numeros += i
    string_numeros += ' '

print (f"La secuencia de numeros hasta el numero ingresado es: {string_numeros}")