import streamlit as st
from PIL import Image
from compras import gestorcompras
from ventas import gestorventas
from archivos import gestorArchivos
from clientes import gestorClientes

# Configuración del tema directamente en el código
st.set_page_config(
    page_title="Serena",
    page_icon="icons8-de-acuerdo-48.png",
    layout="wide"
)

#Esta funcion de streamlit abre un espacio de memoria en el cache para guardar doocumentos
#@st.cache_data

# Aplicar tema personalizado
st.markdown("""
    <style>
    .stApp {
        background-color: #F5F5F5;
    }
    .stButton>button {
        background-color: #F63366;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #E0E0E0;
    }
    </style>
""", unsafe_allow_html=True)

with st.container():
     st.title("GESTION DE FARMACIA SERENA")
     st.header("de Flavia Valeria Bustos - MP.122")
     st.write("Utilice el menú de opciones de la columna lateral Izquierda")
     #Image de la portada principal
     img=Image.open("imagenes\Cartel.jpg")
     st.image(img)
     
st.write("---")

def main():
     st.sidebar.header("Opciones del Sistema")
     menu=["Escritorio", "Compras", "Ventas", "Clientes", "Informes", "Mantenimiento", "Archivos", "Inicio"]
     seleccion=st.sidebar.selectbox("Seleccione una opción", menu)
     if seleccion=="Escritorio":
          pass
     elif seleccion=="Compras":
          gestorcompras()
     elif seleccion=="Ventas":
          gestorventas()
     elif seleccion=="Clientes":
          gestorClientes()
     elif seleccion=="Informes":
          st.subheader("Modulo de Informes")
     elif seleccion=="Archivos":
          gestorArchivos()
     elif seleccion=="Mantenimiento":
          st.subheader("Modulo de Mantenimiento")


if __name__ == "__main__":
     main()

