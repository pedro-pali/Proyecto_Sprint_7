import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header("Tablero interactivo de datos de vehiculos")

hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir un diagrama de dispersion')
 
if build_scatter:
    st.write('Construyendo un grafico de dispercion')

    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)