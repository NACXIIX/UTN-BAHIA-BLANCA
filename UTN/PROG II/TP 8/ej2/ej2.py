import json

class Contacto:
    def __init__(self, nombre:str, apellido:str, telefono:str, correoElectronico:str, direccion:str):
        if not isinstance(nombre, str):
            raise TypeError("El valor ingresado por parametro en nombre debe ser un string.")
        if not isinstance(apellido, str):
            raise TypeError("El valor ingresado por parametro en apellido debe ser un string.")
        if not isinstance(telefono, str):
            raise TypeError("El valor ingresado por parametro en telefono debe ser un string.")
        if not isinstance(correoElectronico, str):
            raise TypeError("El valor ingresado por parametro en correo electronico debe ser un string.")
        if not isinstance(direccion, str):
            raise TypeError("El valor ingresado por parametro en direccion debe ser un string.")
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__correoEletronico = correoElectronico
        self.__direccion = direccion
        
    def serializarContacto(self)->dict:
        dict_contacto = {
            "nombre":self.__nombre,
            "apellido":self.__apellido,
            "telefono":self.__telefono,
            "correoElectronico":self.__correoEletronico,
            "direccion":self.__direccion
        }
        return dict_contacto
    
    @classmethod
    def deserializarContacto(cls, data)->'Contacto':
        if isinstance(data, dict):
            return cls(data["nombre"], data["apellido"], data["telefono"], data["correoElectronico"], data["direccion"])
        else:
            raise TypeError("El valor ingresado por parametro en json data debe ser de tipo diccionario.")
    
    def obtenerApellido(self):
        return self.__apellido

    def __str__(self):
        return f"Nombre: {self.__nombre} - Apellido: {self.__apellido} - Teléfono: {self.__telefono} - Correo Electrónico: {self.__correoEletronico} - Direccion: {self.__direccion}"

class TesterContacto:
    @staticmethod
    def test():
        lista_contactos = []
        contacto1 = Contacto("Juan", "Pérez", "123-456-7890", "juan.perez@email.com", "Calle Falsa 123")
        contacto2 = Contacto("Ana", "Gómez", "234-567-8901", "ana.gomez@email.com", "Av. Siempre Viva 456")
        contacto3 = Contacto("Carlos", "López", "345-678-9012", "carlos.lopez@email.com", "Boulevard Central 789")
        contacto4 = Contacto("María", "Martínez", "456-789-0123", "maria.martinez@email.com", "Ruta Provincial 101")
        contacto5 = Contacto("Luis", "Fernández", "567-890-1234", "luis.fernandez@email.com", "Camino Real 202")
        contacto6 = Contacto("Sofía", "Rodríguez", "678-901-2345", "sofia.rodriguez@email.com", "Pasaje Colón 303")
        lista_contactos.append(contacto1)
        lista_contactos.append(contacto2)
        lista_contactos.append(contacto3)
        lista_contactos.append(contacto4)
        lista_contactos.append(contacto5)
        lista_contactos.append(contacto6)
        
        with open("contactos.json", "w", encoding="utf-8") as file:
            dict_contactos = [contacto.serializarContacto() for contacto in lista_contactos]
            json.dump(dict_contactos, file, ensure_ascii=False, indent=4)
        
        lista_reconstruida_contactos = []
        with open("contactos.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            for contacto in data:
                lista_reconstruida_contactos.append(Contacto.deserializarContacto(contacto))
                
        pedir_letra = str(input("letra: "))
        for contacto in lista_reconstruida_contactos:
            apellido_contacto = contacto.obtenerApellido()
            
            if apellido_contacto[0].lower() == pedir_letra.lower():
                print (contacto)

TesterContacto.test()