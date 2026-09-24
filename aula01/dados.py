"""Leitura dos arquivos CSV do projeto.
"""

from pathlib import Path
import csv

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

catalogo = []

def calcular_preco_medio(livros):
    if not livros:
        return 0.0
    soma: float = 0
    for livro in livros:
        preco_original: str = livro["preco"]
        preco_original_limpo: str = preco_original.replace("£", "")
        preco_num: float = float(preco_original_limpo)
        soma += preco_num
    preco_medio = soma / len(livros)
    return preco_medio

def contar_cinco_estrelas(livros):
    contador = 0
    for livro in livros:
        if livro["nota"] == "Five":
            contador += 1
    return contador

def ler_livros_v3(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            print(linha["titulo"])

def ler_livros_v2(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        print(arquivo.read())

def ler_livros(caminho):
    arquivo = None
    livros = []
    try:
        arquivo = open(caminho, "r", encoding="utf-8")
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            livros.append(linha)
    except FileNotFoundError:
        print("Ocorreu um erro na leitura do arquivo!")
    except Exception as error:
        print("Ocorreu um erro inesperado:", error)
    finally:
        if arquivo is not None:
            arquivo.close()
    return livros

def livro_mais_caro(livros):
    nome_livro = ""
    preco_livro = 0
    for livro in livros:
        preco_original: str = livro["preco"]
        preco_original_limpo: str = preco_original.replace("£", "")
        preco_num: float = float(preco_original_limpo)
        if (preco_num > preco_livro):
            preco_livro = preco_num
            nome_livro = livro["titulo"]

    return nome_livro, preco_livro

if __name__ == "__main__":
    catalogo = ler_livros(CAMINHO_LIVROS)
    print(f"A quantidade de livros eh {len(catalogo)}")
    print(calcular_preco_medio(catalogo))