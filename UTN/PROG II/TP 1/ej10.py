'''
Escriba un programa que permita al usuario ingresar las medidas de 2 lados de un 
rectángulo, y que luego mediante la impresión repetida de un caracter (ej: *) lo dibuje 
en la pantalla. Para este ejercicio tomaremos un máximo de 40 para el lado más 
largo, con el fin de evitar problemas de visualización en la consola. Verificar en los 
datos de entrada que se cumpla este requisito
'''
lado_ancho = 4
lado_largo = 40
for i in range(lado_ancho):
    for y in range(lado_largo):
        print (f"*",end="")
    print ("")
