import flet as ft
import cv2
import imutils
import numpy as np
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
        self.etiqueta_sospechoso_mapping={}
        self.face_recognizer= cv2.face.LBPHFaceRecognizer_create()
        self.view.btnCrearEmpleado.on_click = self.Click_videoRegistroCrearEmpleado
        self.view.btnTomarImagenes.on_click=self.Click_videoRegistroTomarImagenes
        self.view.btnAdministrarEmpleadosPanel.on_click=self.Change_NavRegistroAdmin
        self.view.btnAgregarEmpleadoPanel.on_click=self.Change_NavRegistroCrear
        self.view.btnEliminarEmpleado.on_click=self.EliminarEmpleado
        self.view.btnModificarEmpleado.on_click=self.ActualizarEmpleado
        self.view.btnIniciarReconocimiento.on_click=self.Click_IniciarCamara
        self.selected_row = None
        self.EntrenarSistema()        
  
    #NAVEGACION 
        
    def Change_NavRegistroAdmin(self,e):
        self.view.ContenedorRegistro.content=self.view.ContenedoresResgistro[1]
        self.view.update()
        self.Click_ListarEmpleados()

    def Change_NavRegistroCrear(self,e):
        self.view.ContenedorRegistro.content=self.view.ContenedoresResgistro[0]
        self.view.update()

    #RECONOCIMIENTO VIDEO CAP
    def Click_IniciarCamara(self, e):
        self.faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.face_recognizer.read('ModeloFacesFrontalData2024.xml')
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
        while True:  # Bucle infinito para mantener la visualización continua
            ret, frame = self.cap.read()  # Captura un frame de video
            if ret:  # Si se captura correctamente un frame
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convierte el frame a escala de grises
                auxFrame = gray.copy()  # Copia del frame en escala de grises
                faces = self.faceClassif.detectMultiScale(gray, 1.3, 5)  # Detecta las caras en el frame

                for (x, y, w, h) in faces:  # Itera sobre las coordenadas de las caras detectadas
                    rostro = auxFrame[y:y + h, x:x + w]  # Recorta la región de la cara
                    rostro = cv2.resize(rostro, (300, 300), interpolation=cv2.INTER_CUBIC)  # Redimensiona la cara
                    result = self.face_recognizer.predict(rostro)  # Realiza el reconocimiento facial en la cara
                    
                    if result[1] < 65:  # Si la confianza en el reconocimiento es alta
                        nombre = self.etiqueta_sospechoso_mapping.get(result[0], "No encontrado")  # Obtiene el nombre correspondiente a la etiqueta
                        if nombre != "No encontrado":
                            name = nombre
                        else:
                            name=nombre
                    else:  # Si la confianza en el reconocimiento es baja
                        name = "Desconocido"
                    info_text = f"{name} ({result[1]:.2f})"
                    cv2.putText(frame, info_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)  # Muestra el nombre en el frame
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Dibuja un rectángulo alrededor de la cara reconocida

                cv2.imshow('Reconocimiento Facial', frame)  # Muestra el frame con las caras detectadas
                key = cv2.waitKey(1)  # Espera 1 milisegundo por la pulsación de una tecla
                if key == 27: 
                    self.finalizar_video() # Si se presiona la tecla 'Esc' (27 en ASCII), finaliza la visualización
                    break

    # Finaliza la visualización del video

    def finalizar_video(self):
        # Método para finalizar la visualización del video y liberar los recursos de la cámara
        self.cap.release()  # Libera los recursos de la cámara
        cv2.destroyAllWindows()  # Cierra todas las ventanas de OpenCV





    #REGISTRO
    def Click_videoRegistroTomarImagenes(self,e):
        self.imagenes=[]
        self.view.btnTomarImagenes.disabled=True
        self.view.btnFinalizarVideo.disabled=False
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        count = 0
        frame_skip = 10  # Número de frames a omitir entre cada captura de imagen
        frame_counter = 0
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while True:
            ret, frame = self.cap.read()  # Capta los frame de los videos
            if ret == False:
                break
            frame = imutils.resize(frame, width=640)  # Se redimenciona el frame por si es muy grande
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Se cambia el frame a blanco y negro para mejor precision
            auxFrame = frame.copy()  # Copia los frames leidos
            faces = faceClassif.detectMultiScale(gray, 1.3, 5)  # detecta la posicion de los rostros
            if frame_counter % frame_skip == 0:
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
            frame_counter += 1 
        self.cap.release()
        cv2.destroyAllWindows()
        print("Se retornaron buen las imagenes")
        self.view.btnCrearEmpleado.disabled=False
        self.view.btnTomarImagenes.disabled=False
        self.view.btnCrearEmpleado.update()
        return self.imagenes

    def Click_videoRegistroCrearEmpleado(self,e):
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
                self.modelImagen.CrearImagenes(imagen)
            print("Todo conforme, se subio") #COLOCAR VENTANA EMERGENTE   
            self.limpiarCeldas()
            self.EntrenarSistema()
            self.imagenes=[]
            
        else:
            print("DNI IGUALES") #COLOCAR VENTANA EMERGENTE
        
    def limpiarCeldas (self):
        self.view.tfIdEmpleado.value=""
        self.view.tfApellidosEmpleado.value=""
        self.view.tfNombreEmpleado.value=""
        self.view.tfDniEmpleado.value=""
        self.view.tfTelefonoEmpleado.value=""
        self.view.cbTipoEmpleado.value=""
        self.view.cbPermisoDIngreso.value=""


    def EntrenarSistema(self):
        facesData,self.indicesReconocimiento,self.Diccionario=self.modelImagen.ObtenerContenidoImagenes_NombresEmpleado()
        self.etiqueta_sospechoso_mapping = {etiqueta: nombre for nombre, etiqueta in self.Diccionario.items()}
        print("Diccionario de entrenamiento:", self.etiqueta_sospechoso_mapping)

        model = cv2.face.LBPHFaceRecognizer_create()
        print("Entrenando...")
        model.train(facesData, np.array(self.indicesReconocimiento))

            # Guardar el modelo entrenado en un archivo XML
        model.write("ModeloFacesFrontalData2024.xml")
            
        print("Entrenamiento Completado", "El modelo ha sido entrenado y guardado.")
        return self.etiqueta_sospechoso_mapping
    
    #ADMINISTRADOR DE EMPLEADOS - CRUD
    def Click_ListarEmpleados(self): 
        self.view.tbRegistroEmpleados.rows=[]
        empleados= self.modelEmpleado.mostrarDatosEmpleado()
        for empleado in empleados:
            self.view.tbRegistroEmpleados.rows.append(
                ft.DataRow(
                    on_select_changed=self.SeleccionarCellTabla,
                    cells=[
                        ft.DataCell(ft.Text(str(empleado.getIdE()))),
                        ft.DataCell(ft.Text(empleado.getNombreE())),
                        ft.DataCell(ft.Text(empleado.getApellidoE())),
                        ft.DataCell(ft.Text(empleado.getDniE())),
                        ft.DataCell(ft.Text(empleado.getFechaRegistroE())),
                        ft.DataCell(ft.Text(empleado.getTelefonoE())),
                        ft.DataCell(ft.Text(empleado.getTipoE())),
                        ft.DataCell(ft.Text(empleado.getPermisoE())),
                    ]
                )
            )
        self.view.update()


    def SeleccionarCellTabla(self,e):
        if self.selected_row:
            self.selected_row.selected = False  # Deseleccionar la fila anteriormente seleccionada
        e.control.selected = True  # Seleccionar la nueva fila
        self.selected_row = e.control
        id=e.control.cells[0].content.value
        empleado=self.modelEmpleado.obtenerEmpleadoxID(id)
        if empleado != None:
            self.view.tfIdEmpleado.disabled=False
            self.view.tfIdEmpleado.value=empleado.getIdE()
            self.view.tfIdEmpleado.disabled=True
            self.view.tfNombreEmpleado.value=empleado.getNombreE()
            self.view.tfApellidosEmpleado.value=empleado.getApellidoE()
            self.view.tfDniEmpleado.value=empleado.getDniE()
            self.view.tfTelefonoEmpleado.value=empleado.getTelefonoE()
            self.view.cbTipoEmpleado.value=empleado.getTipoE()
            self.view.cbPermisoDIngreso.value=empleado.getPermisoE()
        self.view.update()
    
    def EliminarEmpleado(self,e):
        self.view.tfIdEmpleado.disabled=False
        id=self.view.tfIdEmpleado.value
        self.view.tfIdEmpleado.disabled=True
        if not self.modelEmpleado.eliminarDatosEmpleado(id):
            print("ELIMINADO CORRECTAMENTE")
            self.Click_ListarEmpleados()
            self.limpiarCeldas()
            self.EntrenarSistema() 

    def ActualizarEmpleado(self,e):
        self.view.tfIdEmpleado.disabled=False
        id=self.view.tfIdEmpleado.value
        self.view.tfIdEmpleado.disabled=True
        nombre=self.view.getNombreRegistro()
        apellido=self.view.getApellidoRegistro()
        dni=self.view.getDniRegistro()
        telefono=self.view.getTelefonoRegistro()
        permiso=self.view.getPermisoIngresoRegistro()
        tipoEmpleado=self.view.getTipoEmpleadoRegistro()
        empleado=EmpleadoDTO(id,nombre,apellido,dni,None,telefono,tipoEmpleado
                             ,permiso)
        self.modelEmpleado.actualizarDatosEmpleado(empleado)
        self.limpiarCeldas()
        self.Click_ListarEmpleados()
    ##YA SE IDENTIFICA, Y TODO, SOLO DEBO IMPLEMENTAR LAS VENTANAS DE ALERTA, LA SECCION DE HISTORIAL, ALERTAS Y NA MAS CREO##

   
    def run(self):
        self.view.page.update()
    
    def main(self,page: ft.Page):
        
        page.add(self.view)

