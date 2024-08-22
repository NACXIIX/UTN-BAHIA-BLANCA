'''
 Escriba un programa que dado un texto ingresado por el usuario cuente la cantidad 
total de vocales que aparecen y lo muestre por pantalla.
 '''

texto = input("Ingrese un texto y se contaran las vocales que se encuentren: ")

cantidad_vocales = 0

for letras in texto:
    if (letras == "a"):
        cantidad_vocales += 1
    elif (letras == "e"):
        cantidad_vocales += 1
    elif (letras == "i"):
        cantidad_vocales += 1
    elif (letras == "o"):
        cantidad_vocales += 1
    elif (letras == "u"):
        cantidad_vocales += 1
    else:
        continue

print (f"La cantidad de vocales que tiene su texto es de: {cantidad_vocales}")