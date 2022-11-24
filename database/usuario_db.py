from crear_db import CrearDB

class UsuarioDB:

    def __init__(self):
        self.database = CrearDB()

    def tabla_carrito(self):
        try:
            sql = """(
                      "id_usuario"	INTEGER NOT NULL,
                      "usuario"	VARCHAR(50) NOT NULL UNIQUE,
                      "contraseña"	VARCHAR(200) NOT NULL,
                      "correo" 	VARCHAR(50) NOT NULL UNIQUE,
                      "direccion"	VARCHAR(50),
                      "is_admin" 	VARCHAR(1) NOT NULL,
                      PRIMARY KEY("IDAdmin" AUTOINCREMENT)
                      );"""
            
            self.database.crear_tabla('usuario', sql)
        except:
            print("No se pudo crear la tabla")


    def mostrar_usuarios(self):
        mostrar = self.database.get_sql('usuario')
        # for x in mostrar:
        #     print(x)

    def mostrar_un_usuario(self, id_value):
        mostrar = self.database.get_one('usuario','IDAdmin', id_value)
        return mostrar

    def crear_usuario(self, *args):
        tabla= "usuario ('usuario', 'contraseña')"
        self.database.insert_sql(tabla, args)
    
    def borrar_usuario(self, id):
        id_usuario = f"id_usuario= {id}"
        self.database.delete_sql('usuario', id_usuario)
    
    def modificar_usuario(self, **kwargs):
        self.database.update_sql('usuario', **kwargs)

if __name__ == "__main__":
    pass