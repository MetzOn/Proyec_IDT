import flet as ft
import cv2
import imutils
import base64
from Modelo.DAOEmpleado import EmpleadoDAO
from Modelo.DTOEmpleado import EmpleadoDTO
from Modelo.DAOImagen import ImagenDAO
from Modelo.DTOImagen import ImagenDTO
from Vista.GUIPrincipal import PrincipalGUI

class PrincipalControlador:
    def __init__(self, view: PrincipalGUI, EmpleadoDao: EmpleadoDAO,ImagenDao: ImagenDAO):
        self.view = view
        self.modelEmpleado = EmpleadoDao
        self.modelImagen = ImagenDao
        self.cap=None
        self.imagenes = []
        self.view.btnCrearEmpleado.on_click = self.Click_CrearEmpleado
        self.view.btnTomarImagenes.on_click=self.Click_videoRegistroTomarImagenes
  
    #REGISTRO
    def Click_videoRegistroTomarImagenes(self,e):
        self.view.btnTomarImagenes.disabled=True
        self.view.btnFinalizarVideo.disabled=False
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        count = 0
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while True:
            ret, frame = self.cap.read()  # Capta los frame de los videos
            if ret == False:
                break
            frame = imutils.resize(frame, width=640)  # Se redimenciona el frame por si es muy grande
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Se cambia el frame a blanco y negro para mejor precision
            auxFrame = frame.copy()  # Copia los frames leidos
            faces = faceClassif.detectMultiScale(gray, 1.3, 5)  # detecta la posicion de los rostros
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Dibuja un rectángulo alrededor de cada rostro
                rostro = auxFrame[y:y + h, x:x + w]  # Recorta la región del rostro
                rostro = cv2.resize(rostro, (300, 300), interpolation=cv2.INTER_CUBIC)  # Redimensiona el rostro a 150x150 píxeles

                imagen = ImagenDTO()
                imagen.setNombreI('Rostro_{}.jpg'.format(count))
                _, buffer = cv2.imencode('.jpg', rostro)
                imagen.setContenidoI(buffer.tobytes())
                self.imagenes.append(imagen)
                count+=1
                print(count)
            cv2.imshow('frame', frame)  # Muestra el frame con los rectángulos dibujados
            k = cv2.waitKey(1)
            if k == 27 or count >= 15:  # Permite presionar esc para salir de la toma de datos, o se finaliza con 300 imagenes capturadas
                break
        self.cap.release()
        cv2.destroyAllWindows()
        print("Se retornaron buen las imagenes")
        self.view.btnCrearEmpleado.disabled=False
        self.view.btnCrearEmpleado.update()
        return self.imagenes

    def Click_CrearEmpleado(self,e):
        nombre=self.view.getNombreRegistro()
        apellido=self.view.getApellidoRegistro()
        dni=self.view.getDniRegistro()
        telefono=self.view.getTelefonoRegistro()
        permiso=self.view.getPermisoIngresoRegistro()
        tipoEmpleado=self.view.getTipoEmpleadoRegistro()

        empleado=EmpleadoDTO(None,nombre,apellido,dni,None,telefono,tipoEmpleado
                             ,permiso)
        
        resp=self.modelEmpleado.CreateEmpleado(empleado)
        print(resp)
        if(resp):
            IdSospechoso=self.modelEmpleado.obtenerIDEmpleado(dni)
            for imagen in self.imagenes:
                imagen.setIdE(IdSospechoso)
                print(IdSospechoso)
                print(imagen.getNombreI())
                self.modelImagen.CrearImagenes(imagen)
        print("Todo conforme, se subio")
    
    #FUNCIONA TODO LO DE ARRIBA, QUIERO HACER QUE APENAS SE TOMEN LAS FOTOS, SE REQUIERA QUE SE HAYA COMPLETADO LA FASE DE FORMULARIOS PARA EVITAR ESTAN HACIENDO MUHCO Y JALAR DIRECTAMENTE EL NOMBRE E ID DEL SOSPECHOSO, 

    #AHORA ES EL MOMENTO DE LISTAR EMPLEADOS, TAMBIEN GENERA EL ENTRENAMIENTO PARA PODER LUEGO IMPLEMENTAR EL SISTEMA. 
    def Click_ListarEmpleados(): 
        return 1



        


   
    def run(self):
        self.view.page.update()
    
    def main(self,page: ft.Page):
        
        page.add(self.view)

