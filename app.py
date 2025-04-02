import streamlit as st
from PIL import Image
import requests
import streamlit_lottie as st_lottie

st.set_page_config(page_title="stone cold steve austin",page_icon="🖕",layout="wide")
email_contact="emaildecontacto@hotmail.com"

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

css_load("style/style.css")


url="https://lottie.host/747a68d0-a65b-417b-9d89-a035930410c0/WHmZD2Hf6J.lottie"
def load_lottie(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#introduccion

with st.container():
    st.write("---")
    text_column, animation_column=st.columns(2)
    with text_column:
        st.header("Pagina dedicada a Stone cold Steve Austin")
        st.title("creamos soluciones para acelearar tu negocio")
        st.write(
                "Somos unos apasionados de la tecnología y la innovación, especializados en el sector de la digitalización y automatización de negocios. Nos gusta crear soluciones para resolver problemas y mejorar procesos."
        )
        st.write("[Saber mas >](https://www.google.com)")

    with animation_column:
        st.empty()

#servicios

with st.container():
    st.write("---")
    st.header("servicios 🖕")
    st.write("##")
    image_column,text_column = st.columns((1,2))
    with image_column:
        image = Image.open("imagenes/stone_cold.jpeg")
        st.image(image,use_container_width=True)
    with text_column:
        st.subheader("Disenio de aplicaiones")
        st.write(
            """
            Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarios.
            """
        )
        st.write("[Ver servicios >](https://www.google.com)")

#contacto
with st.container():
    st.write("---")
    st.header("Contact con nostros 🖕")
    st.write("##")
    #este formulario fue sacado directamente de internet, de un
    contact_form = f"""
    <form action="https://formsubmit.co/{email_contact}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Tu nombre" required>
        <input type="email" name="email" placeholder="Tu email" required>
        <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """

    left_column, right_column =st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()