import streamlit as st
import pandas as pd
import datetime

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

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

df = pd.read_csv("integrador\static\datos.csv", parse_dates=['fecha_nacimiento'])
df_nuevo = df.copy()

st.title("🔍 Aplicación de Filtros Dinámicos - CRM de Ventas")
st.sidebar.title("🔧 Filtros")

# 1. Filtro por rango de edad 
if st.sidebar.checkbox("Filtrar por rango de edad"):
    edad_min, edad_max = st.sidebar.slider("Selecciona el rango de edad", 15, 75, (20, 40))
    df_nuevo = df_nuevo[df_nuevo['edad'].between(edad_min, edad_max)]

# 2. Filtro por municipios específicos
if st.sidebar.checkbox("Filtrar por municipios"):
    municipios = ['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja', 'Manizales', 'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida']
    municipios_seleccionados = st.sidebar.multiselect("Selecciona los municipios", municipios)
    if municipios_seleccionados:
        df_nuevo = df_nuevo[df_nuevo['municipio'].isin(municipios_seleccionados)]

# 3. Filtro por ingreso mensual mínimo
if st.sidebar.checkbox("Filtrar por ingreso mensual mínimo"):
    ingreso_min = st.sidebar.slider("Ingreso mensual mínimo (COP)", 800000, 12000000, 2000000, step=100000)
    df_nuevo = df_nuevo[df_nuevo['ingreso_mensual'] > ingreso_min]

# 4. Filtro por ocupación
if st.sidebar.checkbox("Filtrar por ocupación"):
    ocupaciones = ['Estudiante', 'Docente', 'Comerciante', 'Agricultor', 'Ingeniero', 'Médico', 'Desempleado', 'Pensionado', 'Emprendedora', 'Obrera']
    ocupaciones_seleccionadas = st.sidebar.multiselect("Selecciona las ocupaciones", ocupaciones)
    if ocupaciones_seleccionadas:
        df_nuevo = df_nuevo[df_nuevo['ocupacion'].isin(ocupaciones_seleccionadas)]

# 5. Filtro por tipo de vivienda no propia
if st.sidebar.checkbox("Filtrar personas sin vivienda propia"):
    df_nuevo = df_nuevo[~(df_nuevo['tipo_vivienda'] == 'Propia')]

# 6. Filtro por nombres que contienen una cadena
if st.sidebar.checkbox("Filtrar por nombre"):
    cadena = st.sidebar.text_input("Texto contenido en el nombre")
    if cadena:
        df_nuevo = df_nuevo[df_nuevo['nombre_completo'].str.contains(cadena, case=False, na=False)]

# 7. Filtro por año de nacimiento
if st.sidebar.checkbox("Filtrar por año de nacimiento"):
    anio = st.sidebar.selectbox("Selecciona el año", list(range(1949, 2010)))
    df_nuevo = df_nuevo[df_nuevo['fecha_nacimiento'].dt.year == anio]

# 8. Filtro por acceso a internet
if st.sidebar.checkbox("Filtrar por acceso a internet"):
    acceso = st.sidebar.radio("Tiene acceso a internet:", ["Sí", "No"])
    valor = True if acceso == "Sí" else False
    df_nuevo = df_nuevo[df_nuevo['acceso_internet'] == valor]

# 9. Filtro por ingresos nulos
if st.sidebar.checkbox("Filtrar por ingresos nulos"):
    df_nuevo = df_nuevo[df_nuevo['ingreso_mensual'].isnull()]

# 10. Filtro por rango de fechas de nacimiento
if st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento"):
    fecha_inicio = st.sidebar.date_input("Fecha de inicio", datetime.date(1949, 1, 1))
    fecha_fin = st.sidebar.date_input("Fecha de fin", datetime.date(2009, 12, 31))
    df_nuevo = df_nuevo[df_nuevo['fecha_nacimiento'].between(pd.to_datetime(fecha_inicio), pd.to_datetime(fecha_fin))]

st.subheader("Resultado de los filtros")
st.dataframe(df_nuevo, use_container_width=True)

st.caption("Total de registros encontrados: {}".format(len(df_nuevo)))
