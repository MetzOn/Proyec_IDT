import flet as ft
from Modelo.DAOAutenticacion import AutenticacionDAO
from Modelo.DTOAutenticacion import AutenticacionDTO
from Vista.GUILogin import LoginGUI
from Controladores.ControladorPrincipal import PrincipalControlador
from Modelo.DAOEmpleado import EmpleadoDAO
from Modelo.DAOImagen import ImagenDAO
from Modelo.DAOHistorial import HistorialDAO
from Vista.GUIPrincipal import PrincipalGUI

class LoginController:
    def __init__(self, view: LoginGUI, model: AutenticacionDAO):
        self.view = view
        self.model = model
        self.is_authenticated=False
        self.view.sign_in_button.on_click = self.handle_sign_in

    def handle_sign_in(self, e):
        username = self.view.get_username()
        password = self.view.get_password()
        usuario = AutenticacionDTO(None, None, username, password)
        
        if self.model.AutenticarUsuario(usuario):
            print("Login successful")
            self.show_principal_view()
        else:
            print("Login failed")
            # Logica del que hacer si la autenticacion no a sido exitosa

    def show_principal_view(self):
        # Inicializa la vista y el modelo para la sección principal
        principal_view = PrincipalGUI()
        model_empleado = EmpleadoDAO()
        model_imagen = ImagenDAO()
        model_historial=HistorialDAO()
        principal_controller = PrincipalControlador(principal_view, model_empleado, model_imagen,model_historial)
        
        # Elimina la vista de inicio de sesión y agrega la vista principal
        self.view.page.clean()
        self.view.page.window_min_height=820
        self.view.page.window_min_width=1100
        self.view.page.theme_mode=ft.ThemeMode.SYSTEM
        self.view.page.add(principal_view)
        self.view.page.update()
        principal_controller.run()

    def run(self):
        ft.app(target=self.main)

    def main(self, page: ft.Page):
        
        page.window_width = 580
        page.window_height = 740
        page.padding = 0
        page.add(self.view.body)
        self.view.page = page