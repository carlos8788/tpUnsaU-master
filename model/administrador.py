from database.crear_tablas import CrearDB
from model.producto import Producto
class Administrador:

    def __init__(self):
        self.tabla_producto = CrearDB('producto', None)
        self.producto = Producto(None, None, None, None, None)
    
    def agregar_producto(self, window, treeview, *args):
        a = str(args[0])
        a = a[1:-1]
        b = str(args[1])
        b = b[1:-1]
        self.tabla_producto.insert_sql(a, b)
        self.producto.record(treeview)
        self.producto.get_products(treeview)



    def editar_producto(self):
        pass