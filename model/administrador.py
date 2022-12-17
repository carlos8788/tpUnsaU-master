from database.crear_tablas import CrearDB
from model.producto import Producto
# from model.usuario import Usuario

from tkinter import messagebox
class Administrador:

    def __init__(self):
        self.tabla_producto = CrearDB('producto', None)
        self.producto = Producto(None, None, None, None, None)
        # self.usuario = Usuario(None, None, None, None, None)
        
        self.tabla_usuario = CrearDB("usuario", None)

        self.tabla_carrito = CrearDB("carrito", None)
    
    def agregar_producto(self, window, treeview, *args):
        a = str(args[0])
        a = a[1:-1]
        b = str(args[1])
        b = b[1:-1]
        self.tabla_producto.insert_sql(a, b)
        
        self.producto.record(treeview)
        self.producto.get_products(treeview)
        messagebox.showinfo("Agregar producto", "El producto fue agregado correctamente")
        window.destroy()
        

    def editar_producto(self, window, treeview, *args):
        
        self.tabla_producto.update_sql(
            id=args[0], 
            nombre=args[1], 
            stock=args[2], 
            precio=args[3], 
            categoria=args[4], 
            descripcion=args[5]
            )
        self.producto.record(treeview)
        self.producto.get_products(treeview)
        messagebox.showinfo("Editar producto", "El producto fue editó correctamente")
        window.destroy()
    
    def eliminar_producto(self, treeview, id):
        variable = messagebox.askquestion("Eliminar", "Desea eliminar el producto?")
        
        if variable == "yes":

            self.tabla_producto.delete_sql("id", id)
            self.producto.record(treeview)
            self.producto.get_products(treeview)
            messagebox.showinfo("Eliminar producto", "El producto fue eliminado correctamente")
    
    def get_carritos(self, treeview):

        db_rows = self.tabla_carrito.get_sql()
        
        for row in db_rows:
            treeview.insert('', 0, text=row[0], values=(
                row[1], row[2], row[3], row[4], row[5]))

    def get_usuarios(self, treeview):

        db_rows = self.tabla_usuario.get_sql()
        
        for row in db_rows:
            treeview.insert('', 0, text=row[0], values=(
                row[1], row[2], row[3], row[4], row[5]))

    def editar_usuario(self, window, treeview, *args):
        self.tabla_usuario.update_sql(
            id=args[0], 
            usuario=args[1], 
            contrasenia=args[2], 
            correo=args[3], 
            direccion=args[4]
            )
        self.producto.record(treeview)
        self.get_usuarios(treeview)
        messagebox.showinfo("Editar usuario", "El usuario se editó correctamente")
        window.destroy()

    def eliminar_usuario(self, treeview, id):
        variable = messagebox.askquestion("Eliminar", "Desea eliminar el usuario?")
        
        if variable == "yes":
            self.tabla_usuario.delete_sql("id", id)
            self.producto.record(treeview)
            self.get_usuarios(treeview)
            messagebox.showinfo("Eliminar usuario", "El usuario fue eliminado correctamente")
    
    def eliminar_carrito(self, treeview, id):
        variable = messagebox.askquestion("Eliminar", "Desea eliminar el carrito?")
        
        if variable == "yes":
            self.tabla_carrito.delete_sql("id_carrito", id)
            self.producto.record(treeview)
            self.get_carritos(treeview)
            messagebox.showinfo("Eliminar carrito", "El carrito fue eliminado correctamente")