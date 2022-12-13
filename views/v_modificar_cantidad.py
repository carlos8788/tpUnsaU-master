
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Label, Button, PhotoImage, Toplevel, IntVar
from model.carrito import Carrito


class ModificarCantidad:
    def __init__(self, tabla_origen, tabla_destino):
        try:

            OUTPUT_PATH = Path(__file__).parent
            ASSETS_PATH = OUTPUT_PATH / Path(r"assets_mod_cant\frame0")

            self.carrito = Carrito(None, None)

            def relative_to_assets(path: str) -> Path:
                return ASSETS_PATH / Path(path)

            self.window_2 = Toplevel()
            self.item = self.carrito.mostrar_producto(self.window_2, tabla_origen, tabla_destino)

            self.window_2.geometry("552x353+150+400")
            self.window_2.configure(bg="#FFFFFF")
            self.window_2.overrideredirect(True)
            self.window_2.wm_attributes("-topmost", True)
            
            self.canvas = Canvas(
                self.window_2,
                bg="#CEF6F5",
                height=353,
                width=552,
                bd=0,
                highlightthickness=0,
                relief="ridge"
            )

            self.canvas.place(x=0, y=0)
            self.entry_image_1 = PhotoImage(
                file=relative_to_assets("entry_1.png"))
            self.entry_bg_1 = self.canvas.create_image(
                306.5,
                162.5,
                image=self.entry_image_1
            )
            self.nueva_cantidad = IntVar()
            self.entry_1 = Entry(
                self.window_2,
                bd=0,
                bg="#FFD2D2",
                fg="#000716",
                highlightthickness=0,
                textvariable=self.nueva_cantidad
            )
            self.entry_1.place(
                x=217.0,
                y=148.0,
                width=179.0,
                height=27.0
            )

            self.cant_max = Label(
                self.window_2,
                text=self.item[2],
                font=("Inter", 16 * -1),
                wraplength=170,
                bd=0,
                bg="#FFD2D2",
                fg="#000716",
                highlightthickness=0,
 
            )

            self.cant_max.place(
                x=217.0,
                y=84.0,
                width=179.0,
                height=27.0
            )

            self.canvas.create_text(
                140.0,
                150.0,
                anchor="nw",
                text="Cantidad:",
                fill="#000000",
                font=("Inter", 16 * -1)
            )

            self.canvas.create_text(
                79.0,
                87.0,
                anchor="nw",
                text="Cantidad máxima:",
                fill="#000000",
                font=("Inter", 16 * -1)
            )

            self.canvas.create_text(
                215.0,
                22.0,
                anchor="nw",
                text="MODIFICAR CANTIDAD",
                fill="#000000",
                font=("Inter", 16 * -1)
            )

            self.button_image_1 = PhotoImage(
                file=relative_to_assets("button_1.png"))
            self.cancelar = Button(
                self.window_2,
                image=self.button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.window_2.destroy(),
                relief="flat"
            )
            self.cancelar.place(
                x=307.0,
                y=216.0,
                width=179.0,
                height=38.0
            )

            self.button_image_2 = PhotoImage(
                file=relative_to_assets("button_2.png"))
            self.actualizar = Button(
                self.window_2,
                image=self.button_image_2,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.carrito.modificar_cantidad(self.window_2, tabla_origen, tabla_destino,self.item, self.nueva_cantidad.get()),
                relief="flat"
            )
            self.actualizar.place(
                x=79.0,
                y=216.0,
                width=179.0,
                height=38.0
            )
            
            self.window_2.resizable(False, False)
            self.window_2.mainloop()
        except:
            pass

