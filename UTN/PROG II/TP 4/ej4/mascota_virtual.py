class MascotaVirtual:
    """
        Las actividades de desgaste son: JUGAR, CAMINAR, SALTAR
        
        Las actividades COMER, BEBER, DORMIR Y BAÑAR resetean el contador de actividades de desgaste
    """
    
    #ATRIBUTOS DE CLASE
    __MAX_VALOR = 100
    __MIN_VALOR = 0

    #ATRIBUTOS DE INSTANCIA
    def __init__(self, nombre:str):
        if isinstance (nombre, str):
            self.__nombre = nombre
        else:
            raise TypeError("El nombre de la mascota debe ser un string")
        
        self.__energia = self.__MAX_VALOR
        self.__diversion = self.__MAX_VALOR
        self.__higiene = self.__MAX_VALOR
        self.__dormido = False
        self.__cantActividadesDesgaste = 3

    # COMANDOS
    def comer(self):
        """
        Aumenta la energia en 20 puntos.
        """
        if self.estaVivo():
            self.__energia += 20
            self.__cantActividadesDesgaste = self.__MAX_VALOR
        else:
            print ("La mascota no esta viva.")
            
    
    def beber(self):
        """
        Aumenta la energia en 10 puntos.
        """
        if self.estaVivo():
            self.__energia += 10
            self.__cantActividadesDesgaste = self.__MAX_VALOR
        else:
            print ("La mascota no esta viva.")
    
    def dormir(self):
        """
        Aumenta la energia en 20 puntos,
        reduce la diversion en 10 puntos.
        """
        if self.estaVivo():
            if self.estaDormido():
                print ("La mascota ya esta durmiendo")
            else:
                self.__energia += 20
                self.__diversion -= 10
                self.__cantActividadesDesgaste = self.__MAX_VALOR
        else:
            print ("La mascota no esta viva.")
    
    def despertar(self):
        if self.estaVivo():
            self.__dormido = True
            self.__cantActividadesDesgaste = self.__MAX_VALOR
            return self.__dormido
        else:
            print("La mascota no esta viva.")
    
    def jugar(self):
        """
        Aumenta la diversion en 40 puntos,
        reduce la energia en 20 puntos,
        reduce la higiene en 15 puntos.
        """
        if self.estaVivo():
            self.__diversion += 40
            self.__energia -= 20
            self.__higiene -= 15
            self.__cantActividadesDesgaste -= 1
        else:
            print ("La mascota no esta viva.")
    
    def caminar(self):
        """
        Aumenta la diversion en 20 puntos,
        reduce la energia en 10 puntos,
        reduce la higiene en 8 puntos
        """
        if self.estaVivo():
            self.__diversion += 20
            self.__energia -= 10
            self.__higiene -= 8
            self.__cantActividadesDesgaste -= 1
        else:
            print ("La mascota no esta viva.")
    
    def saltar(self):
        """
        Aumenta la diversion en 10 puntos,
        reduce la energia en 15 puntos,
        reduce la higiene en 10 puntos.
        """
        if self.estaVivo():
            self.__diversion += 10
            self.__energia -= 15
            self.__higiene -= 10
            self.__cantActividadesDesgaste -= 1
        else:
            print ("La mascota no esta viva.")
            
    def bañar(self):
        """
        Aumenta la higiene en 40 puntos,
        reduce la diversion en 10 puntos.
        """        
        if self.estaVivo():
            self.__higiene += 40
            self.__diversion -= 10
            self.__cantActividadesDesgaste = self.__MAX_VALOR
        else:
            print ("La mascota no esta viva.")

    # CONSULTAS
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerEnergia(self)->int:
        return self.__energia
    
    def obtenerDiversion(self)->int:
        return self.__diversion
    
    def obtenerHigiene(self)->int:
        return self.__higiene
    
    def estaDormido(self)->bool:
        pass

    def obtenerHumor(self)->str:
        if self.__energia >= 70 and self.__diversion >= 70 and self.__higiene >= 70:
            humor = "Feliz"
            
        if 50 < self.__energia < 70 and 50 < self.__diversion < 70 and 50 < self.__higiene < 70:
            humor = "Alegre"
        elif 50 < self.__energia < 70 and 50 < self.__diversion < 70 or 50 < self.__higiene < 70:
            humor = "Alegre"
        elif 50 < self.__energia < 70 or 50 < self.__diversion < 70 and 50 < self.__higiene < 70:
            humor = "Alegre"
        elif 50 < self.__energia < 70 or 50 < self.__diversion < 70 or 50 < self.__higiene < 70:
            humor = "Alegre"
        
        if 30 < self.__energia < 50 and 30 < self.__diversion < 50 and 30 < self.__higiene < 50:
            humor = "Neutral"
        elif 30 < self.__energia < 50 and 30 < self.__diversion < 50 or 30 < self.__higiene < 50:
            humor = "Neutral"
        elif 30 < self.__energia < 50 or 30 < self.__diversion < 50 and 30 < self.__higiene < 50:
            humor = "Neutral"
        elif 30 < self.__energia < 50 or 30 < self.__diversion < 50 or 30 < self.__higiene < 50:
            humor = "Neutral"
        
        if 10 < self.__energia < 30 and 10 < self.__diversion < 30 and 10 < self.__higiene < 30:
            humor = "Triste"
        elif 10 < self.__energia < 30 and 10 < self.__diversion < 30 or 10 < self.__higiene < 30:
            humor = "Triste"
        elif 10 < self.__energia < 30 or 10 < self.__diversion < 30 and 10 < self.__higiene < 30:
            humor = "Triste"
        elif 10 < self.__energia < 30 or 10 < self.__diversion < 30 or 10 < self.__higiene < 30:
            humor = "Triste"

        if self.__energia <= 10 or self.__diversion <= 10 or self.__higiene <= 10:
            humor = "Muy triste"
            
        return humor
            
    def estaVivo(self)->bool:
        esta_vivo = False
        if self.__energia > 0:
            esta_vivo = True
        else:
            esta_vivo = False
        return esta_vivo
    
    def __str__(self):
        return f"Nombre: {self.obtenerNombre()} - Energia: {self.obtenerEnergia()} - Diversion: {self.obtenerDiversion()} - Higiene: {self.obtenerHigiene()} - Humor: {self.obtenerHumor()}"
