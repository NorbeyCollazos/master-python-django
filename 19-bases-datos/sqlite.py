#importar modulo
import sqlite3

#conexon
conexion = sqlite3.connect('prueba.db')

#crear el cursor
cursor = conexion.cursor()

#crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id integer primary key autoincrement,"+
"titulo varchar(255),"+
"descripcion text,"+
"precio int(255)"
")")

# guardar cambios
conexion.commit()

# insertar dato
#cursor.execute("INSERT INTO productos VALUES(null, 'primer producto','descripcion del producto',550);")
#conexion.commit()

# listar datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

for productos in productos:
    print("Título: ",productos[1])
    print("Descripción: ",productos[2])
    print("Precio: ",productos[3])
    print("\n")

#cerrar conexion
conexion.close()