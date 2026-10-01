"""Leitura dos arquivos CSV do projeto."""

import csv
from pathlib import Path

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"


def ler_livros():
    """Lê o CSV de livros e devolve uma lista de dicionários.

    Os valores vêm do jeito que estão no arquivo, ou seja, como texto:
    {"titulo": "Sharp Objects", "preco": "£47.82", "nota": "Four", ...}
    """
    livros = []
    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha)
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo", error)

    return livros


def calcular_preco_medio(livros):
    """Soma os preços de todos os livros e divide pelo total.

    O preço vem como texto ("£51.77"): removemos o "£" e convertemos com float.
    """
    soma: float = 0
    for livro in livros:
        soma += livro["preco"]
    
    preco_medio: float = soma / len(livros)
    return preco_medio

def converter_preco(preco):
    return float(preco.replace("£", ""))

def converter_nota(nota):
    notas = ["One", "Two", "Three", "Four", "Five"]
    for nome in notas:
        if (nome == nota):
            return notas.index(nome) + 1


def contar_cinco_estrelas(livros):
    """Conta quantos livros têm a nota máxima. A nota vem como texto ("Five")."""
    contador: int = 0
    for livro in livros:
        if livro["nota"] == 5:
            contador += 1
    return contador


def encontrar_mais_caro(livros):
    """Devolve o livro de maior preço. O preço vem como texto ("£51.77")."""
    mais_caro = livros[0]
    for livro in livros:
        if livro["preco"] > mais_caro["preco"]:
            mais_caro = livro
    return mais_caro

def preparar_livros(livros):
    livrosConvertidos = []
    for livro in livros:
        livro = {
            "titulo": livro["titulo"],
            "preco": converter_preco(livro["preco"]),
            "categoria": livro["categoria"],
            "nota": converter_nota(livro["nota"]),
            "url": livro["url"]
        }
        livrosConvertidos.append(livro)
    return livrosConvertidos

def carregar_livros():
    return preparar_livros(ler_livros())

if __name__ == "__main__":
    preco_original = "£32.00"
    print(converter_preco(preco_original))
    nota = "One"
    print(converter_nota(nota))