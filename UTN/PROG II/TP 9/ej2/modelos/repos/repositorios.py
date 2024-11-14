from modelos.repos.repositorio_socios import RepositorioSocios

repo_Socios = None

def obtenerRepositorioSocios():
    global repo_Socios
    if repo_Socios is None:
        repo_Socios = RepositorioSocios()
    return repo_Socios