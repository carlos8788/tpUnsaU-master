from database.producto_db import ProductoDB


class Producto:
    def __init__(self, nombre, stock, precio, descripcion):
        self.__stock = stock
        self.__nombre = nombre
        self.__precio = precio
        self.__descripcion = descripcion

    def get_stock(self):
        return self.__stock

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

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

################# SACAR LUEGO DE ACá ##########################################


def get_products(tabla):

    nuevo_producto = ProductoDB()

    db_rows = nuevo_producto.mostrar_productos()

    for row in db_rows:
        # print(row)
        tabla.insert('', 0, text=row[0], values=(
            row[1], row[2], row[3], row[4]))


def record(tabla):
    records = tabla.get_children()
    # print(records)
    for i in records:
        tabla.delete(i)


# def mostrar(descripcion, precio, stock, product, data):

#     descripcion.config(text=data[3])
#     precio.config(text=data[2])
#     stock.config(text=data[1])
#     product.config(text=data[0])

################# SACAR LUEGO DE ACá ##########################################
