from models.repos.repositorio_generos import Repo_Generos
from models.repos.repositorio_videojuegos import Repo_videojuegos
from models.repos.repositorio_desarrollador import Repo_desarrolladoras

repo_Generos = None
repo_Videojuegos = None
repo_Desarrolladoras = None

def obtenerRepositorioGeneros():
    global repo_Generos
    
    if repo_Generos is None:
        repo_Generos = Repo_Generos()
    return repo_Generos

def obtenerRepositorioVideojuegos():
    global repo_Videojuegos
    
    if repo_Videojuegos is None:
        repo_Videojuegos = Repo_videojuegos()
    return repo_Videojuegos

def obtenerRepositorioDesarrolladoras():
    global repo_Desarrolladoras
    
    if repo_Desarrolladoras is None:
        repo_Desarrolladoras = Repo_desarrolladoras()
    return repo_Desarrolladoras