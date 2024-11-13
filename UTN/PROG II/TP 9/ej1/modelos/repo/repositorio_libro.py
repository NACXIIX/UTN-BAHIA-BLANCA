from modelos.entidades.libro import Libro
import json

class RepositorioLibros:
    FILE_PATH = "datos\libros.json"
    
    def __init__(self):
        self.__libros = self.__cargarTodos()
        
    def __cargarTodos(self):
        lista = []
        try:
            with open(RepositorioLibros.FILE_PATH, 'r') as file:
                libros = json.load(file)
                for libro in libros:
                    lista.append(Libro.fromDiccionario(libro))
        except FileNotFoundError:
            print("No se encontro el archivo con datos de libros.")
        return lista

    def __guardarTodos(self):
        try:
            lista = []
            for libro in self.__libros:
                lista.append(libro.toDiccionario())
            
            with open (RepositorioLibros.FILE_PATH, 'w', encoding='utf-8') as file:
                json.dump(lista, file, indent=4)
        except FileNotFoundError:
            print("No se encontro el archivo con datos de libros.")
    
    #obtener todos los libros
    def obtenerTodos(self):
        return self.__libros

    #obtener un libro por codigo ISBN
    def obtenerPorISBN(self, ISBN:int):
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                return libro
        return None
    
    #agregar un libro
    def agregar(self, libro:Libro):
        if not isinstance(libro, Libro):
            raise TypeError("El valor ingresado por parametro en libro debe ser un Libro")
        if self.existeISBN(libro.obtenerISBN()):
            raise ValueError("El libro que desea agregar ya existe.")
        self.__libros.append(libro)
        self.__guardarTodos()
    
    #verificando si existe un libro por ISBN
    def existeISBN(self, ISBN)->bool:
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                return True
        return False

    #modificar un libro por ISBN
    def modificarPorISBN(self, ISBN:int, titulo:str, autor:str, genero:str, anioPublicacion:int)->bool:
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                libro.establecerTitulo(titulo)
                libro.establecerAutor(autor)
                libro.establecerGenero(genero)
                libro.establecerAnioPublicacion(anioPublicacion)
                return True
        return False
    
    def eliminarPorISBN(self, ISBN:int)->bool:
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                self.__libros.remove(libro)
                self.__guardarTodos()
                return True
        return False