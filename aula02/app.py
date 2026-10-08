"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st

import dados

def montar_tabela(livros):
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
    if preco < 20:
        return "Barato"
    elif preco <= 40:
        return "Médio"
    else:
        return "Caro"

def contar_por_faixa(livros):
    contador = {}
    for livro in livros:
        faixa = classificar_preco(livro["preco"])
        if faixa in contador:
            contador[faixa] = contador[faixa] + 1
        else:
            contador[faixa] = 1
    return contador

def buscar_por_titulo(livros, busca):
    livros_encontrados = []
    for livro in livros:
        if busca.lower() in livro["titulo"].lower():
            livros_encontrados.append(livro)
    
    return livros_encontrados

def listar_categorias(livros):
    categorias = []
    for livro in livros:
        if livro["categoria"] not in categorias:
            categorias.append(livro["categoria"])
    
    categorias.sort()

    return categorias

def filtrar_por_categoria(livros, categoria):
    if categoria == "Todas":
        return livros

    livros_filtrados = []
    for livro in livros:
        if livro["categoria"] == categoria:
            livros_filtrados.append(livro)
    return livros_filtrados


def main():
    st.set_page_config(page_title="Dashboard de Livros", page_icon="📚", layout="wide")
    st.title("📚 Dashboard de Livros")

    livros = dados.carregar_livros()
    tabela = montar_tabela(livros)
    contador_classificacao = contar_por_faixa(livros)

    col1, col2, col3, col4 = st.columns(4)
    qtd_livros = len(livros)
    col1.metric("Total de Livros", qtd_livros)

    preco_medio = dados.calcular_preco_medio(livros)
    col2.metric("Preço médio", f"£{preco_medio:.2f}")

    cinco_estrelas = dados.contar_cinco_estrelas(livros)
    col3.metric("Qtd. livros 5 Estrelas", cinco_estrelas)
    col3.caption("Teste")

    mais_caro = dados.encontrar_mais_caro(livros)
    col4.metric("Livro mais caro", f"£{mais_caro["preco"]}")
    col4.caption(mais_caro["titulo"])

    col_busca, col_categoria = st.columns(2)

    busca_titulo = col_busca.text_input(label="🔎 Busca pelo título", type="search")
    opcao_categoria = col_categoria.selectbox("Filtrar por categoria", ["Todas"] + listar_categorias(livros))

    livros_categoria = filtrar_por_categoria(livros, opcao_categoria)
    livros_busca = dados.buscar_por_titulo(livros_categoria, busca_titulo)

    # se a busca por titulo não estiver vazia ele pega a string da busca e procura livros com essa string
    if (len(livros_busca) == 0):
        st.warning("Nenhum livro encontrado")
    else:
        st.caption(f"{len(livros_busca)} livros encontrados")
        st.dataframe(montar_tabela(livros_busca))

    st.dataframe(contador_classificacao)



if __name__ == "__main__":
    main()
