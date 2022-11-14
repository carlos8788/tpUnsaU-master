from crear_db import CrearDB

class CarritoDB:

    def __init__(self):
        self.database = CrearDB()

    def tabla_carrito(self):
        try:
            sql = """(
                      "IDUsuario"	INTEGER NOT NULL,
                      "usuario"	VARCHAR(50) NOT NULL UNIQUE,
                      "contraseña"	VARCHAR(200) NOT NULL,
                      PRIMARY KEY("IDAdmin" AUTOINCREMENT)
                      );"""
            
            self.database.crear_tabla('usuario', sql)
        except:
            print("No se pudo crear la tabla")


    def mostrar_usuarios(self):
        mostrar = self.database.get_sql('usuario')
        for x in mostrar:
            print(x)

    def mostrar_un_usuario(self, id_value):
        mostrar = self.database.get_one('usuario','IDAdmin', id_value)
        return mostrar

    def crear_usuario(self, *args):
        tabla= "usuario ('usuario', 'contraseña')"
        self.database.insert_sql(tabla, args)
    
    def borrar_usuario(self, id):
        IDUsuario = f"IDUsuario= {id}"
        self.database.delete_sql('usuario', IDUsuario)
    
    def modificar_usuario(self, **kwargs):
        self.database.update_sql('usuario', **kwargs)

if __name__ == "__main__":
    pass