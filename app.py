import streamlit as st
import pandas as pd
import plotly.graph_objects as go


# Configuración básica de la app
st.header("Análisis de anuncios de venta de vehículos en EE. UU.")
st.write("Essta Aplicación muestra un DAsboard dinámico con python")

# Cargar Datos
ruta = r"C:\Users\diego\OneDrive\Desktop\Triple_Ten\intro_ml\Proyecto_1_sprint_7\vehicles_us.csv"

df = pd.read_csv(ruta)

# Botón para Histgrama
hist_button = st.button("Construir Histograma")

if hist_button:
    st.write("Histograma de la columna odometer")
    fig_hist = go.Figure(data=[go.Histogram(x=df["odometer"])])
    fig_hist.update_layout(
        title_text="Distribución del odómetro",
        xaxis_title="Odómetro",
        yaxis_title="Frecuencia"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para gráfico de dispersión
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Gráfico de dispersión: odómetro vs precio")
    fig_scatter = go.Figure(
        data=[
            go.Scatter(
                x=df["odometer"],
                y=df["price"],
                mode="markers"
            )
        ]
    )
    fig_scatter.update_layout(
        title_text="Relación entre odómetro y precio",
        xaxis_title="Odómetro",
        yaxis_title="Precio"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
