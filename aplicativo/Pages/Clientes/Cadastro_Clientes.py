import streamlit as st
import pandas as pd
import numpy as np
import time as time
import datetime as dt
import openpyxl

# cache_data - obtem as informações dos arquivo e salva internamente, para que não haja necessidade de baixas as informações novamente;
# Só baixará novamente, quando uma informação for acrescentada


 
def cadastrar_cliente():
    # lista que será a base de dados para armazenar os clientes cadastrados
    input_clientes = []
    data_hoje = dt.datetime.today()

    # titulo da página
    st.title("Studio Ana Ferreira")
    # base onde estão os dados salvos
    df_clientes = pd.read_excel(r"C:\Users\joaoc\OneDrive\Documentos\GitHub\projeto_gerenciamento_salao\bases_salao\clientes_cadastrados.xlsx",sheet_name="clientes_cadastrados",engine="openpyxl")
    st.header("Cadastro de clientes 🙋‍♀️")
    
    with st.form("myform"):
        var_nome  = st.text_input("Nome:")
        var_nascimento = st.date_input("Data de nascimento",format= "DD/MM/YYYY")
        var_nascimento_convertido = f"{var_nascimento:%d/%m/%Y}"
        var_id = df_clientes["id_cliente"].max() + 1
        var_desde = f"{data_hoje:%d/%m/%Y}"
        submitted = st.form_submit_button("Salvar")
           
        if submitted:
            st.write("Nome do clinete:",var_nome)
            st.write("Data de nascimento:",var_nascimento_convertido)
            st.write("Cliente cadastrado em:",var_desde)
            input_clientes.append((var_id,var_nome,var_nascimento_convertido,var_desde))
            novo_cliente = pd.DataFrame(input_clientes,columns=["id_cliente",
                                                                "nome_cliente",
                                                                "data_nascimento",
                                                                "ativo_em"
                    ])
            atualizacao_clientes = pd.concat([df_clientes,novo_cliente],ignore_index=True,names=None)
            atualizacao_clientes.to_excel(r"C:\Users\joaoc\OneDrive\Documentos\GitHub\projeto_gerenciamento_salao\bases_salao\clientes_cadastrados.xlsx",sheet_name="clientes_cadastrados",index= False,index_label=False)
                    # base que será a banco de dados onde as informações serão salvas
            df_clientes = pd.read_excel(r"C:\Users\joaoc\OneDrive\Documentos\GitHub\projeto_gerenciamento_salao\bases_salao\clientes_cadastrados.xlsx",sheet_name="clientes_cadastrados",engine="openpyxl",index_col=0)
            st.success('Cliente cadastrado com sucesso!', icon="✅")

if __name__ == "__main.py":
    cadastrar_cliente()
                



