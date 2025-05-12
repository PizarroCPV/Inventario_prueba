import streamlit as st

st.title("Plataforma TALLER PAÑOL")
st.write("Seleccione una opción en la barra lateral para navegar.")

# Información sobre navegación
st.info("👈 Use el menú de la izquierda para navegar entre las diferentes secciones")

# También puedes agregar enlaces directos usando markdown
st.markdown("""
### Enlaces rápidos:
- [Inventario](/app.py)
- [Productos](/Productos)
- [Dashboard](/Dashboard)
""")