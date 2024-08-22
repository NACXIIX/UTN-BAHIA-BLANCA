'''
 Escriba un programa que, dada una oración ingresada muestre por pantalla:

a. El número total de caracteres en la oración
b. La cantidad total de letras (consonantes y vocales, sin signos de puntuación)
c. La cantidad de palabras separadas por uno o más espacios

En este ejercicio, para simplificar, asumiremos que los posibles caracteres de 
entrada son letras, espacios, dígitos, signos de puntuación, signos de 
interrogación y de exclamación.
Investigar si hay funciones de strings que nos faciliten la resolución [len(), 
.isalpha(), .split() , etc.]
'''

texto = "j a j a j a!!"

total_caracteres = len(texto)
total_letras = 0
total_espacios = 0

for i in texto:
    i = i.lower()
    if (i >= "a" and i <= "z"):
        total_letras += 1

espacios = texto.split(' ')
total_espacios = len(espacios)-1

print (f"La oracion tiene un total de {total_caracteres} caracteres, {total_letras} letras y {total_espacios} espacios ")