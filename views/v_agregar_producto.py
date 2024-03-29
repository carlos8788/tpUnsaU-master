from tkinter import Toplevel, Label, Entry, Button, StringVar, IntVar, DoubleVar
from model.administrador import Administrador
# from views.v_admin import VistaAdministrador
class AgregarProducto:
    def __init__(self, window, treeview):


        self.admin = Administrador()
        self.window_2 = Toplevel()

        self.window_2.geometry("500x350+150+300")
        self.window_2.configure(bg = "#CDF8B1")
        self.window_2.overrideredirect(True)
        self.window_2.wm_attributes("-topmost", True)

        self.nombre_prod = Label(self.window_2, text='NOMBRE:', anchor='e', bg = "#CDF8B1")
        self.nombre_prod.place(
            x=75,
            y=50,
            width=100
        )
        self.stock_prod = Label(self.window_2, text='STOCK:', anchor='e', bg = "#CDF8B1")
        self.stock_prod.place(
            x=75,
            y=80,
            width=100
        )
        self.precio_prod = Label(self.window_2, text='PRECIO:', anchor='e', bg = "#CDF8B1")
        self.precio_prod.place(
            x=75,
            y=110,
            width=100
        )
        self.categoria_prod = Label(self.window_2, text='CATEGORIA:', anchor='e', bg = "#CDF8B1")
        self.categoria_prod.place(
            x=75,
            y=140,
            width=100
        )
        
        self.descrip_prod = Label(self.window_2, text='DESCRIPCION:', anchor='e', bg = "#CDF8B1")
        self.descrip_prod.place(
            x=75,
            y=170,
            width=100
        )

        self.nombre = StringVar()
        self.stock = IntVar()
        self.precio = DoubleVar()
        self.categoria = StringVar()
        self.descripcion = StringVar()


        self.entry_nombre= Entry(self.window_2, textvariable=self.nombre)
        self.entry_nombre.place(
            x=175,
            y=50,
            width=130,
            
        )
        self.entry_stock= Entry(self.window_2, textvariable=self.stock)
        self.entry_stock.place(
            x=175,
            y=80,
            width=130,
            
        )
        self.entry_precio= Entry(self.window_2, textvariable=self.precio)
        self.entry_precio.place(
            x=175,
            y=110,
            width=130,
            
        )
        self.entry_categoria= Entry(self.window_2, textvariable=self.categoria)
        self.entry_categoria.place(
            x=175,
            y=140,
            width=130,
            
        )
        self.entry_descrip= Entry(self.window_2, textvariable=self.descripcion)
        self.entry_descrip.place(
            x=175,
            y=170,
            width=130,
            
        )

        self.boton_aceptar = Button(
            self.window_2, 
            text="ACEPTAR",
            command=lambda:self.admin.agregar_producto(
                self.window_2,
                treeview,
                ('nombre', 'stock', 'precio', 'categoria', 'descripcion'),
                (self.nombre.get(), self.stock.get(), self.precio.get(), self.categoria.get(), self.descripcion.get()))
            )
        self.boton_aceptar.place(
            x=100,
            y=300,
            width=100,
            height=30
        )

        self.boton_cancelar = Button(
            self.window_2, 
            text="CANCELAR",
            command= lambda: self.window_2.destroy()
            )
        self.boton_cancelar.place(
            x=300,
            y=300,
            width=100,
            height=30
        )

        self.window_2.resizable(True, True)
        self.window_2.mainloop()
