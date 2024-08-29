'''
Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de 
vocales en ella. El programa deberá pedirle palabras al usuario hasta que éste 
introduzca la palabra “salir”.
'''

def contar_vocales():
    contador = 0
    repetir = True
    while repetir:
        pedir_palabra = input("Ingrese una palabra:")
        if (pedir_palabra == 'salir'):
            repetir = False
            
        for i in pedir_palabra:
            if (i == 'a'):
                contador +=1
            elif (i == 'e'):
                contador +=1
            elif (i == 'i'):
                contador +=1
            elif (i == 'o'):
                contador +=1
            elif (i == 'u'):
                contador +=1
                
    return print (f"la cantidad de vocales entre todas las palabras puestas son: {contador}")
            

contar_vocales()