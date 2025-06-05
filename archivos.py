import streamlit as st
import pandas as pd #para leer archivos de excel, csv, etc
import docx2txt as txt
from PyPDF2 import PdfReader
from PIL import Image

def gestorArchivos():
     st.subheader("Carga de archivos de diferentes formatos para su lectura")
     menu=["Arvhivo PDF", "Archivo TXT", "Archivo Excel", "Imágen", ]
     st.sidebar.header("Opciones de Archivos para cargar")
     eleccion=st.sidebar.selectbox("Formato de Archivos",menu)

     if eleccion=="Archivos PDF":
          st.subheader("Lectura de PDF")
     elif eleccion=="Imágen":
          st.subheader("Visualización de Imágen")
          archivo_img = st.file_uploader("Subir imágen", type=["png", "jpg", "jpeg"])
          if archivo_img is not None:
               detalles_archivos={"nombre_archivo":archivo_img.name,
                              "tipo_archivo":archivo_img.type,
                              "tamaño_archivo":archivo_img.size}
               st.write(detalles_archivos)
               st.image(cargar_imagen(archivo_img), width=500)
     elif eleccion=="Archivo Excel":
          #Usamos Pandas (pd) para leer conjuntos de datos
          st.subheader("Conjunto de Datos - (Excel/CSV)")
          archivo_datos=st.file_uploader("Subir Excel", type=["xlsx", "xls", "csv"])

          if archivo_datos is not None:
               detalles_archivos={"tipo_archivo":archivo_datos.type}
               st.write(detalles_archivos)
               if detalles_archivos=="text/csv":
                    df=pd.read_csv(archivo_datos)
               elif detalles_archivos=="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                    df=pd.read_excel(archivo_datos)
               else:
                    df=pd.DataFrame()

               st.dataframe(df)
     elif eleccion=="Archivo TXT":
          st.subheader("Docuemntos de textos")
          archivo_doc=st.file_uploader("Archivo txt:", type=["docx", "doc", "txt"])
          if st.button("Procesar"):
               if archivo_doc is not None:
                    detalles_archivos={"Nombre archivo": archivo_doc.name,
                                       "Tipo de archivo": archivo_doc.type,
                                       "Tamaño archivo": archivo_doc.size}
                    st.write(detalles_archivos)
                    if archivo_doc.type == "text/plain":
                         texto=str(archivo_doc.read(), "UTF-8")
                         st.text(texto)

                    #esto identica el tipo de archivo de word     
                    elif archivo_doc.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                         texto = txt.process(archivo_doc)
                         st.write(texto)



#Decorador de Streamlit para guadar en memoria cache
@st.cache_data

#Funcion para cargar un archivo de imagen
def cargar_imagen(imagen):
     img = Image.open(imagen)
     return (img)

def leer_pdf(file):
     pdfreader=PdfReader(file)
     #Contamos las paginas que contiene el pdf
     count=len(pdfreader.pages)
     todo_el_texto=""
     #iteramos por todas las paginas del pdf
     for i in range(count):
          #Leemos cada una de las paginas
          pagina=pdfreader.pages(i)
          #Concatenamos todas las paginas en esta variable
          todo_el_texto=+pagina.extract_text()
     return todo_el_texto


if __name__ == "__main__":
     gestorArchivos()

