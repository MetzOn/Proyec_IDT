import flet as ft
from PIL import Image
import cv2
import numpy as np
from io import BytesIO
import threading

class CameraHandler:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame = None
        self.lock = threading.Lock()
        self.running = True

    def start_capture(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                with self.lock:
                    self.frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    def stop_capture(self):
        self.running = False
        self.cap.release()

    def get_frame(self):
        with self.lock:
            return self.frame.copy() if self.frame is not None else None

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.camera = CameraHandler()

        # Crear un contenedor principal
        self.container = ft.Container(
            expand=True,
            bgcolor=ft.colors.WHITE,
        )

        # Widget de imagen para mostrar la transmisión en vivo
        self.image_widget = ft.Image(value=None, width="100%", height="100%")
        self.container.content = [self.image_widget]

        # Iniciar la captura de la cámara en un hilo separado
        self.capture_thread = threading.Thread(target=self.camera.start_capture)
        self.capture_thread.start()

        # Función para actualizar la imagen en vivo desde la cámara
        def update_live_image():
            frame = self.camera.get_frame()
            if frame is not None:
                image = Image.fromarray(frame)
                with BytesIO() as output:
                    image.save(output, format="PNG")
                    image_data = output.getvalue()
                self.image_widget.value = image_data

                # Programar la siguiente actualización
                self.page.after(100, update_live_image)

        # Programar la primera actualización
        self.page.after(100, update_live_image)

        # Agregar el contenedor a la página
        self.page.add(self.container)

        # Función para detener la captura al cerrar la aplicación
        def on_close():
            self.camera.stop_capture()
            self.capture_thread.join()

        # Asignar función de cierre al evento de la aplicación
        self.page.on_app_close(on_close)

# Iniciar la aplicación Flet
if __name__ == "__main__":
    ft.app(target=App)