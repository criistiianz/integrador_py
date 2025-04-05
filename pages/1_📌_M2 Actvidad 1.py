import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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

st.header("Solución")

st.markdown("""
    <div style="background-color:#f9f9f9; padding:20px; border-radius:10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
""", unsafe_allow_html=True)

# Título y descripción
st.title("📊 Creación de DataFrames")
st.write("Esta actividad tiene como objetivo practicar la creación de DataFrames desde diferentes fuentes de datos utilizando Pandas.")

# DataFrame desde un diccionario
st.write("📚 DataFrame de Libros")

libros = {
    "título": ["Cien años de soledad", "1984", "Don Quijote", "El Principito"],
    "autor": ["Gabriel García Márquez", "George Orwell", "Miguel de Cervantes", "Antoine de Saint-Exupéry"],
    "año de publicación": [1967, 1949, 1605, 1943],
    "género": ["Realismo mágico", "Distopía", "Novela", "Fábula"]
}

df_libros = pd.DataFrame(libros)
st.dataframe(df_libros)

# DataFrame desde una lista de diccionarios
st.write("🌆 DataFrame de Ciudades")

ciudades = [
    {"nombre": "Bogotá", "población": 7743955, "país": "Colombia"},
    {"nombre": "Ciudad de México", "población": 9209944, "país": "México"},
    {"nombre": "Buenos Aires", "población": 2890151, "país": "Argentina"},
    {"nombre": "Lima", "población": 9674755, "país": "Perú"}
]

df_ciudades = pd.DataFrame(ciudades)
st.dataframe(df_ciudades)

# DataFrame desde una lista de listas
st.write("🎓 ### DataFrame de Estudiantes")

datos_estudiantes = [
    ["Ana", 20, "Matemáticas"],
    ["Luis", 22, "Ingeniería"],
    ["María", 19, "Literatura"],
    ["Carlos", 21, "Biología"]
]

df_estudiantes = pd.DataFrame(datos_estudiantes, columns=["Nombre", "Edad", "Carrera"])
st.dataframe(df_estudiantes)

# DataFrame desde Series
st.write("👩‍💼 DataFrame desde Series")

nombres = pd.Series(["Laura", "Jorge", "Valentina"])
edades = pd.Series([23, 25, 22])
profesiones = pd.Series(["Diseñadora", "Arquitecto", "Psicóloga"])

df_series = pd.DataFrame({"Nombre": nombres, "Edad": edades, "Profesión": profesiones})
st.dataframe(df_series)

st.markdown("</div>", unsafe_allow_html=True)
