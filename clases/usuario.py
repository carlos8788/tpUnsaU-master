class Usuario:
    def __init__(self, nombre, correo, direccion, contrasenia, is_admin):
        self.__nombre= nombre        
        self.__correo  = correo
        self.__direccion = direccion
        self.__contrasenia  = contrasenia
        self.__is_admin  = is_admin
    
    def get_nombre(self):
        return self.__nombre
    def get_correo(self):
        return self.__correo
    def get_direccion(self):
        return self.__direccion
    def get_contrasenia(self):
        return self.__contrasenia
    def get_is_admin(self):
        return self.__is_admin
    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
        return self.__nombre

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

