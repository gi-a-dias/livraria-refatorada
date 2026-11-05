FAVORITOS_DB = set()

def alternar_favorito(livro_id):
    if livro_id in FAVORITOS_DB:
        FAVORITOS_DB.remove(livro_id)
        return False
    else:
        FAVORITOS_DB.add(livro_id)
        return True

def obter_favoritos():
    return list(FAVORITOS_DB)