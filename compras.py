import streamlit as st
import pandas as pd

def gestorcompras():
     st.subheader("Gestión de Compras a Proveedores")
     #Creamos un formulario
     with st.container():
          campos_col, grilla_col = st.columns(2)
          with campos_col:
               with st.form(key="Gestion_compra"):
                    st.write("Gestión de Compras a Proveedores")
                    proveedor=st.selectbox("Proveedores", ["Droguería Suizo","Monroe Americana Rioja","Monroe Americana Cordoba", "Genericos"])
                    cbarra=st.text_input("Código de Barra")
                    producto=st.text_input("Descripción del Producto:")
                    cantidad=st.number_input("Cantidad")
                    col1, col2 = st.columns(2)
                    with col1:
                         grabar=st.form_submit_button(label="Grabar")
                    with col2:
                         cancelar=st.form_submit_button(label="Cancelar")
          with grilla_col:
               pass


if __name__ == "__main__":
     gestorcompras()