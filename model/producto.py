from database.crear_tablas import CrearDB
from tkinter import messagebox

class Producto:
    def __init__(self, nombre, stock, precio, categoria, descripcion):
        self.__stock = stock
        self.__nombre = nombre
        self.__precio = precio
        self.__categoria = categoria
        self.__descripcion = descripcion
        self.__columnas = """ producto (                                
                                "id"	INTEGER NOT NULL,
                                "nombre"	VARCHAR(50) NOT NULL UNIQUE,
                                "stock"	INTEGER NOT NULL,
                                "precio"	REAL NOT NULL,
                                "categoria" VARCHAR(50) NOT NULL,
                                "descripcion"	TEXT,
                                PRIMARY KEY("id" AUTOINCREMENT)
                                )"""
        self.table = CrearDB("producto", self.__columnas)
        try:
            self.table.crear_tabla()
        except:
            pass

    def get_stock(self):
        return self.__stock

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_categoria(self):
        return self.__categoria

    def get_descripcion(self):
        return self.__descripcion

    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
        return self.__nombre

    def set_stock(self, new_stock):
        self.__stock = new_stock
        return self.__stock

    def set_descripcion(self, new_descripcion):
        self.__descripcion = new_descripcion
        return self.__descripcion

    def set_precio(self, new_precio):
        self.__precio = new_precio
        return self.__precio

    def set_precio(self, new_categoria):
        self.__categoria = new_categoria
        return self.__categoria

    def _carga_tree(self, treeview, row):
            treeview.insert('', 0, text=row[0], values=(
                row[1], row[2], row[3], row[4], row[5]))

    def get_products(self, treeview):

        db_rows = self.table.get_sql()
        for row in db_rows:
            if row[2]> 0:
                self._carga_tree(treeview, row)
                
    def get_products_admin(self, treeview):

        db_rows = self.table.get_sql()
        for row in db_rows:

            self._carga_tree(treeview, row)

    def record(self, treeview):
        records = treeview.get_children()
        for i in records:
            treeview.delete(i)


    def mostrar(self, descripcion, precio, stock, product, data):

        descripcion.config(text=data[3])
        precio.config(text=data[2])
        stock.config(text=data[1])
        product.config(text=data[0])

    def mostrar_categorias(self):
        seteo = []
        categorias = self.table.get_sql()
        for categoria in categorias:
            categoria = categoria[4].upper()
            seteo.append(categoria)
        seteo = set(seteo)
        seteo = list(seteo)
        seteo.append("TODAS")
        return seteo
    
    def cargar_categoria(self, categ_recibida, treeview):
        self.record(treeview)
        if categ_recibida == "TODAS":
            self.get_products(treeview)
        db_rows = self.table.get_sql()
        for row in db_rows:
            if row[4] == categ_recibida:
                if row[2] > 0:
                    self._carga_tree(treeview, row)
