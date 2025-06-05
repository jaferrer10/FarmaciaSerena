import sqlite3

def crea_basedatos():
    #conectar a la base de datos y la crea si no existe
    conn = sqlite3.connect("farmacia.db")
    cursor=conn.cursor()

    #Crea la tabla Clientes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes(
                   idCliente INTEGER PRIMARY KEY AUTOINCREMENT,
                   Nombre TEXT NOT NULL,
                   Apellido TEXT NOT NULL,
                   Telefono TEXT NOT NULL,
                   Direccion TEXT,
                   eMail TEXT,
                   FechaNac date,
                   Observacion TEXT,
                   CondIva INTERGER,
                   Cuit TEXT,
                   ObraSocial INTEGER
                   )
         """)
    
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS compras(
                   idCompras INTEGER PRIMARY KEY AUTOINCREMENT,
                   idProveedor INTEGER NOT NULL,
                   Fecha DATE NOT NULL,
                   Tipo TEXT NOT NULL,
                   Cpte_numero TEXT NOT NULL,
                   Importe DOUBLE NOT NULL,
                   Impuesto1 DOUBLE, 
                   Impuesto2 DOUBLE,
                   Impuesto3 DOUBLE,
                   Impuesto4 DOUBLE,
                   Observacion TEXT,
                   Estado text,
                   FechaVto DATE,
                   idRubro INTEGER NOT NULL,
                   idUsuario INTEGER NOT NULL,
                   FOREIGN KEY (idRubro) REFERENCES Rubro(idRubro),
                   FOREIGN KEY (idProveedor) REFERENCES Proveedores(idProveedor)
                   )
        """)
    
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS pedidos(
                   idPedido INTEGER PRIMARY KEY AUTOINCREMENT,
                   Fecha REAL NOT NULL, 
                   Codigo INTEGER NOT NULL,
                   Descripcion TEXT NOT NULL,
                   Cantidad DOUBLE NOT NULL,
                   idProveedor INTEGER NOT NULL,
                   Estado INTEGER NOT NULL,
                   Observacion TEXT
                   )
        """)
    
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Rubro(
                   idRubro INTEGER PRIMARY KEY AUTOINCREMENT,
                   Descripcion TEXT NOT NULL,
                   Margen DOUBLE
                   )
        """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Proveedores(
                   idProveedor INTEGER PRIMARY KEY AUTOINCREMENT,
                   Nombre TEXT NOT NULL,
                   Direccion TEXT,
                   Localidad TEXT,
                   Provincia TEXT,
                   Telefono TEXT,
                   Observaciones TEXT
                   )
         """)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    crea_basedatos()
    print("Las bases de datos fueron creadas exitosamente....")