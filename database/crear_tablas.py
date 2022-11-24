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



if __name__ == "__main__":
    
    columnas = """(
                "id"	INTEGER NOT NULL,
                "nombre"	VARCHAR(50) NOT NULL,
                "apellido"	VARCHAR(50) NOT NULL,
                "edad"	INTEGER NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT)
              )"""
    
    tabla_persona = CrearDB('persona', columnas)
    # tabla_persona.crear_tabla(param)
    # tabla_persona.insert_sql('nombre, apellido, edad', '"Luis", "Pérez", 34')
    # print(tabla_persona.get_sql())
    # tabla_persona.delete_sql('id',2)
    # tabla_persona.update_sql(id=3, nombre='Lucas')
    # print(tabla_persona.get_one_sql('id', 1))
