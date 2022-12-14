
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Canvas, Toplevel, Button, PhotoImage, StringVar
from model.carrito import Carrito


class Comprar:
    def __init__(self, usuario, tabla_carrito):
        self.__tabla_carrito = tabla_carrito
        self.__usuario = usuario    
        self.carrito = Carrito(self.__usuario, None)    
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets_comprar\frame0")

        self.carrito_preparado = self.carrito.preparar_compra(self.__tabla_carrito)
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        self.window_2 = Toplevel()

        self.window_2.geometry("402x268")
        self.window_2.configure(bg = "#FFFFFF")


        canvas = Canvas(
            self.window_2,
            bg = "#FFFFFF",
            height = 268,
            width = 402,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            104.0,
            140.0,
            anchor="nw",
            text="Comprador:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        canvas.create_text(
            152.0,
            94.0,
            anchor="nw",
            text="Total:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        canvas.create_text(
            16.0,
            48.0,
            anchor="nw",
            text="Cantidad de productos:",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.dato_comprador = StringVar()
        self.dato_comprador.set("DATO_COMPR")
        canvas.create_text(
            214.0,
            140.0,
            anchor="nw",
            text=self.__usuario,
            fill="#0019FF",
            font=("Inter", 16 * -1)
        )

        canvas.create_text(
            214.0,
            94.0,
            anchor="nw",
            text=f"${self.carrito_preparado[1]}",
            fill="#0019FF",
            font=("Inter", 16 * -1)
        )

        canvas.create_text(
            214.0,
            48.0,
            anchor="nw",
            text=self.carrito_preparado[2],
            fill="#0019FF",
            font=("Inter", 16 * -1)
        )


        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self.window_2,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.carrito.comprar(self.window_2, self.__tabla_carrito, self.__usuario, self.carrito_preparado),
            relief="flat"
        )
        button_1.place(
            x=39.0,
            y=206.0,
            width=132.0,
            height=26.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.window_2,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.carrito.cancelar_compra(self.window_2),
            relief="flat"
        )
        self.button_2.place(
            x=219.0,
            y=206.0,
            width=132.0,
            height=26.0
        )

        canvas.create_text(
            166.0,
            12.0,
            anchor="nw",
            text="COMPRA",
            fill="#000000",
            font=("Inter", 16 * -1)
        )
        self.window_2.resizable(False, False)
        self.window_2.mainloop()
