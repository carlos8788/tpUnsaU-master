import sqlite3

class CrearDB:
    
    def __init__(self, nombre_tabla, columnas):
        
        self.__nombre_tabla = nombre_tabla
        self.__columnas = columnas

    def _conectar_db(self):
        try:
            nombre_db = 'supermarket.db'
            conexion = sqlite3.connect(nombre_db)

            return conexion
        except:
            print("no se pudo conectar a la base de datos")

    def crear_tabla(self):
        
        conexion = self._conectar_db()
        cursor = conexion.cursor()
        sql = f"CREATE TABLE IF NOT EXISTS {self.__nombre_tabla} {self.__columnas}"
        cursor.execute(sql)
        conexion.commit()
        conexion.close()


    def get_sql(self):
        conexion = self._conectar_db()
        sql = f"SELECT * FROM {self.__nombre_tabla};"
        cursor = conexion.cursor()
        cursor.execute(sql)
        datos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        return datos

    def get_one_sql(self, id_tabla, id_value):
        conexion = self._conectar_db()
        sql = f"SELECT * FROM {self.__nombre_tabla} WHERE {id_tabla}={id_value};"
        cursor = conexion.cursor()
        cursor.execute(sql)
        datos = cursor.fetchone()
        conexion.commit()
        conexion.close()
        if len(datos)==0:
            return f"No hay algún registro con ese ID en la tabla {self.__nombre_tabla}"
        else:
            return datos

    def insert_sql(self, columnas, sql_values):
        conexion = self._conectar_db()
        sql = f"INSERT INTO {self.__nombre_tabla} ({columnas}) VALUES ({sql_values});"
        cursor = conexion.cursor()
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def delete_sql(self, id_tabla, id_value):
        conexion = self._conectar_db()
        sql = f"DELETE FROM {self.__nombre_tabla} WHERE {id_tabla}={id_value};"
        cursor = conexion.cursor()
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    def update_sql(self, **kwargs):
        """
        Pasar como primer argumento el nombre de la tabla y como segundo las claves y valores
        que se van a actualizar teniendo en cuenta que se debe pasar como primer instancia el ID
        """
        conexion = self._conectar_db()
        sql = ''
        contador = 0
        for x, y in kwargs.items():
            if contador == 0:
                ide = f"{x}= '{y}'"
            else:
                sql += f"{x}= '{y}', "
            contador += 1

        query = f"UPDATE {self.__nombre_tabla} SET {sql[:-2]} WHERE {ide};"

        cursor = conexion.cursor()
        cursor.execute(query)
        conexion.commit()
        conexion.close()
    
    def sql_search(self, column, value):
        conexion = self._conectar_db()
        sql = f"SELECT * FROM {self.__nombre_tabla} WHERE {column} LIKE '{value}';"
        cursor = conexion.cursor()
        cursor.execute(sql)
        datos = cursor.fetchone()
        conexion.commit()
        conexion.close()

        if datos == None:
            return False
        
        return datos[2]





if __name__ == "__main__":
    
    columnas = """(
                "id"	INTEGER NOT NULL,
                "usuario"	VARCHAR(50) NOT NULL UNIQUE,
                "contrasenia"	VARCHAR(50) NOT NULL,
                "correo"	VARCHAR(50),
                "direccion"	VARCHAR(100),
                "is_admin" 	INTEGER(1) NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT)
              )"""
    
    tabla_persona = CrearDB('usuario', columnas)
    # tabla_persona.crear_tabla()
    tabla_persona.insert_sql('usuario, contrasenia, correo, direccion, is_admin', '"luis3", "perez", "luis@carlos.com", "av siempre viva", 1')
    # print(tabla_persona.sql_search('usuario', 'luis3'))
    # print(tabla_persona.get_sql())
    # tabla_persona.delete_sql('id',2)
    # tabla_persona.update_sql(id=3, nombre='Lucas')
    # print(tabla_persona.get_one_sql('id', 1))
