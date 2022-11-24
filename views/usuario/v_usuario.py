from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, ttk, Label, Scrollbar, IntVar, messagebox
# from database import producto_db
# from clases.producto import get_products, record
# from clases.carrito import Carrito


class VistaUsuario:
    def __init__(self):
        
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / \
            Path(r"assets\frame0")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        self.window = Tk()

        self.window.geometry("987x751")
        self.window.configure(bg="#FFFFFF")
        self.insertar_producto=[]

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
            command=lambda: print("button_1 clicked"),
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
            command=lambda: print("button_3 clicked"),
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
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: insertar_en_carrito(self.tabla_carrito, self.entrada.get(), self.insertar_producto),####################################
            command=lambda: self.carrito.insertar_en_carrito(
                self.tabla_carrito, self.entrada.get(),
                self.insertar_producto,
                self.descripcion,
                self.precio,
                self.stock,
                self.product,
                self.entrada
                ),
            relief="flat"
        )
        self.button_5.place(
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
        
        self.descripcion_text=''
        self.descripcion = Label(text=self.descripcion_text,
            font=("Inter", 16 * -1),
            wraplength= 170, 
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
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

        self.stock = Label(
            text=self.stock_text,
            font=("Inter", 16 * -1),
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
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

        self.precio_text= ''
        self.precio = Label(
            text=self.precio_text,
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

        self.producto_text = ''

        self.product = Label(
            text=self.producto_text,
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
                                columns=('col1', 'col2', 'col3', 'col4'))

        # self.tabla.configure("mystyle.Treeview", background='light blue')

        self.tabla.place(
            x=0,
            y=0,
            width=670.0,
            height=379.0
        )
        self.tabla.column('#0', width=30)
        self.tabla.column('col1', width=100)
        self.tabla.column('col2', width=50)
        self.tabla.column('col3', width=50)
        self.tabla.column('col4', width=150)


        self.tabla.heading('#0', text='ID')
        self.tabla.heading('col1', text='NOMBRE')
        self.tabla.heading('col2', text='STOCK')
        self.tabla.heading('col3', text='PRECIO')
        self.tabla.heading('col4', text='DESCRIPCIÓN')

        self.barra = Scrollbar(self.caja_2, orient='vertical', 
                                command=self.tabla.yview)

        self.barra.place(
            x=654,
            y=0,
            bordermode='inside',
            height=379
            
        )

        self.tabla.config(yscrollcommand=self.barra.set)

        

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
            text="tabla_Carrito:",
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
            text="BIENVENIDO USUARIO",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        

        self.window.resizable(False, False)
        self.window.mainloop()


    def on_tree_select(self, tabla):
        
        self.current_item = self.tabla.focus()
        if not self.current_item:
            return
        data = self.tabla.item(self.current_item)
        
        data = data["values"]
        
        self.descripcion.config(text=data[3])
        self.precio.config(text=data[2])
        self.stock.config(text=data[1])
        self.product.config(text=data[0])
        self.insertar_producto = []
        self.capturar_datos(data)
    
    def capturar_datos(self, data):
        # self.insertar_producto.append(self.entrada.get())
        self.insertar_producto.append(data[0])
        self.insertar_producto.append(data[2])
        self.insertar_producto.append(data[3])

    def capturar_entrada(self):
        try: 
            return self.entrada.get()
        except:
            return messagebox.showerror("Error de datos", "Por favor compruebe el dato ingresado")

# vista = VistaUsuario()