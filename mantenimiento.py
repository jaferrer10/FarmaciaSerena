import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def gestorsoporte():

    with st.container():
        st.title("Pruebas de Mantenimiento de Datos")
        st.subheader("Pruebas Estadisticas de Uber en California")
        datos, mapa = st.columns((1,2))

        DATE_COLUMN = 'date/time'
        #trae datos de ejemplo 
        DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
                    'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

        @st.cache_data
        def load_data(nrows):
            data= pd.read_csv(DATA_URL, nrows=nrows)
            lowercase= lambda x: str(x).lower()
            data.rename(lowercase, axis='columns', inplace=True)
            data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
            return data


        data_load_state = st.text('Descargando datos....')
        # Load 10,000 rows of data into the dataframe.
        data = load_data(10000)
        # Notify the reader that the data was successfully loaded.
        data_load_state.text=st.text("Descarga completada con exito....")

        st.write(data)

        # Mostrar el mapa
        st.map(data)

