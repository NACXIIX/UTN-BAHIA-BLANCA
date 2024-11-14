from modelos.entidades.socio import Socio
from datetime import date
import json
class RepositorioSocios:
    
    FILE_PATH = "datos\socios.json"
    
    def __init__(self):
        self.__socios = self.__cargarTodos()
        
    def __cargarTodos(self):
        lista = []
        try:
            with open (RepositorioSocios.FILE_PATH, "r", encoding="utf-8") as file:
                socios = json.load(file)
                for socio in socios:
                    lista.append(Socio.fromDiccionario(socio))
        except: FileNotFoundError("No se ha encontrado el archivo")
        return lista
    
    def __guardarTodos(self):
        try:
            lista = []
            for socio in self.__socios:
                lista.append(socio.toDiccionario())
            
            with open(RepositorioSocios.FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(lista, file, indent=4)
                
        except: FileNotFoundError("No se ha encontrado el archivo")
        
    def obtenerTodos(self)->list:
        return self.__socios

    def existe(self,socio:'Socio')->bool:
        for s in self.__socios:
            if s.esIgual(socio):
                return True
        return False
    
    def existeDNI(self, dni:int)->bool:
        for s in self.__socios:
            if s.obtenerDNI() == dni:
                return True
        return False
    
    def agregar(self, nuevoSocio:'Socio'):
        if isinstance(nuevoSocio, Socio):
            if self.existeDNI(nuevoSocio.obtenerDNI()):
                return ValueError("El socio ya existe")
            self.__socios.append(nuevoSocio)
            self.__guardarTodos()
    
    def modificarPorDNI(self, DNI:int, nombre:str, apellido:str, mail:str, fecha_nacimiento:date):
        for socio in self.__socios:
            if DNI == socio.obtenerDNI():
                socio.establecerNombre(nombre)
                socio.establecerApellido(apellido)
                socio.establecerMail(mail)
                socio.establecerFechaNacimiento(fecha_nacimiento)
                self.__guardarTodos()
                return True
        return False
                
    def eliminarPorDNI(self, DNI:int):
        for socio in self.__socios:
            if DNI == socio.obtenerDNI():
                self.__socios.remove(socio)
                self.__guardarTodos()
                return True
        return False
    
    def obtenerPorDNI(self, DNI:int):
        for socio in self.__socios:
            if DNI == socio.obtenerDNI():
                return socio