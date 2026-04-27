import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.header("Análisis de anuncios de venta de vehículos en EE. UU.")
st.write("Esta aplicación muestra un dashboard dinámico con Python, Streamlit y Plotly.")

df = pd.read_csv("vehicles_us.csv")

hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Histograma de la columna odometer")

    fig_hist = go.Figure(data=[go.Histogram(x=df["odometer"])])
    fig_hist.update_layout(
        title_text="Distribución del odómetro",
        xaxis_title="Odómetro",
        yaxis_title="Frecuencia",
    )

    st.plotly_chart(fig_hist, use_container_width=True)

scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Gráfico de dispersión: odómetro vs precio")

    fig_scatter = go.Figure(
        data=[
            go.Scatter(
                x=df["odometer"],
                y=df["price"],
                mode="markers",
            )
        ]
    )

    fig_scatter.update_layout(
        title_text="Relación entre odómetro y precio",
        xaxis_title="Odómetro",
        yaxis_title="Precio",
    )

    st.plotly_chart(fig_scatter, use_container_width=True)
