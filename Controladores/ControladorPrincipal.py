import flet as ft
from Modelo.DAOEmpleado import EmpleadoDAO
from Modelo.DAOImagen import ImagenDAO
from Vista.GUIPrincipal import PrincipalGUI

class PrincipalControlador:
    def __init__(self, view: PrincipalGUI, EmpleadoDao: EmpleadoDAO,ImagenDao: ImagenDAO):
        self.view = view
        self.modelEmpleado = EmpleadoDao
        self.modelImagen = ImagenDao
        self.view.btnCrearEmpleado.on_click = self.Click_CrearEmpleado

    def Click_CrearEmpleado(self,e):
        nombre=self.view.getNombreRegistro()
        apellido=self.view.getApellidoRegistro()
        dni=self.view.getDniRegistro()
        telefono=self.view.getTelefonoRegistro()
        permiso=self.view.getPermisoIngresoRegistro()
        tipoEmpleado=self.view.getTipoEmpleadoRegistro()
        print(nombre+"  "+apellido+"  "+dni+"  "+telefono+"  "+permiso+"  "+tipoEmpleado)


   
    def run(self):
        self.view.page.update()
    
    def main(self,page: ft.Page):
        
        page.add(self.view)

