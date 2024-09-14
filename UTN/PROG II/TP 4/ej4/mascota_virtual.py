class MascotaVirtual:
    """
        Las actividades de desgaste son: JUGAR, CAMINAR, SALTAR
        
        Las actividades COMER, BEBER, DORMIR Y BAÑAR resetean el contador de actividades de desgaste
    """
    __MAX_VALOR = 100
    __MIN_VALOR = 0

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

    def __str__(self):
        return f'El nombre de la mascota es: {self.__nombre}'

    # COMANDOS
    def comer(self):
        if self.estaVivo():
            self.__energia += 20
        else:
            print ("La mascota no esta viva.")
            
    
    def beber(self):
        if self.estaVivo():
            self.__energia += 10
        else:
            print ("La mascota no esta viva.")
    
    def dormir(self):
        if self.estaVivo():
            if self.estaDormido():
                print ("La mascota ya esta durmiendo")
            else:
                self.__energia += 20
                self.__diversion -= 10
        else:
            print ("La mascota no esta viva.")
    
    def despertar(self):
        pass
    
    def jugar(self):
        if self.estaVivo():
            self.__diversion += 40
            self.__energia -= 20
            self.__higiene -= 25
        else:
            print ("La mascota no esta viva.")
    
    def caminar(self):
        if self.estaVivo():
            self.__diversion += 20
            self.__energia -= 10
            self.__higiene -= 8
        else:
            print ("La mascota no esta viva.")
    
    def saltar(self):
        if self.estaVivo():
            self.__diversion += 10
            self.__energia -= 15
            self.__higiene -= 10
        else:
            print ("La mascota no esta viva.")
            
    def bañar(self):
        if self.estaVivo():
            self.__higiene += 40
            self.__diversion -= 10
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
            return f'Humor feliz'
        
    def estaVivo(self)->bool:
        esta_vivo = False
        if self.__energia > 0:
            esta_vivo = True
        else:
            esta_vivo = False
        return esta_vivo
    
mascota = MascotaVirtual("Pandasaurus")
print (mascota.obtenerEnergia())
mascota.comer()
print (mascota.obtenerEnergia())
mascota.jugar()
print (mascota.obtenerEnergia())
mascota.jugar()
print (mascota.obtenerEnergia())
mascota.jugar()
print (mascota.obtenerEnergia())
mascota.jugar()
print (mascota.obtenerEnergia())
mascota.jugar()
print (mascota.obtenerEnergia())
mascota.jugar()
print (mascota.obtenerEnergia())
mascota.jugar()
print (mascota.obtenerEnergia())
mascota.jugar()
print (mascota.obtenerEnergia())
mascota.jugar()
print (mascota.obtenerEnergia())
mascota.jugar()
print (mascota.obtenerEnergia())