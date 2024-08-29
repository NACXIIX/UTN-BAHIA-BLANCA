'''
Dado un diccionario de personas y sus edades, crea una lista que contenga solo los 
nombres de las personas cuya edad es mayor a una edad ingresada por el usuario, 
utilizando list comprehensions.
'''

diccionario = {
    "Andres" : 30,
    "Alfredo" : 46,
    "Claudio" : 35,
    "Martin" : 20,
    "Julian" : 10,
    "Mauricio" : 15,
    "Nicolas" : 19,
    "Jose" : 17
}

pedir_edad = int(input("Coloque una edad y se devolvera las personas mayores a la ingresada: "))
def personas_mayores(dato):
    nuevalista = [nombre for nombre,edad in diccionario.items() if edad > dato]
    return nuevalista

pidiendo_edad = personas_mayores(pedir_edad)

print (pidiendo_edad)
