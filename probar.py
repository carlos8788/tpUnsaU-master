import sqlite3
conexion = sqlite3.connect('ejemplo.db')
# Creamos el cursor
cursor = conexion.cursor()
# Creamos una tabla de usuarios con nombres, edades y emails


cursor.execute("""CREATE TABLE IF NOT EXISTS usuario(
    PersonID INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (PersonID AUTOINCREMENT));""")

cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
    OrderID INTEGER NOT NULL,
    OrderNumber INTEGER NOT NULL,
    PersonID INTEGER,
    PRIMARY KEY (OrderID AUTOINCREMENT),
    FOREIGN KEY (PersonID) REFERENCES usuario(PersonID) ON DELETE CASCADE );""")

conexion.close()

# conexion2 = sqlite3.connect('ejemplo.db')
# cursor= conexion2.cursor()
# #Insertamos un registro en la tabla usuario
# cursor.execute("INSERT INTO orders('OrderNumber', 'PersonID') VALUES(15, 3)")
# # Guardamos los cambios haciendo un commit
# conexion2.commit()
# conexion2.close()

conexion2 = sqlite3.connect('ejemplo.db')
cursor= conexion2.cursor()
#Insertamos un registro en la tabla usuario
cursor.execute("PRAGMA foreign_keys = ON;")
cursor.execute("DELETE FROM usuario WHERE PersonID=3")
# Guardamos los cambios haciendo un commit

conexion2.commit()
conexion2.close()

# frame_1 = Frame(window, height=539, width=386, background='red')