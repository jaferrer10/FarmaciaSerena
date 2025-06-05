import streamlit as st
from PIL import Image
import pandas as pd
import sqlite3

# el valor del ttl está expresado en los segundos que se actualizará automáticamente el caché
@st.cache_data(ttl=600)
def carga_datos():
    cnn=sqlite3.connect("farmacia.db")
    datos=pd.read_sql_query("SELECT * FROM clientes order by apellido", cnn)
    df=pd.DataFrame(datos).sort_values("Apellido")
    df.set_index("idCliente")

    return df

def gestorClientes():
    df = carga_datos()
    
    # Inicializar el estado de la sesión para el cliente seleccionado
    if 'selected_client' not in st.session_state:
        st.session_state.selected_client = None

    with st.container():
        st.title("Modulo de Gestión de Clientes")
        colum_datos, colum_image = st.columns((1,2))
        with colum_datos:
            with st.form(key="form_cliente", clear_on_submit=True):
                st.subheader("Datdos del Cliente")
                nombre=st.text_input("Nombres: ", placeholder="Intruce el nombre del Cliente", value=st.session_state.selected_client.get('Nombre', '') if st.session_state.selected_client else "")
                apellido=st.text_input("Apellidos: ", value=st.session_state.selected_client.get('Apellido', '') if st.session_state.selected_client else "")
                telefono=st.text_input("Telefono: ", value=st.session_state.selected_client.get('Telefono', '') if st.session_state.selected_client else "")
                dccion=st.text_input("Direccion: ", value=st.session_state.selected_client.get('Direccion', '') if st.session_state.selected_client else "")
                mail=st.text_input("e-Mail: ", placeholder="Intruce el e-mail del Cliente", max_chars=60, value=st.session_state.selected_client.get('eMail', '') if st.session_state.selected_client else "")
                nac=st.date_input("Fecha de Nacimiento: ", value=pd.to_datetime(st.session_state.selected_client['FechaNac']).date() if st.session_state.selected_client and 'FechaNac' in st.session_state.selected_client else None)
                obs=st.text_area("Observaciones: ", placeholder="Intruce las observaciones del Cliente", max_chars=200, value=st.session_state.selected_client.get('Observacion', '') if st.session_state.selected_client else "")
                
                # Listas de opciones para los selectbox
                cond_iva_opciones = ["Consumidor Final", "Responsable Inscripto", "Monotributista", "Exento"]
                obra_social_opciones = ["Obra Social", "No tiene"]
                
                # Obtener el índice actual para los selectbox
                cond_iva_index = cond_iva_opciones.index(st.session_state.selected_client.get('CondIva', cond_iva_opciones[0])) if st.session_state.selected_client and 'CondIva' in st.session_state.selected_client else 0
                obra_social_index = obra_social_opciones.index(st.session_state.selected_client.get('ObraSocial', obra_social_opciones[0])) if st.session_state.selected_client and 'ObraSocial' in st.session_state.selected_client else 0
                
                condiva=st.selectbox("Condicion de IVA", cond_iva_opciones, index=cond_iva_index)
                cuit=st.text_input("CUIT: ", max_chars=13, value=st.session_state.selected_client.get('Cuit', '') if st.session_state.selected_client else "")
                obraSocial=st.selectbox("Obra Social", obra_social_opciones, index=obra_social_index)
                
                boton_grabar=st.form_submit_button("Grabar", use_container_width=True) 
                boton_cancelar=st.form_submit_button("Cancelar", use_container_width=True)

                if boton_cancelar:
                    st.session_state.selected_client = None
                    st.rerun()

                if boton_grabar:
                    cursor=cnn.cursor()
                    try:
                        if st.session_state.selected_client is not None:
                            # Actualizar cliente existente
                            cursor.execute("""
                                UPDATE clientes 
                                SET Nombre=?, Apellido=?, Telefono=?, Direccion=?, eMail=?, 
                                    FechaNac=?, Observacion=?, CondIva=?, Cuit=?, ObraSocial=?
                                WHERE idCliente=?
                            """, (nombre, apellido, telefono, dccion, mail, nac, obs, condiva, cuit, obraSocial, st.session_state.selected_client.get('idCliente')))
                        else:
                            # Insertar nuevo cliente
                            cursor.execute("""
                                INSERT INTO clientes 
                                (Nombre, Apellido, Telefono, Direccion, eMail, FechaNac, Observacion, CondIva, Cuit, ObraSocial) 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            """, (nombre, apellido, telefono, dccion, mail, nac, obs, condiva, cuit, obraSocial))
                        cnn.commit()
                        st.success("Cliente grabado correctamente")
                        st.session_state.selected_client = None
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error al grabar el cliente: {str(e)}")

        with colum_image:
            image=Image.open("imagenes/clientes.jpg")
            st.image(image, use_container_width=True)
 
            # Inicializar el estado de la sesión para la selección
            if 'selected_row' not in st.session_state:
                st.session_state.selected_row = None

            # Mostrar el DataFrame
            st.dataframe(
                df,
                use_container_width=True,
                selection_mode="single-row"
            )
                        # Agregar botón para seleccionar la fila actual
            if st.button("Editar Cliente"):
                try:
                    # Obtener el índice de la fila seleccionada
                    selected_indices = st.session_state.get('selected_rows', [])
                    if selected_indices:
                        selected_data = df.iloc[selected_indices[0]].to_dict()
                        st.session_state.selected_client = selected_data
                        return()
                    else:
                        st.warning("Por favor, seleccione un cliente de la tabla")
                except Exception as e:
                    st.error(f"Error al seleccionar el cliente: {str(e)}")



if __name__ == "__main__":
    gestorClientes()


