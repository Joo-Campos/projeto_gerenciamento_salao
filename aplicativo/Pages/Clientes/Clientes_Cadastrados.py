import streamlit as st
import pandas as pd
import numpy as np
import time as time
import datetime as dt
import aplicativo.Pages.Clientes.Excluir_Clientes as deletar_clientes
import aplicativo.Pages.Clientes.Editar_Clientes as atualizar_clientes
import openpyxl

def visualizar_clientes():
            
            st.title("Studio - Ana Ferrreira")
            st.subheader("Clientes cadastrados")
            df_clientes = pd.read_excel(r"C:\Users\joaoc\OneDrive\Documentos\GitHub\projeto_gerenciamento_salao\bases_salao\clientes_cadastrados.xlsx",sheet_name="clientes_cadastrados",engine="openpyxl")
            criar_colunas= st.columns((2,4,3,3,3,3))
            lista_colunas = ["ID","Nome","Data de nascimento","Cadastrado em","",""] #array
            for colunas,cabeçalhos in zip(criar_colunas,lista_colunas): #zip está conectanto a criação das colunas com os nomes das colunas
                        colunas.write(cabeçalhos)
            
            for index, row in df_clientes.iterrows():
                  col1,col2,col3,col4,col5,col6 = st.columns((2,4,3,3,3,3))
                  col1.write(row["id_cliente"])
                  col2.write(row["nome_cliente"])
                  col3.write(row["data_nascimento"])
                  col4.write(row["ativo_em"])
                  espaco_btexcluir = col5.empty() # criando uma coluna vazia
                  apertar_excluir = espaco_btexcluir.button("Excuir",key="bt_excluir" + str(row["id_cliente"]), icon="🗑️")# na chave key foi se criada uma chave para cada botão.
                  espaco_btalterar = col6.empty() # criando uma coluna vazia
                  apertar_alterar = espaco_btalterar.button("Editar",key="bt_alterar" + str(row["id_cliente"]), icon="📝")
                   
                  if apertar_excluir:    
                        deletar_clientes.excluir_cliente(int(row["id_cliente"]))
                        st.rerun()
                  if apertar_alterar:
                        atualizar_clientes.editar_cliente(int(row["id_cliente"]))
                        

                  