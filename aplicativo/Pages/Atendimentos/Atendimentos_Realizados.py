import streamlit as st
import pandas as pd
import openpyxl

def atedimentos_realizados():
    atendimentos = r"C:\Users\joaoc\OneDrive\Documentos\GitHub\projeto_gerenciamento_salao\bases_salao\atendimentos_realizados.xlsx"
    df_atendimentos = pd.read_excel(atendimentos,sheet_name="atendimentos_realizados",engine="openpyxl")
    clientes = r"C:\Users\joaoc\OneDrive\Documentos\GitHub\projeto_gerenciamento_salao\bases_salao\clientes_cadastrados.xlsx"
    df_clientes = pd.read_excel(clientes,sheet_name="clientes_cadastrados",engine="openpyxl")
    clientes_cadastrados = df_clientes["nome_cliente"].unique()
    st.title("Atendimentos realizados")

    input_atendimentos = []

    with st.form("meus_atendimentos"):
        
         # cliente_atendido
        nome_atendido = st.selectbox(label=f"**Cliente**",options=clientes_cadastrados)
        #id_atendimento
        id_verificacao = df_atendimentos["id_atendimento"].empty

        if id_verificacao == True:
            id_atendimento = 1
        else:
            id_atendimento = df_atendimentos["id_atendimento"].max() + 1
        # procedimento_realizado
        procedimento_realizado = st.selectbox(label="Qual procedimento?",options=[
                                                                                    "Progressiva com formol",
                                                                                    "Progressiva sem formol",
                                                                                    "Reconstrução",
                                                                                    "Hidratação",
                                                                                    "Corte",
                                                                                    "Escova",
                                                                                    "Botox",
                                                                                    "Pintura",

                                                                                    ])
        # data_atendimento
        data_atendimento = st.date_input(label="Data do atendimento",format="DD/MM/YYYY")
        data_atendimento_formatado = f"{data_atendimento:%d/%m/%Y}"
        # valor_serviço	
        valor_servico = float(st.text_input("Valor R$",value=0))
        st.warning(f"**Para valores decimais, favor, colocar (.) ao invés de (,)**!")
        valor_servico_convertido = f"{valor_servico:.2f}"
        # forma_pagamento
        options = ["Dinheiro", "Crédito", "Débito","Pix"]
        forma_pagamento = st.selectbox(label="Forma de pagamento",options=options)


        
        
        submit_form = st.form_submit_button(f"**Salvar** 💾") 
        if submit_form:     
            

                    col1,col2,col3,col4,col5 = st.columns((2,2,2,2,2))

                    with col1:
                        st.write(f"Cliente: {nome_atendido}")

                    with col2:
                        st.write(f"Procedimento: {procedimento_realizado}")
                    
                    with col3:
                        st.write(f"Data: {data_atendimento_formatado}")
                    
                    with col4:
                        st.write(f"Valor R$: {valor_servico_convertido}")
                    
                    with col5:
                        st.write(f"Forma Pagamento: {forma_pagamento}")
                    st.success("Muito bom! Realizamos mais um atendimento! 🚀")
                    st.balloons()
                    
                    input_atendimentos.append((id_atendimento,
                                            procedimento_realizado,
                                            data_atendimento_formatado,
                                            nome_atendido,
                                            valor_servico,
                                            forma_pagamento))
                    
                    atendimento_feito = pd.DataFrame(input_atendimentos,columns=
                                                                                ["id_atendimento",
                                                                                "procedimento_realizado",
                                                                                "data_atendimento",
                                                                                "cliente_atendido",
                                                                                "valor_serviço",
                                                                                "forma_pagamento"
                                                                                ])
                    atualizacao_atendimentos = pd.concat([df_atendimentos,atendimento_feito],ignore_index=True,names=None)
                    atualizacao_atendimentos.to_excel(atendimentos,sheet_name="atendimentos_realizados",index= False,index_label=False)
                    df_atendimentos = pd.read_excel(atendimentos,sheet_name="atendimentos_realizados",engine="openpyxl")
