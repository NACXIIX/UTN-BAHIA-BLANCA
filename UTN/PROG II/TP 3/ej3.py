'''
 Lee el contenido de un archivo de texto llamado "datos.txt" y crea una lista con todas 
las líneas del archivo, utilizando list comprehensions.
'''

ruta = r"C:\Users\Nico\Desktop\UTN-BAHIA-BLANCA\UTN\PROG II\TP 3\archivos\datos.txt"

archivo = open(ruta, "r")

lista = [linea.strip() for linea in archivo]


print (lista)
archivo.close()