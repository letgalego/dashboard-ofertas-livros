"""Leitura dos arquivos CSV do projeto e conversão dos textos em números."""

import csv
from pathlib import Path

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"
CAMINHO_FAVORITOS = PASTA / "favoritos.csv"
CAMPOS_FAVORITO = ["titulo", "preco", "categoria", "status", "comentario"]

def encontrar_mais_caro(livros):
    """Devolve o livro de maior preço. O preço vem como texto ("£51.77")."""
    mais_caro = livros[0]
    for livro in livros:
        if livro["preco"] > mais_caro["preco"]:
            mais_caro = livro
    return mais_caro


def ler_livros(caminho=CAMINHO_LIVROS):
    """Lê o CSV de livros e devolve uma lista de dicionários.

    Os valores vêm do jeito que estão no arquivo, ou seja, como texto:
    {"titulo": "Sharp Objects", "preco": "£47.82", "nota": "Four", ...}
    """
    livros = []
    with open(caminho, encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            livros.append(linha)
    return livros


def converter_preco(texto):
    """Converte um preço do site em número: "£51.77" -> 51.77"""
    return float(texto.replace("£", ""))


def converter_nota(texto):
    """Converte a nota escrita em inglês em número: "Three" -> 3"""
    if texto == "One":
        return 1
    elif texto == "Two":
        return 2
    elif texto == "Three":
        return 3
    elif texto == "Four":
        return 4
    elif texto == "Five":
        return 5
    else:
        return 0


def preparar_livros(linhas):
    """Recebe as linhas lidas do CSV e devolve os livros com preço e nota em número."""
    livros = []
    for linha in linhas:
        livro = {
            "titulo": linha["titulo"],
            "preco": converter_preco(linha["preco"]),
            "nota": converter_nota(linha["nota"]),
            "categoria": linha["categoria"],
            "url": linha["url"],
        }
        livros.append(livro)
    return livros


def carregar_livros(caminho=CAMINHO_LIVROS):
    """Lê o CSV e já devolve os livros prontos para usar."""
    return preparar_livros(ler_livros(caminho))

def carregar_favoritos():
    """Lê os favoritos e devolve um dicionário: {titulo: dados do favorito}."""
    favoritos = {}
    try:
        with open(CAMINHO_FAVORITOS, encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                favoritos[linha["titulo"]] = {
                    "preco": float(linha["preco"]),
                    "categoria": linha["categoria"],
                    "status": linha["status"],
                    "comentario": linha["comentario"],
                    }
    except FileNotFoundError:
        pass # Ainda não há favoritos: não é um erro
    return favoritos

def salvar_favorito(livro):
    """Acrescenta um livro no fim do arquivo de favoritos (modo "a")."""
    arquivo_ja_existia = CAMINHO_FAVORITOS.exists()
    with open(CAMINHO_FAVORITOS, "a", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS_FAVORITO)
        if not arquivo_ja_existia:
            escritor.writeheader()
        escritor.writerow({
            "titulo": livro["titulo"],
            "preco": livro["preco"],
            "categoria": livro["categoria"],
            "status": "Quero ler",
            "comentario": "",
            })

def gravar_favoritos(favoritos):
    """Reescreve o arquivo inteiro com os favoritos do dicionário (modo "w")."""
    with open(CAMINHO_FAVORITOS, "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS_FAVORITO)
        escritor.writeheader()
        for titulo, favorito in favoritos.items():
            escritor.writerow({
                "titulo": titulo,
                "preco": favorito["preco"],
                "categoria": favorito["categoria"],
                "status": favorito["status"],
                "comentario": favorito["comentario"],
            })


if __name__ == "__main__":
    # Só roda com "python dados.py". Quando o app faz "import dados", nada disto executa.
    print("Texto do CSV:  ", ler_livros()[0])
    print("Depois de preparar:", carregar_livros()[0])
