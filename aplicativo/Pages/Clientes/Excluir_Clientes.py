import streamlit as st
import pandas as pd
import numpy as np
import time as time
import datetime as dt
import openpyxl 

def excluir_cliente(id_cliente):
        excel_path = r"C:\Users\joaoc\OneDrive\Documentos\GitHub\projeto_gerenciamento_salao\bases_salao\clientes_cadastrados.xlsx"
        df_clientes = pd.read_excel(excel_path,sheet_name="clientes_cadastrados",engine="openpyxl")
        localizar = df_clientes.index[df_clientes["id_cliente"] == id_cliente ]
        remover  =   df_clientes.drop(axis= 0, index= localizar)
        remover.to_excel(excel_path,sheet_name="clientes_cadastrados",index= False,index_label=False)