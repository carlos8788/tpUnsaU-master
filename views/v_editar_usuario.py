from tkinter import Toplevel, Label, Entry, Button, StringVar, IntVar, DoubleVar, messagebox
from model.administrador import Administrador

class EditarUsuario:
    def __init__(self, treeview, lista):

        self.lista = lista
        self.admin = Administrador()
        self.window_2 = Toplevel()
        # print(self.lista, "EDIAR")
        self.window_2.geometry("500x350+150+300")
        self.window_2.configure(bg = "#E6D5C2")
        self.window_2.overrideredirect(True)
        self.window_2.wm_attributes("-topmost", True)

        self.lab_usuario = Label(self.window_2, text='USUARIO:', anchor='e', bg = "#E6D5C2")
        self.lab_usuario.place(
            x=75,
            y=50,
            width=100
        )
        self.lab_psw = Label(self.window_2, text='PASSWORD:', anchor='e', bg = "#E6D5C2")
        self.lab_psw.place(
            x=75,
            y=80,
            width=100
        )
        self.lab_correo = Label(self.window_2, text='CORREO:', anchor='e', bg = "#E6D5C2")
        self.lab_correo.place(
            x=75,
            y=110,
            width=100
        )
        self.lab_direccion = Label(self.window_2, text='DIRECCION:', anchor='e', bg = "#E6D5C2")
        self.lab_direccion.place(
            x=75,
            y=140,
            width=100
        )
        
        self.id_usuario = IntVar()
        self.usuario = StringVar()
        self.password = StringVar()
        self.correo = StringVar()
        self.direccion = StringVar()
        
        self.id_usuario.set(lista[0])
        self.usuario.set(lista[1])
        self.password.set(lista[2])
        self.correo.set(lista[3])
        self.direccion.set(lista[4])
        
        

        self.entry_usuario= Entry(self.window_2, textvariable=self.usuario)
        self.entry_usuario.place(
            x=175,
            y=50,
            width=230,
            
        )
        self.entry_password= Entry(self.window_2, textvariable=self.password)
        self.entry_password.place(
            x=175,       
            y=80,
            width=230,
            
        )
        self.entry_correo= Entry(self.window_2, textvariable=self.correo)
        self.entry_correo.place(
            x=175,
            y=110,
            width=230,
            
        )
        self.entry_direccion= Entry(self.window_2, textvariable=self.direccion)
        self.entry_direccion.place(
            x=175,
            y=140,
            width=230,
            
        )
        
        # print(self.id_producto.get())
        self.boton_aceptar = Button(
            self.window_2, 
            text="ACEPTAR",
            command=lambda:self.admin.editar_usuario(
                self.window_2,
                treeview,
                self.id_usuario.get(),
                self.usuario.get(),
                self.password.get(),
                self.correo.get(),
                self.direccion.get(),
                )
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