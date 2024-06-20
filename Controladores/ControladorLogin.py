import flet as ft
from Modelo.DAOAutenticacion import AutenticacionDAO
from Modelo.DTOAutenticacion import AutenticacionDTO
from Vista.GUILogin import LoginGUI

class LoginController:
    def __init__(self, view: LoginGUI, model: AutenticacionDAO):
        self.view = view
        self.model = model
        self.view.sign_in_button.on_click = self.handle_sign_in

    def handle_sign_in(self, e):
        username = self.view.get_username()
        password = self.view.get_password()
        Usuario=AutenticacionDTO(None,None,username,password)
        if self.model.AutenticarUsuario(Usuario):
            print("Login successful")
            # Logica del que hacer si la autenticacion a sido exitosa
        else:
            print("Login failed")
            # Logica del que hacer si la autenticacion no a sido exitosa

    def run(self):
        ft.app(target=self.main)

    def main(self, page: ft.Page):
        page.window_max_width = 580
        page.window_max_height = 740
        page.padding = 0
        page.add(self.view.body)

