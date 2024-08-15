import streamlit as st 
from PIL import Image

st.title("Mi primera página")
st.header("mi primera chamba")
st.write("recuerdo el día que de la chamba me enamoré")

image = Image.open('The Dark Lord.png')
st.image(image, caption='the dark lord')

texto = st.text_input('Escribele algo', 'Este es mi texto')
st.write('El texto escirto es', texto)

st.subheader ("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Esta es la primera columna")
  st.write("Darth Vader es un buen villano")
  resp = st.checkbox ('Estoy de acuerdo')
  if resp: 
    st.write('Correcto!')

with col2: 
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Quien es Darth Vader", ('Anakin', 'Obiwan', 'Dooku'))
  if modo == 'Anakin':
    st.write('Correcto, Darth Vader es el caballero Jedi Anakin Skywalker')
  if modo == 'Obiwan':
    st.write('Darth Vader es el caballero Jedi Anakin Skywalker')
  if modo == 'Dooku':
    st.write('Darth Vader es el caballero Jedi Anakin Skywalker')


st.subheader("Uso de botones")
if st.button('Presiona el boton'):
  st.write(' If you're not with me, you're my enemy.')
else: 
  st.write('Anakin, my allegiance is to the Republic ... to democracy.)
