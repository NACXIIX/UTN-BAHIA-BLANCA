class Especie():
    # ATRIBUTOS DE INSTANCIA
    def __init__(self, nombre:str, machos:int = 0, hembras:int = 0, ritmo:float = 0):
        if isinstance (nombre, str):
            self.__nombre = nombre
        else:
            raise TypeError("El valor ingresado por parametro debe ser un string.")
        if isinstance(machos, int) and machos >= 0 and isinstance(hembras, int) and hembras >= 0 :
            self.__machos = machos
            self.__hembras = hembras
        else:
            raise TypeError("Los valores ingresados por parametro deben ser un numero entero positivo.")
        if isinstance(ritmo, (int, float)):
            self.__ritmo = ritmo
        else:
            raise TypeError("Los valores ingresados por parametro deben ser de tipo real")
        
    #COMANDOS
    
    def establecerHembras(self, cantHembras:int):
        if isinstance(cantHembras, int):
            if cantHembras > 0:
                self.__hembras = cantHembras
                
    def establecerMachos(self, cantMachos:int):
        if isinstance(cantMachos, int):
            if cantMachos > 0:
                self.__machos = cantMachos
                
    def establecerRitmo(self, ritmo:float):
        if isinstance(ritmo, (int,float)):
            self.__ritmo = ritmo
    
    def actualizarHembras(self, cantHembras: int):
        if isinstance(cantHembras, int):
            self.__hembras += cantHembras
            if self.__hembras < 0:
                self.__hembras = 0
        else:
            raise TypeError("El valor ingresado por parametro debe ser un numero.")
            
    def actualizarMachos(self, cantMachos: int):
        if isinstance(cantMachos, int):
            self.__machos += cantMachos
            if self.__machos < 0:
                self.__machos = 0
        else:
            raise TypeError("El valor ingresado por parametro debe ser un numero.")
        
    def actualizarRitmo(self, ritmo: float):
        if isinstance(ritmo, (int,float)):
            self.__ritmo += ritmo
        else:
            raise TypeError("El valor ingresado por parametro debe ser un numero real.")
    
    # CONSULTAS
    
    def poblacionActual(self)->int:
        return self.__machos + self.__hembras
    
    def poblacionEstimada(self, anios:int)->int:
        if isinstance(anios,int) and anios > 0:
            crecimiento =  self.poblacionActual() * self.__ritmo
            crecimiento_en_anios = crecimiento * anios + self.poblacionActual()
            return int(crecimiento_en_anios)
        else:
            raise TypeError("El valor ingresado por parametro debe ser un numero positivo.")
        
    def aniosParaPoblacion(poblacion:int)->int:
        # cuántos años serán necesarios estimativamente para que la  población alcance un valor dado.
        pass
    
    def riesgo(self)->str:
        crecimiento =  self.poblacionActual() * self.__ritmo
        nivel_riesgo = ""
        if crecimiento > 0:
            nivel_riesgo = "Verde"
        elif crecimiento < 0:
            nivel_riesgo = "Rojo"
        else:
            nivel_riesgo = "amarillo"
        
        return nivel_riesgo
    
    def __str__(self):
        return (f"Machos: {self.__machos} - Hembras: {self.__hembras} - Ritmo: {self.__ritmo}")
                
especie = Especie("Homo Pelonitis",15,20,20.3)
print(especie.poblacionEstimada(2))