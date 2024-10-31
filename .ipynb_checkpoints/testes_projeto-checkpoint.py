
import pandas as pd # type: ignore
import datetime as dt

# lista que será a base de dados para armazenar os clientes cadastrados
base_clientes = []

# base que será a banco de dados onde as informações serão salvas
df_clientes = pd.read_excel(r"C:\Users\joaoc\OneDrive\projetos do salão\bd_salao.xlsx",sheet_name="clientes_cadastrados",engine="openpyxl")

class Atualizar_Cadastro():
    def data_nascimento():
        var_nascimento = input("Insira a data de nascimento: ")  
        df_clientes.loc[df_clientes["nome_cliente"] == "Joao Campos","data_nascimento"] = var_nascimento
        print(df_clientes)
    def nome_cliente():
        var_nome = input("Insira o nome do cliente: ")
        df_clientes.loc[df_clientes["nome_cliente"] == "Joao Campos","nome_cliente"] = var_nome
        print(df_clientes)
    def remover_cliente():
        localizar_indice = df_clientes.index[df_clientes["nome_cliente"] == "Ana Clara Ferreira"]
        df_clientes.drop(axis= 0, index= localizar_indice)
        print(df_clientes)
# base que será a banco de dados onde as informações serão salvas
df_clientes = pd.read_excel(r"C:\Users\joaoc\OneDrive\projetos do salão\bd_salao.xlsx",sheet_name="clientes_cadastrados",engine="openpyxl")

#print(df_clientes)

#data = dt.datetime.today()

#print(data)

#data_formatada = f"{data:%d/%m/%y}"

#print(data_formatada)

#data_str = "11/12/2024"

#data_str_formatada = dt.datetime.strptime(data_str,"%d/%m/%Y")
#data_final = f"{data_str_formatada:%d/%m/%Y}"

#print(data_final)

#localizar = df_clientes.index[df_clientes["nome_cliente"] == "Ana Clara Ferreira"]

#remover  =   df_clientes.drop(axis= 0, index= localizar)

#print(remover)

Atualizar_Cadastro.nome_cliente()