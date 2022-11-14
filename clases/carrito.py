class Carrito:

    def __init__(self, comprador, lista_productos, total):
        self.__comprador = comprador
        self.__lista_productos = lista_productos
        self.__total = total


def insertar_en_carrito(tabla, cantidad, args):
    args.insert(0, cantidad)
    print(tabla)
    print(args)
    print(len(args))
    if len(args) != 4:
        pass
    else:
        tabla.insert('', 0, text=args[0], values=(
                args[1], args[2], args[3]))
        args.clear()