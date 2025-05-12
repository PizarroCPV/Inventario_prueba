import streamlit as st
import pandas as pd

df = pd.read_csv("/Inventario_prueba/BD_TALLER_PANOL.csv", sep=";")

# Título principal
st.title("Sistema Principal de Control")

# Menú lateral para navegación
menu = st.sidebar.selectbox("Selecciona una sección", ["Inicio", "Inventario", "Solicitudes", "Reportes"])

# Lógica para mostrar cada subventana
if menu == "Inicio":
    st.header("Página de Inicio")
    st.write("Bienvenido al sistema de control de inventario.")

elif menu == "Inventario":
    st.header("Gestión de Inventario")
    st.text("Lista de materiales actualización 2024")
    st.dataframe(df)
    # Aquí podrías agregar carga desde Excel, lectura de códigos de barras, etc.
    st.write("Aquí puedes ver y actualizar el inventario.")

elif menu == "Solicitudes":
    st.header("Solicitudes de Material")
    st.write("Aquí los alumnos pueden solicitar instrumentos.")
    nombre = st.text_input("Nombre del alumno")
    instrumento = st.text_input("Instrumento solicitado")
    if st.button("Enviar solicitud"):
        st.success(f"Solicitud enviada por {nombre} para {instrumento}.")

elif menu == "Reportes":
    st.header("Generación de Reportes")
    st.write("Aquí se pueden generar reportes de uso o stock.")
