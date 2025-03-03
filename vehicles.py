import pandas as pd
import plotly.express as px
import streamlit as st

# cargas datos
car_data = pd.read_csv('vehicles_us.csv')

st.header('Vehicles')

# crear casillas de verificacion
show_histogram = st.checkbox('Mostrar histograma del odometro')
show_scatter = st.checkbox(
    'Mostrar grafico de dispersion (precio vs odometro)')

# mostrar histograma si la casilla esta marcada
if show_histogram:
    st.write(
        'Creacion de un histograma para el conjunto de datos de anuncios de ventas de coches')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)
