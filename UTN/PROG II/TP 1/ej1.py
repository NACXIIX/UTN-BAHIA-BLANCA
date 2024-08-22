lado_1 = int(input("Coloque la longitud del lado 1 del triangulo: "))
lado_2 = int(input("Coloque la longitud del lado 2 del triangulo: "))
lado_3 = int(input("Coloque la longitud del lado 3 del triangulo: "))

if (lado_1 == lado_2 and lado_2 == lado_3):
    print ("el triangulo es Equilatero")
elif lado_1 != lado_2 and lado_3 != lado_1 and lado_2 != lado_3:
    print ("el triangulo es Escaleno")
else:
    print ("el triangulo es Isosceles")
