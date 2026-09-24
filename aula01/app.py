"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados

st.set_page_config(layout="wide")
st.title("📚 Dashboard de Livros")
st.write("Se você está vendo esta página, o seu ambiente está pronto! 🎉")

col1, col2, col3, col4 = st.columns(4)

livros = dados.ler_livros(dados.CAMINHO_LIVROS)
qtd_livros = len(livros)

preco_medio = dados.calcular_preco_medio(livros)

qtd_cinco_estrelas = dados.contar_cinco_estrelas(livros)

livro_mais_caro, preco_mais_caro = dados.livro_mais_caro(livros)

col1.metric(label="Total de livros:", value=qtd_livros)
col2.metric(label="Preco medio", value=f"£{preco_medio:.2f}")
col3.metric (label="Livros com cinco estrelas", value=qtd_cinco_estrelas)
col4.metric (label="Livro mais caro", value=f"£{preco_mais_caro}", delta=livro_mais_caro)

st.dataframe(livros)