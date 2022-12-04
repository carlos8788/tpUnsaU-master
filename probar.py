import sqlite3
conexion = sqlite3.connect('supermarket.db')
# Creamos el cursor
cursor = conexion.cursor()
columnas = """(                                                
                                "id"	INTEGER NOT NULL,
                                "nombre"	VARCHAR(50) NOT NULL UNIQUE,
                                "stock"	INTEGER NOT NULL,
                                "precio"	REAL NOT NULL,
                                "categoria" VARCHAR(50) NOT NULL,
                                "descripcion"	TEXT,
                                PRIMARY KEY("id" AUTOINCREMENT)
                                )"""
# Creamos una tabla de usuarios con nombres, edades y emails

# cursor.execute(f"CREATE TABLE IF NOT EXISTS producto {columnas}")
import json
ruta = 'sin_id.json'
with open(ruta) as contenido:
    datos = json.load(contenido)
    for dato in datos:
        try:
            print(dato['categoria'])
            cursor.execute(f"INSERT INTO producto('nombre', 'stock', 'precio', 'categoria', 'descripcion') VALUES('{dato['nombre']}', '{dato['stock']}', '{dato['precio']}', '{dato['categoria']}', '{dato['descripcion']}')")
            conexion.commit()
        except:
            pass
        
conexion.close()
# cursor.execute("INSERT INTO orders('OrderNumber', 'PersonID') VALUES(15, 3)")

# cursor.execute("""CREATE TABLE IF NOT EXISTS usuario(
#     PersonID INTEGER NOT NULL,
#     name VARCHAR(50) NOT NULL,
    # PRIMARY KEY (PersonID AUTOINCREMENT));""")

# cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
#     OrderID INTEGER NOT NULL,
#     OrderNumber INTEGER NOT NULL,
#     PersonID INTEGER,
#     PRIMARY KEY (OrderID AUTOINCREMENT),
#     FOREIGN KEY (PersonID) REFERENCES usuario(PersonID) ON DELETE CASCADE );""")

# conexion.close()

# conexion2 = sqlite3.connect('ejemplo.db')
# cursor= conexion2.cursor()
# #Insertamos un registro en la tabla usuario
# cursor.execute("INSERT INTO orders('OrderNumber', 'PersonID') VALUES(15, 3)")
# # Guardamos los cambios haciendo un commit
# conexion2.commit()
# conexion2.close()

# conexion2 = sqlite3.connect('ejemplo.db')
# cursor= conexion2.cursor()
# #Insertamos un registro en la tabla usuario
# cursor.execute("PRAGMA foreign_keys = ON;")
# cursor.execute("DELETE FROM usuario WHERE PersonID=3")
# # Guardamos los cambios haciendo un commit

# conexion2.commit()
# conexion2.close()

# frame_1 = Frame(window, height=539, width=386, background='red')