'''
Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo 
las palabras que comienzan con una letra específica (por ejemplo, "a") indicada por 
el usuario, utilizando list comprehensions.
'''

diccionario = {
    "salame": "gusto picante depende la marca que compres.",
    "mortadela": "un clasico.",
    "bondiola": "ostias, esto es riquisimo.",
    "jamon cocido": "si te estas cuidando, esto es un poco mas saludable que el rest.o",
    "osobuco": "osobuco argentino, algunas personas comen eso los domingos.",
    "jamon crudo": "Sanisimo, pero tiene muchisima sal"
}

dato = input("Elija una letra:")

def letra(letra):
    nueva_lista = [clave for clave in diccionario.keys() if clave[0] == letra.lower() or clave[0] == letra.upper()]
    return nueva_lista

mostrar_lista = letra(dato)

print(mostrar_lista)