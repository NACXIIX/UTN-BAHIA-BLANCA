'''
 Escriba un programa que para un texto ingresado nos muestre cual es la palabra 
más larga dentro de ese texto y cuántas letras tiene.
'''

texto = "Hola que haces padre como va eso"
palabras = texto.split(" ")
palabra_mas_larga = ""

for i in palabras:
    print (i)
    if (len(i) >= len(palabra_mas_larga)):
        palabra_mas_larga = i
cantidad_letras_palabra = len(palabra_mas_larga)
print(f"La palabras mas larga del texto es: {palabra_mas_larga} y tiene {cantidad_letras_palabra} letras")