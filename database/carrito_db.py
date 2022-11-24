from crear_db import CrearDB

class CarritoDB:

    def __init__(self):
        self.database = CrearDB()

    def tabla_carrito(self):
        try:
            sql = """(
                      "id_carrito"	INTEGER NOT NULL,
                      "lista_productos"	VARCHAR(50) NOT NULL,
                      "total_a_pagar" REAL NOT NULL,
                      "modo_de_pago" VARCHAR(1) NOT NULL,
                      "fecha" DATE NOT NULL,
                      "id_usuario" INTEGER NOT NULL,
                       PRIMARY KEY("id_carrito" AUTOINCREMENT)
                       FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE 
                      );"""
            
            self.database.crear_tabla('carrito', sql)
        except:
            print("No se pudo crear la tabla")


    def mostrar_carrito(self):
        mostrar = self.database.get_sql('carrito')
        for x in mostrar:
            print(x)

    def crear_carrito(self, *args):
        tabla= "carrito ('lista_productos', 'total_a_pagar', 'modo_de_pago', 'id_usuario')"
        self.database.insert_sql(tabla, args)
    
    def borrar_carrito(self, id):
        IDProducto = f"id_carrito= {id}"
        self.database.delete_sql('carrito', IDProducto)
    
    def modificar_carrito(self, **kwargs):
        self.database.update_sql('carrito', **kwargs)


if __name__ == "__main__":
    carrito = CarritoDB()
    carrito.tabla_carrito()
    ver = "leche","tomate","aceite"
    # print(str(ver))
    carrito.crear_carrito(str(ver), '100', "tarjeta", '1')