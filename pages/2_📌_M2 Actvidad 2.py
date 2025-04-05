import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")
st.title("EXPLORACION DE DATOS CON PANDAS Y STREAMLIT")
st.header("Solución")

df = pd.read_csv('integrador\static\estudiantes_colombia.csv')
st.dataframe(df)

st.title("LAS PRIMERAS 5 FILAS")
st.dataframe(df.head())

st.title("las ultimas 5 FILAS")
st.dataframe(df.tail())

st.title("MOSTRAR UN INFORME CON .INFO()")
st.write(df.info())

st.title("MOSTRAR LAS ESTADISTICAS BASICAS CON .describe()")
st.write(df.describe()) 

st.title("COLUMNAS ESPECIFICAS ")
st.write(df[['nombre', 'edad', 'promedio']])

st.title("FILTRAR ESTUDIANTES CON PREMEDIO MAYOR POR EL USUARIO  UTILIZANDO SLIDER")
promedio_usuario = st.slider("Promedio", min_value=0, max_value=100, value=75)