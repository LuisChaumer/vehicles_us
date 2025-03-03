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

if show_scatter:
    st.write('Creacion de un grafico de dispersion (Precio vs Odometro)')
    fig_scatter = px.scatter(
        car_data, x='odometer', y='price', title='Relacion entre odometro y precio')
    st.plotly_chart(fig_scatter, use_container_width=True)
