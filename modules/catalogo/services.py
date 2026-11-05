import os


def obter_todos_livros():
    caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../dados.txt'))
    livros = []

    # Inicializa o arquivo com dados padrão caso não exista
    if not os.path.exists(caminho):
        with open(caminho, "w", encoding="latin-1") as f:
            f.write("1;O Hobbit;Fantasia;45.0\n2;1984;Ficcao;30.0\n3;Senhor dos Anéis;Fantasia;60.0\n")

    if os.path.exists(caminho):
        with open(caminho, "r", encoding="latin-1") as f:
            for linha in f:
                if linha.strip():
                    p = linha.strip().split(";")
                    if len(p) >= 4:
                        livros.append({
                            "id": p[0],
                            "titulo": p[1],
                            "genero": p[2],
                            "preco": float(p[3])
                        })
    return livros