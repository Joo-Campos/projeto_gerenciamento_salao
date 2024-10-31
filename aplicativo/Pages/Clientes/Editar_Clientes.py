import streamlit as st
import pandas as pd
import datetime as dt
import openpyxl
@st.dialog("Editando cliente")
def editar_cliente(id_cliente):
    excel_path = r"C:\Users\joaoc\OneDrive\Documentos\GitHub\projeto_gerenciamento_salao\bases_salao\clientes_cadastrados.xlsx"
    df_clientes = pd.read_excel(excel_path,sheet_name="clientes_cadastrados",engine="openpyxl")
    


    nascimento_atual = df_clientes[df_clientes["id_cliente"] == id_cliente]["data_nascimento"].values[0]
    atualizar_nascimento = st.date_input(f"Data",format= "DD/MM/YYYY",value=pd.to_datetime(nascimento_atual))
    atualizar_nascimento_convertido = f"{atualizar_nascimento:%d/%m/%Y}"

    
    nome_atual = df_clientes[df_clientes["id_cliente"] == id_cliente]["nome_cliente"].values[0]
    atualizar_nome = st.text_input(label=f"Nome",value=nome_atual)
    botao_salar = st.button("Salvar")

    if botao_salar:
        df_clientes.loc[df_clientes["id_cliente"] == id_cliente,"data_nascimento"] = atualizar_nascimento_convertido
        df_clientes.loc[df_clientes["id_cliente"] == id_cliente,"nome_cliente"] = atualizar_nome
        df_clientes.to_excel(excel_path, sheet_name="clientes_cadastrados", engine="openpyxl", index=False)
        st.success("Alterações realizadas com sucesso",icon="✅")
        st.write(f"Nome alterado de: {nome_atual} para {atualizar_nome}")
        st.write(f"Data de nascimento alterada de: {nascimento_atual} para {atualizar_nascimento_convertido}")