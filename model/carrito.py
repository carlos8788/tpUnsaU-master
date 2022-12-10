from tkinter import messagebox
# from _tkinter import TclError
from database.crear_tablas import CrearDB
from datetime import datetime

class Carrito:

    def __init__(self, comprador, total):
        self.__comprador = comprador
        self.__lista_productos = []
        self.__total = total
        self.__columnas = """(
                                "id_carrito"	INTEGER NOT NULL,
                                "usuario"	VARCHAR(50) NOT NULL,
                                "direccion"	VARCHAR(100),
                                "lista_productos" TEXT NOT NULL,
                                "total" REAL NOT NULL,
                                "cantidad_productos" INTEGER NOT NULL,
                                "fecha_hora" DATE NOT NULL,
                                PRIMARY KEY("id_carrito" AUTOINCREMENT)
                                )"""
        self.table = CrearDB("carrito", self.__columnas)
        self.table.crear_tabla()
        self.table_producto = CrearDB("producto", None)
        self.table_usuario = CrearDB("usuario", None)

    def insertar_en_carrito(self, tabla_origen, tabla_destino, lista_productos: list, cantidad, *args):
        try:
            # print(self._traer_producto(tabla_origen), "desde insertar a carrito")
            if not int(cantidad.get()) > lista_productos[2]:
                # print(type(cantidad.get()), "lista_productos")
                cantidad_nueva = self._restar_cantidad(lista_productos[2], int(cantidad.get()))

                lista_productos.pop(2)
                # print(lista_productos, "desde insertar_en_carrito")
                lista_productos.insert(0, cantidad.get())

                subtotal = self._subtotal(float(lista_productos[2]), int(cantidad.get()))
                lista_productos.append(subtotal)

                self._carrito(lista_productos)
                # self.__lista_productos.append(lista_productos)

                tabla_destino.insert('', 0, text=lista_productos[0], values=(
                            lista_productos[1], lista_productos[2], lista_productos[3]))
                
                self._borrar_entradas(*args)
                lista_productos.clear()

                datos = self._traer_producto(tabla_origen)
                # print(datos, "_traer_producto")
                self._actualizar_producto(tabla_origen, datos, cantidad_nueva)

            else:
                messagebox.showwarning("Cantidad", "No se puede comprar más de lo que hay en stock")
        except:
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
        # print(id(item2))
        # print(id(item)
        self.__lista_productos.append(item2)
        # print(self.__lista_productos)

    def borrar_item(self, tabla_origen, tabla_destino):
        records = tabla_destino.focus()
        # print(records, "Borrar item")    
        try:

            
            data = tabla_destino.item(records)
            # print(data["text"], data["values"], "Estoy en borrar_item")
            devolver = data['text']
            dato = self._traer_producto(tabla_destino
            )
            # print(dato, "___> dato ásado a suma")
            suma = self._sumar_cantidad(dato[2], devolver)
            self._actualizar_producto(tabla_origen, dato, suma)
            tabla_destino.delete(records)
            

        except:
            messagebox.showerror("Error", "No hay ningún item seleccionado")
    
    def mostrar_producto(self, window, tabla_origen, tabla_destino):
        try:
            producto_origen = self._traer_producto(tabla_destino)
            # print(producto_origen[2], "mostrar_producto oringen")
            producto_destino = tabla_destino.focus()
            stock_destino = tabla_destino.item(producto_destino)
            # print(stock_destino['text'], "mostrar_producto stock destin")
            suma = self._sumar_cantidad(int(producto_origen[2]), int(stock_destino['text']))
            self._actualizar_producto(tabla_origen, [producto_origen[0]], suma)
            lista = [producto_origen[0], producto_origen[1], suma, producto_origen[3], producto_origen[4], producto_origen[5]]
            return lista
        except:
            window.destroy()
            return messagebox.showwarning("Seleccionar", "No se seleccionó un producto para mostrar")

        

    def modificar_cantidad(self, window, tabla_origen, tabla_destino, item, cantidad_nueva):
        # Recibe la cantidad total del producto para mostrar en el label heredada del item seleccionado
        # Condicion de que la nueva cantidad seleccionada no supere a la existente
        self.mostrar_producto(tabla_origen, tabla_destino)
        self.borrar_item(tabla_origen, tabla_destino)########

        if not cantidad_nueva>int(item[2]):
            
            # print(f"nueva cantidad {cantidad_nueva}")
            # print(item, "ITEM")
            subtotal = self._subtotal(item[3], cantidad_nueva)
            tabla_destino.insert('', 0, text=cantidad_nueva, values=(
                            item[1], item[3], subtotal))
            resta = self._restar_cantidad(item[2], cantidad_nueva)
            self._actualizar_producto(tabla_origen, [item[0]], resta)
            

            window.destroy()
        else:
            return messagebox.showerror("Cantidad", "La cantidad seleccionada supera a la existente\n Por favor elija una cantidad inferior")

    # def actualizar_producto(self, tabla, cantidad_total, cantidad_nueva):

    def _traer_producto(self, tabla_destino):
        datos = tabla_destino.focus()
        
        # print(datos2)
        nombre = tabla_destino.item(datos)
        buscar =nombre["values"][0]
        producto = self.table_producto.sql_search("nombre", buscar)
        dato = self.table_producto.get_one_sql("id", producto[0])
        # print(dato, "--->desde traer producto")
        # self.borrar_item(tabla_origen, tabla_destino)
        return dato

    def _actualizar_producto(self, treeview, producto_actualizado: list, cantidad_nueva):

        self.table_producto.update_sql(id=producto_actualizado[0], stock=cantidad_nueva)
        self._refresh_treeview(treeview)
        self._get_products(treeview)
    

    def _restar_cantidad(self, cantidad_actual, cantidad_nueva):
        if int(cantidad_actual)>0 and int(cantidad_actual)>=int(cantidad_nueva):
            return cantidad_actual - cantidad_nueva
        else:
            messagebox.showerror("Cantidad", "No se puede comprar esa cantidad")
            return 0
    
    def _sumar_cantidad(self, cantidad_actual, cantidad_nueva):
        # print(cantidad_actual, cantidad_nueva, "estoy en SUMA-----------")
        # print(type(cantidad_actual), type(cantidad_nueva))
        # return 0
        return int(cantidad_nueva) + int(cantidad_actual)
        
        

    def _carga_tree(self, treeview, row):
            # print(row)
            treeview.insert('', 0, text=row[0], values=(
                row[1], row[2], row[3], row[4], row[5]))

    def _get_products(self, treeview):

        db_rows = self.table_producto.get_sql()
        for row in db_rows:
            if row[2]> 0:
                self._carga_tree(treeview, row)
            
        

    def _refresh_treeview(self, treeview):
        records = treeview.get_children()
        # print(records)
        for i in records:
            treeview.delete(i)

    def borrar_carrito(self, tabla_origen ,treeview):
        records = treeview.get_children()
        try:
            if messagebox.askquestion("Borrar Carrito", "Desea borrar el carrito)"):
                if len(records)>0:

                    for i in records:
                        data = treeview.item(i)
                        buscar =data["values"][0]
                        producto = self.table_producto.sql_search("nombre", buscar)
                        dato = self.table_producto.get_one_sql("id", producto[0])
                        # print(type(data['text']), type(dato[2]))
                        suma = self._sumar_cantidad(int(data['text']), dato[2])
                        self.table_producto.update_sql(id=dato[0], stock=suma)
                        treeview.delete(i)
                    self._refresh_treeview(tabla_origen)
                    self._get_products(tabla_origen)
                else:
                    messagebox.showwarning("Borrar carrito", "No hay items que borrar")
        except:
            messagebox.showerror("Error Carrito", "No se pudo borrar el carrito")

    def preparar_compra(self, treeview):
        records = treeview.get_children()
        total = 0
        lista = []
        items = 0
        for i in records:
            data = treeview.item(i)
            listar = [data['text'], data['values'][0], data['values'][2]]
            total +=  float(listar[2])
            lista.append(listar)
            items += int(data['text'])
        return(lista, total, items)

    def cancelar_compra(self, window):
        window.destroy()
    
    def comprar(self, usuario, lista):
        print(lista, usuario)
        print("guardar_carrito----------")
        # self.guardar_carrito(usuario)
        for i in lista[0]:
            print(i)
        fecha_hora = datetime.now()
        format_fecha = fecha_hora.strftime('%d/%m/%Y - %H:%m:%S')
        self.guardar_carrito(usuario, lista, format_fecha)

    def guardar_carrito(self, usuario, lista, fecha):
        buscar_usuario = self.table_usuario.sql_search("usuario", usuario)
        usuario_completo = self.table_usuario.get_one_sql("id", buscar_usuario[0])
        self.table.insert_sql(
            'usuario, direccion, lista_productos, total, cantidad_productos, fecha_hora',
            f'"{usuario_completo[1]}", "{usuario_completo[4]}", "{lista[0]}", "{lista[1]}", "{lista[2]}", "{fecha}"')
