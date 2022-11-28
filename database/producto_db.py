from . import crear_db

class ProductoDB:
    def __init__(self):

        self.database = crear_db.CrearDB()
        self.tabla_producto()

    def tabla_producto(self):
        try:
            sql = """(
                      "IDProducto"	INTEGER NOT NULL,
                      "nombre"	VARCHAR(50) NOT NULL,
                      "stock"	INTEGER NOT NULL,
                      "precio"	REAL NOT NULL,
                      "descripcion"	TEXT,
                      PRIMARY KEY("IDProducto" AUTOINCREMENT)
                      );"""
            
            self.database.crear_tabla('producto', sql)
        except:
            print("No se pudo crear la tabla")


    def mostrar_productos(self):
        mostrar = self.database.get_sql('producto')
        return mostrar

    def mostrar_un_producto(self, id_value):
        mostrar = self.database.get_one('producto','IDProducto', id_value)
        return mostrar

    def crear_producto(self, *args):
        tabla= "producto ('nombre', 'stock', 'precio', 'descripcion')"
        self.database.insert_sql(tabla, args)
    
    def borrar_producto(self, id):
        IDProducto = f"IDProducto= {id}"
        self.database.delete_sql('producto', IDProducto)
    
    def modificar_producto(self, **kwargs):
        self.database.update_sql('producto', **kwargs)

if __name__ == "__main__":

    nuevo_producto = ProductoDB()
    # nuevo_producto.crear_producto('Gaseosa', '15', '150', 'Talca Cola 3L')
    # nuevo_producto.modificar_producto(IDProducto=1, nombre='LEche', stock=15, precio=150, descripcion='Leche NIDO en tarro 500gr')
    # nuevo_producto.borrar_producto(2)
    # nuevo_producto.mostrar_productos()
    print("***"*10)
    # print(nuevo_producto.mostrar_un_producto(3))
    # nuevo_producto


    # nuevo_producto.tabla_producto()