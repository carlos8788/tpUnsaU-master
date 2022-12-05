from tkinter import messagebox
from _tkinter import TclError


class Carrito:

    def __init__(self, comprador, total):
        self.__comprador = comprador
        self.__lista_productos = []
        self.__total = total


    def insertar_en_carrito(self, tabla, lista_productos: list, cantidad, *args):
        try:
            if not len(lista_productos) == 4:
                lista_productos.insert(0, cantidad.get())
                subtotal = self._subtotal(float(lista_productos[2]), int(cantidad.get()))
                lista_productos.append(subtotal)
                self._carrito(lista_productos)
                # self.__lista_productos.append(lista_productos)
                tabla.insert('', 0, text=lista_productos[0], values=(
                            lista_productos[1], lista_productos[2], lista_productos[3]))
                
                self._borrar_entradas(*args)
                lista_productos.clear()
        except TclError:
            messagebox.showwarning("Datos", "No hay nada que ingresar")

    def _borrar_entradas(self, descripcion, precio, stock, product, entrada):
        descripcion.config(text='')
        precio.config(text='')
        stock.config(text='')
        product.config(text='')
        entrada.set('')

    def _subtotal(self, precio: float, cantidad: int):
        subtotal = precio * cantidad
        return subtotal

    def _carrito(self, item: list):
        item2 = item.copy()
        print(id(item2))
        print(id(item))

        self.__lista_productos.append(item2)
        print(self.__lista_productos)

    
    def comprar(self):
        print(self.__lista_productos)


    def borrar_item(self, tabla_carrito):
        try:
            records = tabla_carrito.focus()
            data = tabla_carrito.item(records)
            print(data["text"], data["values"])
            tabla_carrito.delete(records)
        except:
            messagebox.showerror("Error", "No hay ningún item seleccionado")

