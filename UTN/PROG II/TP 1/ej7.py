'''
Realizar un programa que solicite al usuario un número entero positivo, y luego en 
pantalla muestre solamente los números pares desde el 1 hasta el número 
ingresado.
Ej: usuario ingresa 10, en pantalla se mostrará 2 4 6 8 10
'''

numero_solicitado = int(input("Digite un numero: "))
verificacion_positivo = False
contador = 0
lista_secuencia_numeros = []
if (numero_solicitado > 0):
    verificacion_positivo = True

if (verificacion_positivo):
    while (contador < numero_solicitado):
        contador += 2
        print(contador)
        lista_secuencia_numeros.append(contador)
else:
    print("El numero no debe ser un numero negativo.")

lista_string = " "
for i in lista_secuencia_numeros:
    i = str(i)
    lista_string += i
    lista_string += ' '

print (f"Los numeros son: {lista_string}")