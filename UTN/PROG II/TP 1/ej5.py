''' 5. Dada una cadena de texto ingresada por consola, decir cuántos “espacios” contiene. '''

cadena_string = "Hola como estas querido todo bien?"
prueba= cadena_string.split(' ')
cantidad_palabras = 0

for i in prueba:
    cantidad_palabras+=1

espacios = cantidad_palabras-1

print (f"La cantidad de espacios es de: {espacios}.")