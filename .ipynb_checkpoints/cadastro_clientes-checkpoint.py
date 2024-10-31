import pandas as pd # type: ignore
import datetime as dt

# lista que será a base de dados para armazenar os clientes cadastrados
input_clientes = []
data_hoje = dt.datetime.today()

# base que será a banco de dados onde as informações serão salvas
df_clientes = pd.read_excel(r"C:\Users\joaoc\OneDrive\projetos do salão\bd_salao.xlsx",sheet_name="clientes_cadastrados",engine="openpyxl")

print("----------- Seja bem-vindo ----------\n")


def cadastro():
    var_nome = input("Insira seu nome: ")
    var_nascimento = input("Insira sua data de nasciento: ")  # Convertemos para inteiro aqui
    var_converter_date = dt.datetime.strptime(var_nascimento,"%d/%m/%Y") #convertendo da data que é string para date
    var_nascimento_convertido = f"{var_converter_date:%d/%m/%Y}" #formatando a data para o formato pt-br
    var_desde = f"{data_hoje:%d/%m/%Y}"
    var_id = df_clientes. shape[0] + len(input_clientes) + 1

    input_clientes.append((var_id,var_nome,var_nascimento_convertido,var_desde))
    print(var_nome, "seu cadastro foi realizado com sucesso. \n Obrigado!!! \n \n \n")
    print(input_clientes)
        
    novo_cliente = pd.DataFrame(input_clientes,columns=["id_cliente",
                                                       "nome_cliente",
                                                       "data_nascimento",
                                                       "ativo_em"
    ])

    atualizacao_clientes = pd.concat([df_clientes,novo_cliente],ignore_index=True,names=None)
    atualizacao_clientes.to_excel(r"C:\Users\joaoc\OneDrive\projetos do salão\bd_salao.xlsx",sheet_name="clientes_cadastrados",index= False,index_label=False)

def banco_cadastros():
    df_cadastrados = pd.DataFrame(df_clientes)
    print(df_cadastrados)

#def banco_cadastros():
        #print(var_nome2, var_idade2)

# Aqui, alteramos para comparar com a string "1" ao invés do número 1
controle = input("Digite 1 para continuar, 2 para acessar os cadastros ou pressione Enter para sair: ")

# O loop continuará enquanto o usuário pressionar "1"
while controle == "1":
    cadastro()
    controle = input("Digite 1 para continuar, 2 para acessar os cadastros ou pressione Enter para sair: ")
while controle == "2":
    banco_cadastros()
    controle = input("Digite 1 para continuar, 2 para acessar os cadastros ou pressione Enter para sair: ")

# Se o usuário pressionar Enter, o programa continuará e mostrará a mensagem de saída
if controle == "":
    input("Pressione <enter> para sair")