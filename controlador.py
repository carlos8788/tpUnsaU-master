from views.v_inicio import Bienvenida
# from clases.usuario import Usuario
# from views.v_usuario import VistaUsuario
# figd_oF_MCyXRkIDqKsf5GTY_92-iPN8ZM7i-D0LHbXSP

class Controller:
    # vista_usuario = VistaUsuario()
    vista_bienvenida = Bienvenida()
    # vista_bienvenida.abrir_vista(VistaUsuario())

if __name__ == "__main__":
    controlador = Controller()
    # usuario = Usuario('luis', 'perez', 'cualcuiera', 'perez', 1)
    # print(usuario.get_usuario(), usuario.get_contrasenia())
    # comprobar = usuario.comprobar_usuario(usuario.get_usuario(), usuario.get_contrasenia())
    # print(comprobar)