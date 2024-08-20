''' 
Se desea realizar una aplicación que solicite al usuario tres números enteros 
positivos (A, B, y X), y que muestre por pantalla todos los múltiplos de X que estén 
entre A y B inclusive. 
'''

a = int(input("Coloque un numero: "))
b = int(input("Coloque un numero: "))
x = int(input("Coloque un numero: "))
variable = x
verificacion_positivo = False

if(a > 0 and b > 0 and x > 0):
    verificacion_positivo = True

if (verificacion_positivo):
    for i in range(a+(x-a), b+1, x):
        if (variable >= a):
            print (f"Multiplo de {x}: {i}")
        else:
            variable += x
        
else:
    print("\nERROR: Todos los numeros deben ser positivos")
