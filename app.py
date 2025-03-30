import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Opción 1: Botones para construir gráficos
st.write("### Visualización de Datos de Vehículos")
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

if scatter_button:
    st.write(
        'Creación de un gráfico de dispersión entre el odómetro y el precio del vehículo')
    fig_scatter = px.scatter(car_data, x="odometer",
                             y="price", title="Kilometraje vs. Precio")
    st.plotly_chart(fig_scatter, use_container_width=True)
