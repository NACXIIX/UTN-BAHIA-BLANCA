''' 
Escribir un procedimiento “reverso” que permita ingresar como parámetro una 
cadena, y devuelva la cadena invertida (“hola” se convierte en “aloh”). Escribir luego 
un programa que determine si una cadena de caracteres es un palíndromo (un 
palíndromo es un texto que se lee igual en sentido directo y en inverso, ej.: “radar”). 
Sugerencia: para evitar diferencias entre mayúsculas y minúsculas en las cadenas, 
utilice la función del tipo string .upper() ó .lower() en las cadenas, ya que Radar es 
distinto a radaR.
'''

palabra = input("Escriba una palabra: ")

def reverse(x):
    mensaje = f"Las letras al revés son: {x[::-1]}"
    return print (mensaje, end=", ")

def palindromo(palabra):
    palabra = palabra.lower()
    if (palabra == reverse(palabra)):
        return print ("La palabra es palindromo")
    else:
        return print ("La palabra no es palindromo")

print (reverse(palabra))
print ("AHI VA")