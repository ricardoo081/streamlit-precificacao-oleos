import streamlit as st

st.set_page_config(layout="wide")

st.title("Matriz de Precificação dos Óleos - Visualização Online")

iframe_url = "https://inpasabr.sharepoint.com/sites/ComercialOleoMI/_layouts/15/Doc.aspx?sourcedoc=%7BCDEADB8C-1900-4AC6-8D8B-FEB3BC705A3A%7D&file=base_precificacao_oleos1.xlsx&action=embedview"

st.components.v1.iframe(iframe_url, height=900, scrolling=True)
