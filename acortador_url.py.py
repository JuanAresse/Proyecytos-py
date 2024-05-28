import pyshorteners
import streamlit as st

def acortador_url(url):
    a = pyshorteners.Shortener()
    url_recortada = a.tinyurl.short(url)
    return url_recortada

st.set_page_config(page_title="Acortador de URL", layout="centered")
st.title("Acortador de URL")
url = st.text_input("Ingresa la URL que desea acortar: ")
if st.button("Generar nueva URL: "):
    st.write("URL acortada: ", acortador_url(url))