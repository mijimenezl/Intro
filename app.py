import streamlit as st 
from PIL import Image

st.title("Mi primera página")
st.header("mi primera chamba")
st.write("recuerdo el día que de la chamba me enamoré")

image = Image.open('The Dark Lord.png')
st.image(image, caption='the dark lord')

texto = st.text_input('Escribele algo', 'Este es mi texto')
st.write('El texto escirto es', texto)
