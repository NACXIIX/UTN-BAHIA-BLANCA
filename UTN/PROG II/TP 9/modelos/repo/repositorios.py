from modelos.repo.repositorio_libro import RepositorioLibros

repo_Libros = None

def obtenerRepositorioLibros():
    global repo_Libros
    if repo_Libros is None:
        repo_Libros = RepositorioLibros()
    return repo_Libros