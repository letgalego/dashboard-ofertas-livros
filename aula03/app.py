"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st

import dados

def montar_tabela(livros):
    """Prepara as linhas que aparecem na tabela, com nomes de coluna amigáveis."""
    tabela = []
    for livro in livros:
        linha = {
            "Título": livro["titulo"],
            "Categoria": livro["categoria"],
            "Nota": livro["nota"] * "⭐",
            "Preço": f"£ {livro["preco"]:.2f}",
            "Faixa": classificar_preco(livro["preco"])
        }
        tabela.append(linha)
    return tabela

def classificar_preco(preco):
    """Classifica um preço em libras em uma faixa de texto."""
    if preco < 20:
        return "Barato"
    elif preco <= 40:
        return "Médio"
    else:
        return "Caro"

def contar_por_faixa(livros):
    """Conta quantos livros existem em cada faixa de preço: {"Caro": 403, ...}"""
    contagem = {}
    for livro in livros:
        faixa = classificar_preco(livro["preco"])
        if faixa in contagem:
            contagem[faixa] = contagem[faixa] + 1
        else:
            contagem[faixa] = 1

    return contagem

def buscar_por_titulo(livros, busca):
    """Devolve só os livros cujo título contém o texto buscado."""
    encontrados = []
    for livro in livros:
        if busca.lower().strip() in livro["titulo"].lower().strip():
            encontrados.append(livro)

    return encontrados

def listar_categorias(livros):
    """Devolve as categorias dos livros, sem repetição e em ordem alfabética."""
    categorias = []
    for livro in livros:
        if livro["categoria"] not in categorias:
            categorias.append(livro["categoria"])

    categorias.sort()
    return categorias

def filtrar_por_categoria(livros, categoria):
    """Devolve só os livros da categoria escolhida. Com "Todas", devolve todos."""
    if categoria == "Todas":
        return livros

    resultado = []
    for livro in livros:
        if livro["categoria"] == categoria:
            resultado.append(livro)

    return resultado

def main():
    st.set_page_config(page_title="Dashboard de Livros", page_icon="📚", layout="wide")
    st.title("📚 Dashboard de Livros")

    livros = dados.carregar_livros()

    col1, col2, col3, col4 = st.columns(4)
    qtd_livros = len(livros)
    col1.metric("Total de Livros", qtd_livros)

    preco_medio = dados.calcular_preco_medio(livros)
    col2.metric("Preço médio", f"£{preco_medio:.2f}")

    cinco_estrelas = dados.contar_cinco_estrelas(livros)
    col3.metric("Qtd. livros 5 Estrelas", cinco_estrelas)

    mais_caro = dados.encontrar_mais_caro(livros)
    col4.metric("Livro mais caro", f"£{mais_caro["preco"]}")
    col4.caption(mais_caro["titulo"])

    col_busca, col_categoria = st.columns(2)

    busca = col_busca.text_input("Buscar livros")
    categoria = col_categoria.selectbox("Filtrar por Categoria", ["Todas"] + listar_categorias(livros))

    livros_categoria = filtrar_por_categoria(livros, categoria)
    encontrados = buscar_por_titulo(livros_categoria, busca)

    qtd_livros = len(encontrados)

    if qtd_livros == 0:
        st.warning("Nenhum livro encontrado")
    else:
        st.write(f"Livros encontrados: {qtd_livros}")
        st.dataframe(montar_tabela(encontrados))

if __name__ == "__main__":
    main()