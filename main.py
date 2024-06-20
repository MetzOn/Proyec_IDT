from Controladores.ControladorLogin import LoginController
from Modelo.DAOAutenticacion import AutenticacionDAO
from Vista.GUILogin import LoginGUI

if __name__ == "__main__":
    view = LoginGUI()
    model = AutenticacionDAO()
    controller = LoginController(view, model)
    controller.run()