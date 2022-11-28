from sqlite3 import IntegrityError
from database.crear_tablas import CrearDB
from tkinter import messagebox
from views import v_usuario

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

    def comprobar_usuario(self, window, usuario, contrasenia):
        self.valor = self.table.sql_search('usuario', usuario.get())
        if self.valor == contrasenia.get():
            window.destroy()
            ventana=v_usuario.VistaUsuario()
            return ventana
        messagebox.showwarning("Datos incorrectos", "Por favor verifique su contraseña y usuario")
        self._borrar_entradas(usuario, contrasenia) 
    
    def crear_usuario(self, crear_user, contrasenia_repeat):
        if crear_user.get_contrasenia() == contrasenia_repeat:
            try:
                self.table.insert_sql(
                        'usuario, contrasenia, correo, direccion, is_admin',
                        f"'{crear_user.get_usuario()}',\
                        '{crear_user.get_contrasenia()}',\
                        '{crear_user.get_correo()}',\
                        '{crear_user.get_direccion()}',\
                        {crear_user.get_is_admin()}")
                return messagebox.showinfo("Usuario Creado", "Se ha creado con éxito el usuario")
            except IntegrityError:
                return messagebox.showerror("Error","El usuario ya existe intente con otro")
        return messagebox.showwarning("Contraseña incorrecta", "Por favor verifique si las contraseñas son iguales")

    def _borrar_entradas(self, *args):
        for x in args:
            x.set('')
    
if __name__ == "__main__":
    usuario = Usuario('luis', 'perez', 'cualcuiera', 'contrasenia', 1)
    comprobar = usuario.comprobar_usuario(usuario.get_usuario(), usuario.get_contrasenia())
    print(comprobar)