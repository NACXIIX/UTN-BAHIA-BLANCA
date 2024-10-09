class Color:
    def __init__(self, rojo:int = 255, verde:int = 255, azul:int = 255):
        if isinstance(rojo, int) and 0 <= rojo <= 255:
            self.__rojo = rojo
        else:
            raise TypeError("El valor ingresado por parametro debe ser un numero entero positivo entre 0 y 255 inclusive.")
        if isinstance(verde, int) and 0 <= verde <= 255:
            self.__verde = verde
        else:
            raise TypeError("El valor ingresado por parametro debe ser un numero entero positivo entre 0 y 255 inclusive.")
        if isinstance(azul, int) and 0 <= azul <= 255:
            self.__azul = azul
        else:
            raise TypeError("El valor ingresado por parametro debe ser un numero entero positivo entre 0 y 255 inclusive.")
            

    def variar(self, valor:int):
        if isinstance(valor, int):
            if valor >= 0:
                self.__rojo += valor
                self.__verde += valor
                self.__azul += valor
                if self.__rojo > 255:
                    self.__rojo = 255
                if self.__verde > 255:
                    self.__verde = 255
                if self.__azul > 255:
                    self.__azul = 255
            else:
                self.__rojo += valor
                self.__verde += valor
                self.__azul += valor
                if self.__rojo < 0:
                    self.__rojo = 0
                if self.__verde < 0:
                    self.__verde = 0
                if self.__azul < 0:
                    self.__azul = 0
        else:
            raise TypeError("El valor ingresado por parametro debe ser un numero entero positivo mayor o igual a 0.")
    
    def variarRojo(self, valor:int):
        if isinstance(valor, int) and valor >= 0:
            self.__rojo += valor
        else:
            raise TypeError("El valor ingresado por parametro debe ser un numero entero positivo mayor o igual a 0.")

    def variarAzul(self, valor:int):
        if isinstance(valor, int) and valor >= 0:
            self.__azul += valor
        else:
            raise TypeError("El valor ingresado por parametro debe ser un numero entero positivo mayor o igual a 0.")

    def variarVerde(self, valor:int):
        if isinstance(valor, int) and valor >= 0:
            self.__verde += valor
        else:
            raise TypeError("El valor ingresado por parametro debe ser un numero entero positivo mayor o igual a 0.")
    
    def establecerRojo(self, valor:int):
        if isinstance(valor, int) and  0 <= valor <= 255:
            self.__rojo = valor
        else:
            raise TypeError("El valor ingresado por parametro debe ser un numero entero positivo entre 0 y 255 inclusive.")
        
    def establecerAzul(self, valor:int):
        if isinstance(valor, int) and  0 <= valor <= 255:
            self.__azul = valor
        else:
            raise TypeError("El valor ingresado por parametro debe ser un numero entero positivo entre 0 y 255 inclusive.")
        
    def establecerVerde(self, valor:int):
        if isinstance(valor, int) and  0 <= valor <= 255:
            self.__verde = valor
        else:
            raise TypeError("El valor ingresado por parametro debe ser un numero entero positivo entre 0 y 255 inclusive.")
    
    def copiar(self, otroColor: 'Color'):
        if isinstance(otroColor, object):
            self.__rojo = otroColor.obtenerRojo()
            self.__verde = otroColor.obtenerVerde()
            self.__azul = otroColor.obtenerAzul()
        else:
            raise TypeError("El valor ingresado por parametro debe ser un objeto de tipo Color.")
        
    def obtenerRojo(self):
        return self.__rojo
    
    def obtenerVerde(self):
        return self.__verde
    
    def obtenerAzul(self):
        return self.__azul
    
    def __str__(self):
        return f"R:{self.__rojo} - G:{self.__verde} - B:{self.__azul}"
    
color = Color()
color_1 = Color(150,231,58)

print(color)
print(color_1)

color.copiar(color_1)
print(color)