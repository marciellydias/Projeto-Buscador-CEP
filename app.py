import streamlit as st
from ferramentas import busca_cep
import pandas as pd


st.sidebar.image("logo.png")
st.sidebar.title("CEP Marcielly 💕")
cep = st.sidebar.text_input("Digite o CEP que deseja buscar: ")

if st.sidebar.button("Buscar"):
    dados = busca_cep(cep)
    st.title(f"{dados.get("city")},{dados.get("state")}")
    st.subheader(dados.get("address"))
    lat = float(dados.get("lat"))
    lng = float(dados.get("lng"))
    coordenadas = pd.DataFrame({"latitude":[lat], "longitude":[lng]})
    st.map(coordenadas, zoom=13)
    