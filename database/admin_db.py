from crear_db import CrearDB

class CarritoDB:

    def __init__(self):
        self.database = CrearDB()

    def tabla_carrito(self):
        try:
            sql = """(
                      "IDAdmin"	INTEGER NOT NULL,
                      "admin"	VARCHAR(50) NOT NULL,
                      "contraseña"	VARCHAR(200) NOT NULL,
                      PRIMARY KEY("IDAdmin" AUTOINCREMENT)
                      );"""
            
            self.database.crear_tabla('administrador', sql)
        except:
            print("No se pudo crear la tabla")


    def mostrar_administradores(self):
        mostrar = self.database.get_sql('administrador')
        for x in mostrar:
            print(x)

    def mostrar_un_admin(self, id_value):
        mostrar = self.database.get_one('administrador','IDAdmin', id_value)
        return mostrar

    def crear_administrador(self, *args):
        tabla= "administrador ('admin', 'contraseña')"
        self.database.insert_sql(tabla, args)
    
    def borrar_administrador(self, id):
        IDAdmin = f"IDAdmin= {id}"
        self.database.delete_sql('administrador', IDAdmin)
    
    def modificar_administrador(self, **kwargs):
        self.database.update_sql('administrador', **kwargs)

if __name__ == "__main__":
    pass