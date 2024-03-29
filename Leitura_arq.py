import streamlit as st
import pandas as pd
import openpyxl

def analisar_dados(arquivo):
    # Carrega o arquivo em um DataFrame do pandas
    df = pd.read_excel(arquivo)
    
    # Verifica a quantidade de valores duplicados nas colunas item e model
    qtd_duplicados = df[['model_id']].duplicated().sum()
    st.write(f'{qtd_duplicados}, Valores duplicados na coluna model_id')
       
    # Verifica se a coluna "promo" contém apenas números inteiros
    if pd.api.types.is_integer_dtype(df["promo_stock"]):
        st.write("promo_stock ok.")
    else:
        st.write("Coluna 'promo_stock' contém valores NÃO inteiros (ex:2,5)")
    
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
        st.write("Data ok.")
    
        # Verifica se a coluna "preco_negociado" contém valores menores ou iguais a zero
    if (df["preco_negociado"] == 0).any():
        st.write("Coluna 'preco_negociado' contém valores = zero!!")
   


# In[ ]:


# Cria um componente para upload de arquivo
arquivo = st.file_uploader('Selecione o arquivo .xlsx', type='xlsx')

# Verifica se um arquivo foi carregado e, se sim, executa a análise de dados
if arquivo is not None:
    analisar_dados(arquivo)

