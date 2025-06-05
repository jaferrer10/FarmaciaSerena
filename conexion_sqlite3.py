import sqlite3
import pandas as pd

# Conectar a la base de datos
mi_coneccion = sqlite3.connect('farmacia.db')

# Crear el DataFrame de clientes
df_clientes = pd.read_sql_query("SELECT * FROM clientes", mi_coneccion)

# Note: We don't close the connection here since it needs to be used by other modules 