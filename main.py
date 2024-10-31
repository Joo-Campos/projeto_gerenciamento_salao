import streamlit as st
import pandas as pd
import time as time
import datetime as dt
import aplicativo.Pages.Clientes.Cadastro_Clientes as cadastro_clientes
import aplicativo.Pages.Clientes.Clientes_Cadastrados as cadastrados_clientes
import aplicativo.Pages.Atendimentos.Atendimentos_Realizados as atendimentos
import aplicativo.Pages.Tela_Inicial.tela_inicial as tela_inicial
import aplicativo.Pages.Movimentos.Transacoes_Financeiras as transacoes


hoje = dt.datetime.today()
hoje_mod = f"{hoje:%d/%m/%Y}"






      #principal = st.button(label="Tela Principal",key=f'tela_principal_{st.session_state.counter}')
      #view = st.button(label="Clientes cadastrados",key=f'tela_clientes_{st.session_state.counter}')
      #cadastrar_clientes = st.button(label="Cadastrar Clientes",key=f'tela_cadastro_{st.session_state.counter}')
with st.sidebar:
    menu = st.header("Clientes")
    escolha_pagina = st.radio("-",options=[
                                            "Tela Inicial 🏠",
                                            "Cadastrar Cliente ➕",
                                            "Clientes Cadastrados 📄",
                                            "Atendimentos 🚿",
                                            "Movimentações 💵"])
    

        
        
    

if escolha_pagina == "Cadastrar Cliente ➕":
        cadastro_clientes.cadastrar_cliente()
        

elif escolha_pagina == "Clientes Cadastrados 📄":
        cadastrados_clientes.visualizar_clientes()

elif escolha_pagina == "Atendimentos 🚿":
       atendimentos.atedimentos_realizados()

elif escolha_pagina == "Tela Inicial 🏠":
       tela_inicial.tela_inicial()

elif escolha_pagina == "Movimentações 💵":
       transacoes.movimentacoes()

       
       
        
     




