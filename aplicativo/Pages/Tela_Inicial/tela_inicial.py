import streamlit as st
import datetime as dt


def tela_inicial():

    container = st.container(border=True)       
    
    container.title("           Sistema de Gerenciamento")
    container.image("aplicativo/images/logo.jpg",use_column_width="always")