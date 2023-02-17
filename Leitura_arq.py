import openpyxl
import streamlit as st
import pandas as pd

def analisar_dados(arquivo):
    # Carrega o arquivo em um DataFrame do pandas
    df = pd.read_excel(arquivo)
    
    # Verifica a quantidade de valores duplicados nas colunas item e model
    qtd_duplicados = df[['model_id']].duplicated().sum()
    st.write(f'{qtd_duplicados}, Valores duplicados na coluna model')
       
    # Verifica se a coluna "promo" contém apenas números inteiros
    if pd.api.types.is_integer_dtype(df["promo_stock"]):
        st.write("Todos os valores da coluna 'promo_stock' são inteiros.")
    else:
        st.write("A coluna 'promo_stock' contém valores não inteiros.")
    
    # Verifica se as colunas "start_date" e "end_date" estão no formato correto
    date_cols = ["start_date", "end_date"]
    date_format = "%Y/%m/%d"
    n_dates_incorrect = 0
    for col in date_cols:
        n_incorrect = sum(~pd.to_datetime(df[col], format=date_format, errors="coerce").notnull())
        n_dates_incorrect += n_incorrect
        if n_incorrect > 0:
            st.write(f"{n_incorrect} valores na coluna {col} não está no formato correto.")
    if n_dates_incorrect == 0:
        st.write("Todas as datas estão no formato correto.")
    
        # Verifica se a coluna "preco_negociado" contém valores menores ou iguais a zero
    if (df["preco_negociado"] == 0).any():
        st.write("A coluna 'preco_negociado' contém valores iguais ou menores que zero!!.")
   


# In[ ]:


# Cria um componente para upload de arquivo
arquivo = st.file_uploader('Selecione o arquivo .xlsx', type='xlsx')

# Verifica se um arquivo foi carregado e, se sim, executa a análise de dados
if arquivo is not None:
    analisar_dados(arquivo)

