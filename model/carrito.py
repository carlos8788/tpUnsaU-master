from tkinter import messagebox

class Carrito:

    def __init__(self, comprador, lista_productos, total):
        self.__comprador = comprador
        self.__lista_productos = lista_productos
        self.__total = total
        

    def insertar_en_carrito(self, tabla, cantidad, lista, *args):
        try:
            lista.insert(0, cantidad)
            print(lista)
            print(lista[1].get(), lista[2].get(), lista[3])
            if len(lista) != 4:
                lista.clear()
                self._borrar_entradas(args[0], args[1], args[2], args[3], args[4])
            else:
                tabla.insert('', 0, text=lista[0], values=(
                        lista[1].get(), lista[2].get(), lista[3]))
                lista.clear()
                self._borrar_entradas(args[0], args[1], args[2], args[3], args[4])
        except:
            pass

    def _borrar_entradas(self, descripcion, precio, stock, product, entrada):
        descripcion.config(text='')
        precio.config(text='')
        stock.config(text='')
        product.config(text='')
        entrada.set('')

    def borrar_item(self):
        pass

    def capturar_datos(self, data: list):
        print(data)
        self.insertar_producto = []
        # insertar_producto.append(self.entrada.get())
        self.insertar_producto.append(data[0])
        self.insertar_producto.append(data[1])
        self.insertar_producto.append(data[2])
        # return insertar_producto