from tkinter import messagebox

class Carrito:

    def __init__(self, comprador, lista_productos, total):
        self.__comprador = comprador
        self.__lista_productos = lista_productos
        self.__total = total
        

    def insertar_en_carrito(self, tabla, cantidad, lista, *args):
        try:
            lista.insert(0, cantidad)
            if len(lista) != 4:
                lista.clear()
                self.borrar_entradas(args[0], args[1], args[2], args[3], args[4])
            else:
                tabla.insert('', 0, text=lista[0], values=(
                        lista[1], lista[2], lista[3]))
                lista.clear()
                self.borrar_entradas(args[0], args[1], args[2], args[3], args[4])
        except:
            pass

    def borrar_entradas(self, descripcion, precio, stock, product, entrada):
        descripcion.config(text='')
        precio.config(text='')
        stock.config(text='')
        product.config(text='')
        entrada.set('')

    def borrar_item(self):
        pass