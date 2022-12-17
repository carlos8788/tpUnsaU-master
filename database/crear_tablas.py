import sqlite3

class CrearDB:
    
    def __init__(self, nombre_tabla: str, columnas: str):
        
        self.__nombre_tabla = nombre_tabla
        self.__columnas = columnas

    def _conectar_db(self):
        """
        Método privado de la clase, no recibe parámetros. 
        Se utiliza para conectar a la base de datos
        """
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
        """id_tabla: ID de la tabla seleccionada"""
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
        Pasar como primer argumento las claves y valores
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
    
    def sql_search(self, column: str, value: str):
        conexion = self._conectar_db()
        sql = f"SELECT * FROM {self.__nombre_tabla} WHERE {column} LIKE '{value}';"
        cursor = conexion.cursor()
        cursor.execute(sql)
        datos = cursor.fetchone()
        conexion.commit()
        conexion.close()
        if datos == None:
            return False
        return (datos[0], datos[2], datos[5])

