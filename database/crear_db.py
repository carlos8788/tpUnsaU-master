import sqlite3

class CrearDB:
    def __init__(self):
        pass

    def _conectar_db(self):
        try:
            nombre_db = 'supermarket.db'
            conexion = sqlite3.connect(nombre_db)

            return conexion
        except:
            print("no se pudo conectar a la base de datos")

    def crear_tabla(self, sql_tabla, columnas):
        conexion = self._conectar_db()
        cursor = conexion.cursor()
        sql = "CREATE TABLE IF NOT EXISTS " + str(sql_tabla) + " " + str(columnas)
        cursor.execute(sql)
        conexion.commit()
        conexion.close()


    def get_sql(self, sql_tabla):
        conexion = self._conectar_db()
        sql = "SELECT * FROM " + sql_tabla + ";"
        cursor = conexion.cursor()
        cursor.execute(sql)
        datos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        return datos

    def get_one(self, sql_tabla, id_name, id_value):
        conexion = self._conectar_db()
        sql = "SELECT * FROM " + sql_tabla + "WHERE "+ id_name +"=" + id_value+";"
        cursor = conexion.cursor()
        cursor.execute(sql)
        datos = cursor.fetchone()
        conexion.commit()
        conexion.close()
        if len(datos)==0:
            return f"No hay algún registro con ese ID en la tabla {sql_tabla}"
        else:
            return datos

    def insert_sql(self, sql_tabla, sql_values):
        conexion = self._conectar_db()
        sql = f"INSERT INTO {sql_tabla} VALUES {sql_values};"
        cursor = conexion.cursor()
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def delete_sql(self, sql_tabla, id):
        conexion = self._conectar_db()
        sql = f"DELETE FROM {sql_tabla} WHERE {id};"
        cursor = conexion.cursor()
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def update_sql(self, sql_tabla,**kwargs):
        conexion = self._conectar_db()
        sql = ''
        contador = 0
        for x, y in kwargs.items():
            if contador == 0:
                ide = f"{x}= '{y}'"
            else:
                sql += f"{x}= '{y}', "
            contador += 1

        query = f"UPDATE {sql_tabla} SET {sql[:-2]} WHERE {ide};"

        cursor = conexion.cursor()
        cursor.execute(query)
        conexion.commit()
        conexion.close()

if __name__ == "__main__":
    tabla = CrearDB()
    # param = """(
    #             "id"	INTEGER NOT NULL,
    #             "nombre"	VARCHAR(50) NOT NULL,
    #             "stock"	INTEGER NOT NULL,
    #             "precio"	REAL NOT NULL,
    #             "descripcion"	TEXT,
    #             PRIMARY KEY("id" AUTOINCREMENT)
    #         )"""

    param = """(
    OrderID INTEGER NOT NULL,
    OrderNumber INTEGER NOT NULL,
    PersonID INTEGER,
    PRIMARY KEY (OrderID AUTOINCREMENT),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID) ON DELETE CASCADE 
);"""
    
    param2 = """(
    ID INTEGER NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age INTEGER,
    PRIMARY KEY (ID AUTOINCREMENT)
    
);"""
    ver = tabla.crear_tabla('Persons', param2)
    # ver2 = tabla.crear_tabla('Orders ', param)
    # print(ver)
    tabla.insert_sql("Persons ('LastName','FirstName','Age')", "('Gaseosa', 'asdasd', 15)")
    tabla.insert_sql("Orders", "(3,123,3)")
    # tabla.get_sql('producto')
    # 
    # tabla.delete_sql("Persons", "ID=3")
    print(tabla.get_one("Orders", "OrderID",3))