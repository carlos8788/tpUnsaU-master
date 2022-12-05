from pathlib import Path
# import __init__
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Frame, ttk, Label, Scrollbar, IntVar, messagebox, StringVar

# from database import producto_db
# from clases.producto import get_products, record
from model.carrito import Carrito
from model.producto import Producto


class VistaUsuario:
    def __init__(self, nombre_usuario):
        self.__nombre_usuario = nombre_usuario

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / \
            Path(r"assets_usuario\frame0")

        self.producto = Producto(None, None, None, None, None)
        self.carrito = Carrito(None, None)
        self.lista = []
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.window = Tk()

        self.window.geometry("987x751")
        self.window.configure(bg="#FFFFFF")
        # self.insertar_producto = []

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=751,
            width=987,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: self.carrito.comprar(),
            command=lambda: print("boton comprar"),
            relief="flat"
        )
        self.button_1.place(
            x=791.0,
            y=706.0,
            width=176.0,
            height=38.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=791.0,
            y=603.0,
            width=176.0,
            height=38.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.carrito.borrar_item(self.tabla_carrito),
            relief="flat"
        )
        self.button_3.place(
            x=791.0,
            y=536.0,
            width=176.0,
            height=38.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=791.0,
            y=469.0,
            width=176.0,
            height=38.0
        )

        # self.carrito = Carrito("Luis", "lista", 200)

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.agregar_a_carrito = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: insertar_en_carrito(self.tabla_carrito, self.entrada.get(), self.insertar_producto),####################################
            # command=lambda: print(self.lista),
            command=lambda: self.carrito.insertar_en_carrito(
                self.tabla_carrito, 
                self.lista,
                self.entrada,
                self.descripcion,
                self.precio,
                self.stock,
                self.product,
                self.entrada
                ),
            relief="flat"
        )
        self.agregar_a_carrito.place(
            x=793.0,
            y=383.0,
            width=176.0,
            height=38.0
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            882.5,
            231.5,
            image=self.entry_image_1
        )

        self.descripcion_text= StringVar()
        # self.descripcion_text.set(' ')
        self.descripcion = Label(text=self.descripcion_text.set(''),
                                 font=("Inter", 16 * -1),
                                 wraplength=170,
                                 bd=0,
                                 bg="#D9D9D9",
                                 fg="#000716",
                                 highlightthickness=0,
                                #  textvariable=self.descripcion_text
                                 )

        self.descripcion.place(
            x=793.0,
            y=191.0,
            width=179.0,
            height=79.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            882.5,
            153.5,
            image=self.entry_image_2
        )

        self.stock_text = ''
        self.stock_var = StringVar()
        # self.stock_var
        self.stock = Label(
            text=self.stock_text,
            font=("Inter", 16 * -1),
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            # textvariable=self.stock_var
        )

        self.stock.place(
            x=793.0,
            y=139.0,
            width=179.0,
            height=27.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            882.5,
            101.5,
            image=self.entry_image_3
        )

        self.precio_text = StringVar()
        self.precio = Label(
            text=self.precio_text.set(''),
            font=("Inter", 16 * -1),
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.precio.place(
            x=793.0,
            y=87.0,
            width=179.0,
            height=27.0
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            882.5,
            56.5,
            image=self.entry_image_4
        )

        self.producto_text = StringVar()

        self.product = Label(
            text=self.producto_text.set(''),
            font=("Inter", 16 * -1),
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.product.place(
            x=793.0,
            y=42.0,
            width=179.0,
            height=27.0
        )

        self.canvas.create_text(
            699.0,
            41.0,
            anchor="nw",
            text="Producto:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            699.0,
            93.0,
            anchor="nw",
            text="Precio:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            699.0,
            145.0,
            anchor="nw",
            text="Stock:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            882.5,
            308.5,
            image=self.entry_image_5
        )
        self.entrada = IntVar()
        self.entrada.set('')

        self.entry_5 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.entrada
        )
        self.entry_5.place(
            x=793.0,
            y=294.0,
            width=179.0,
            height=27.0
        )

        self.canvas.create_text(
            699.0,
            295.0,
            anchor="nw",
            text="Cantidad \na comprar:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            699.0,
            220.0,
            anchor="nw",
            text="Descripción:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        # ----------------- TreeView ---- Importamos ttk-------------

        self.caja_2 = Frame(self.window, bg='#c8c6ae')
        # caja_2.grid(row=5, column=0)
        self.caja_2.place(
            x=14.0,
            y=42.0,
            width=670.0,
            height=379.0
        )

        # ----------------- TABLA ---------------------

        self.tabla = ttk.Treeview(self.caja_2,
                                  columns=('col1', 'col2', 'col3', 'col4', 'col5'))

        # self.tabla.configure("mystyle.Treeview", background='light blue')

        self.tabla.place(
            x=0,
            y=0,
            width=670.0,
            height=379.0
        )
        self.tabla.column('#0', width=30)
        self.tabla.column('col1', width=75)
        self.tabla.column('col2', width=50)
        self.tabla.column('col3', width=50)
        self.tabla.column('col4', width=100)
        self.tabla.column('col5', width=75)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('col1', text='NOMBRE')
        self.tabla.heading('col2', text='STOCK')
        self.tabla.heading('col3', text='PRECIO')
        self.tabla.heading('col4', text='CATEGORIA')
        self.tabla.heading('col5', text='DESCRIPCIÓN')

        self.barra = Scrollbar(self.caja_2, orient='vertical',
                               command=self.tabla.yview)
        
        self.barra.place(
            x=654,
            y=0,
            bordermode='inside',
            height=379

        )

        self.tabla.config(yscrollcommand=self.barra.set)

        self.producto.get_products(self.tabla)
        # record(self.tabla)
        # get_products(self.tabla)

        self.tabla.bind("<<TreeviewSelect>>", self.on_tree_select)
        

        self.caja_3 = Frame(self.window)

        self.caja_3.place(
            x=14.0,
            y=469.0,
            width=671.0,
            height=278.0
        )
        self.tabla_carrito = ttk.Treeview(self.caja_3,
                                          columns=('col1', 'col2', 'col3'))
        self.tabla_carrito.place(
            x=0,
            y=0,
            width=671.0,
            height=278.0
        )

        self.barra_2 = Scrollbar(self.caja_3, orient='vertical',
                                 command=self.tabla.yview)

        self.barra_2.place(
            x=654,
            y=0,
            bordermode='inside',
            height=278

        )

        self.tabla_carrito.config(yscrollcommand=self.barra_2.set)

        self.tabla_carrito.column('#0', width=50)
        self.tabla_carrito.column('col1', width=100)
        self.tabla_carrito.column('col2', width=100)
        self.tabla_carrito.column('col3', width=100)

        self.tabla_carrito.heading('#0', text='CANTIDAD')
        self.tabla_carrito.heading('col1', text='NOMBRE')
        self.tabla_carrito.heading('col2', text='PRECIO')
        self.tabla_carrito.heading('col3', text='SUBTOTAL')

        # self.tabla_carrito.insert('', 0, text=self.entrada.get(), values=(
        #     "args[1]", "args[2]", "args[3]"))

        self.canvas.create_text(
            14.0,
            450.0,
            anchor="nw",
            text="Carrito:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            15.0,
            21.0,
            anchor="nw",
            text="Productos:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            407.0,
            2.0,
            anchor="nw",
            text=f"BIENVENIDO {self.__nombre_usuario}",
            fill="#000000",
            font=("Inter", 16 * -1)
        )
        self.tabla_carrito.bind("<<TreeviewSelect>>", self.hola)
        


        ################### COMBOBOX ####################
        self.canvas.create_text(
            620,
            2.0,
            anchor="nw",
            text="CATEGORIAS:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )
        self.lista = self.producto.mostrar_categorias()

        self.combo = ttk.Combobox(
            self.window,
            values=self.lista,
        )
        self.combo.set('TODAS')

        self.combo.bind("<<ComboboxSelected>>",
                        self.selection_changed)
        self.combo.place(x=728, y=2)

        self.window.resizable(False, False)
        self.window.mainloop()

    def selection_changed(self, evento):
        selection = self.combo.get()
        self.producto.cargar_categoria(selection, self.tabla)
        
        
    def on_tree_select(self, tabla):
        self.lista.clear()
        self.current_item = self.tabla.focus()
        if not self.current_item:
            return
        data = self.tabla.item(self.current_item)
        # print(data)
        data = data["values"]

        self.descripcion.config(text=data[4])
        self.precio.config(text=data[2])
        self.stock.config(text=data[1])
        self.product.config(text=data[0])
        self.lista.append(data[0])
        self.lista.append(data[2])
        # print(self.lista)

    def hola(self, evento):
        records = self.tabla_carrito.focus()
        data = self.tabla_carrito.item(records)
        print(data["text"], data["values"])

    
            

    def capturar_entrada(self):
        try:
            return self.entrada.get()
        except:
            return messagebox.showerror("Error de datos", "Por favor compruebe el dato ingresado")

# vista = VistaUsuario()
