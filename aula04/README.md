# Aula 4: Favoritos: escrita em arquivos e dicionários

## O que vimos hoje
- `st.tabs` para separar o app em abas e `st.button` para reagir a um clique
- Modos do `open`: `"w"` apaga e escreve, `"a"` acrescenta no fim
- `write` e `\n` para escrever em um arquivo de texto
- `csv.DictWriter`, `writeheader` e `writerow` para escrever um CSV
- `.keys()`, `.values()` e `.items()` para percorrer dicionários
- `d[chave] = valor`, `.update()` e `del` para alterar e apagar
- `copia = d` é o **mesmo** dicionário, e `d.copy()` é um dicionário **novo**
- Local × publicado: no Streamlit Cloud, o `favoritos.csv` some quando o app reinicia

## Como rodar
```powershell
.venv\Scripts\Activate.ps1
python aula04/teste_arquivos.py    # teste dos modos "w" e "a"
streamlit run aula04/app.py
```