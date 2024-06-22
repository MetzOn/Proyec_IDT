from Controladores.ControladorLogin import LoginController
from Modelo.DAOAutenticacion import AutenticacionDAO
from Vista.GUILogin import LoginGUI

if __name__ == "__main__":
    view = LoginGUI()
    model = AutenticacionDAO()
    controller = LoginController(view, model)
    controller.run()

#from Controladores.ControladorPrincipal import PrincipalControlador
#from Modelo.DAOEmpleado import EmpleadoDAO
#from Modelo.DAOImagen import ImagenDAO
#from Vista.GUIPrincipal import PrincipalGUI

#if __name__ == "__main__":
    #view = PrincipalGUI()
    #modelEmpleado = EmpleadoDAO()
   # modelImagen = ImagenDAO()
    #controller = PrincipalControlador(view, modelEmpleado,modelImagen)
    #controller.run()
