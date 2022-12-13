from sqlite3 import IntegrityError
from database.crear_tablas import CrearDB
from tkinter import messagebox
from views import v_usuario, v_admin


class Usuario:
    def __init__(self, usuario, contrasenia, correo, direccion, is_admin):
        self.__usuario= usuario
        self.__contrasenia  = contrasenia        
        self.__correo  = correo
        self.__direccion = direccion
        self.__is_admin  = is_admin
        self.__columnas = """(
                                "id"	INTEGER NOT NULL,
                                "usuario"	VARCHAR(50) NOT NULL UNIQUE,
                                "contrasenia"	VARCHAR(50) NOT NULL,
                                "correo"	VARCHAR(50),
                                "direccion"	VARCHAR(100),
                                "is_admin" 	INTEGER(1) NOT NULL,
                                PRIMARY KEY("id" AUTOINCREMENT)
                                )"""
        self.table = CrearDB('usuario', self.__columnas)
        self.table.crear_tabla()

    def get_usuario(self):
        return self.__usuario
    def get_correo(self):
        return self.__correo
    def get_direccion(self):
        return self.__direccion
    def get_contrasenia(self):
        return self.__contrasenia
    def get_is_admin(self):
        return self.__is_admin
    
    def set_usuario(self, new_usuario):
        self.__usuario = new_usuario
        return self.__usuario

    def set_correo(self, new_correo):
        self.__correo = new_correo
        return self.__correo

    def set_direccion(self, new_direccion):
        self.__direccion = new_direccion
        return self.__direccion

    def set_contrasenia(self, new_contrasenia):
        self.__contrasenia = new_contrasenia
        return self.__contrasenia

    def set_is_admin(self, new_condicion):
        self.__is_admin = new_condicion
        return self.__is_admin

    def _borrar_entradas(self, *args):
        for x in args:
            x.set('')
    
    def _deshabilitar_boton(self, *args):
        for x in args:
            try:
                x.config(state='disabled')
            except:
                pass
    
    def _habilitar_boton(self, *args):
        for x in args:
            try:
                x.config(state='normal')
            except:
                pass
    
    def comprobar_usuario(self, window, usuario, contrasenia):
        try:
            
            self.valor = self.table.sql_search('usuario', usuario.get())

            if self.valor[2] == 1:
                window.destroy()
                return v_admin.VistaAdministrador(usuario.get())
            if self.valor[1] == contrasenia.get():
                
                window.destroy()
                ventana=v_usuario.VistaUsuario(usuario.get())
                return ventana
            messagebox.showwarning("Datos incorrectos", "Por favor verifique su contraseña y usuario")
            self._borrar_entradas(usuario, contrasenia)
        except:
            return messagebox.showwarning("No ingresó datos", "Por favor ingrese Usuario y contraseña para continuar")
    
    def crear_usuario(self, crear_user, contrasenia_repeat, window, boolean, *args):
        
        condicion = crear_user.get_contrasenia().find('') == 0 and crear_user.get_usuario().find('') == 0
        condicion_2 = crear_user.get_contrasenia().find(' ') == -1 and crear_user.get_usuario().find(' ') == -1
        condicion_3 = len(crear_user.get_usuario()) > 5 and len(crear_user.get_usuario())<12
        condicion_4 = len(crear_user.get_contrasenia()) > 8 and len(crear_user.get_contrasenia())<20
        
        if not condicion_3:
            return messagebox.showwarning("Usuario", "El usuario debe tener mas de 5 caracteres y menos de 12")
        if not condicion_4:
            return messagebox.showwarning("Contraseña", "La contraseña debe tener mas de 8 caracteres y menos de 20")
        if condicion and condicion_2:
            if crear_user.get_contrasenia() == contrasenia_repeat:
                try:
                    self.table.insert_sql(
                            'usuario, contrasenia, correo, direccion, is_admin',
                            f"'{crear_user.get_usuario()}',\
                            '{crear_user.get_contrasenia()}',\
                            '{crear_user.get_correo()}',\
                            '{crear_user.get_direccion()}',\
                            {crear_user.get_is_admin()}")
                    self._borrar_entradas(*args)
                    boolean.set(0)
                    messagebox.showinfo("Usuario Creado", "Se ha creado con éxito el usuario")
                    window.destroy()
                    if 1 != crear_user.get_is_admin():
                        return v_usuario.VistaUsuario(crear_user.get_usuario())
                    else:
                        return v_admin.VistaAdministrador(crear_user.get_usuario())
                except IntegrityError:
                    return messagebox.showerror("Error","El usuario ya existe intente con otro")
            return messagebox.showwarning("Contraseña incorrecta", "Por favor verifique si las contraseñas son iguales")
        else:
            return messagebox.showwarning("Sin espacios ni vacios", "Por favor no deje espacios y complete los campos de usuario y contraseña")

    def mostrar_formulario(self, frame, *args):
            frame.pack_forget()
            frame.destroy()
            self._deshabilitar_boton(*args)
    
    def reset_pass(self, usuario: str, psw_1: str, psw_2:str, window: object, *args):
        
        if not len(psw_1.get()) > 8 and len(psw_1.get())<20:
            return messagebox.showwarning("Contraseña", "La contraseña debe tener mas de 8 caracteres y menos de 20")

        existe_usuario = self.table.sql_search("usuario", usuario.get())

        if existe_usuario == False:
            print("No existe el usuario")
            return messagebox.showwarning("Usuario", "No existe el usuario")
        if psw_1.get() != psw_2.get():
            return messagebox.showerror("Contraseñas", "No coinciden las contraseñas")
        if len(psw_1.get()) == 0:
            return messagebox.showerror("Contraseña vacía","No puede ser una contraseña vacía")
        self.table.update_sql(id=existe_usuario[0], contrasenia=psw_1.get())
        messagebox.showinfo("Contraseña", "Contraseña actualizada correctamente")
        self._habilitar_boton(*args)
        window.destroy()
    
    def close_win(self, window, boton):
        self._habilitar_boton(boton)
        window.destroy()

    def usuarios(self, treeview):

        db_rows = self.table.get_sql()
        for row in db_rows:
            treeview.insert('', 0, text=row[0], values=(
                row[1], row[2], row[3], row[4], row[5]))

