ancho = int(input("Coloque el ancho de la habitacion rectangular: "))
alto = int(input("Coloque el alto de la habitacion rectangular: "))
largo = int(input("Coloque el largo de la habitacion rectangular: "))

litro_pintura_en_m2 = 10
puerta_en_m2 = 2 * 0.8

total_habitacion_en_m2 = (2 * alto * (ancho + largo)) - puerta_en_m2

cantidad_necesaria_pintura = (total_habitacion_en_m2 * 1) / litro_pintura_en_m2

print (f"La cantidad de litros de pintura que se necesita para pintar las paredes de la habitacion es de: {cantidad_necesaria_pintura} litros.")