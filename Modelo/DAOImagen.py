
from .ConexionBD import Conexion
from .DTOImagen import ImagenDTO
from .DTOEmpleado import EmpleadoDTO
import cv2
import numpy as np

class ImagenDAO:
    def __init__(self):
        self.conexion_manager=Conexion()
        
    def CrearImagenes(self,imag):
        con=None
        cursor=None
        if isinstance(imag, ImagenDTO):
            
            nombre=imag.getNombreI()
            contenido=imag.getContenidoI()
            id_empleado= imag.getIdE()

        try:
            con=self.conexion_manager.conectar()
            con.autocommit=False
            cursor=con.cursor()
            sql="INSERT INTO imagenes (IdEmpleado,nombreI,Imagen) VALUES (%s, %s, %s)"
            cursor.execute(sql, (id_empleado,nombre, contenido))
            con.commit()
        except Exception as e:
            print(f'Error al agregar Imagen: {e}')
        finally:
            self.conexion_manager.desconectar(con, cursor)


    def eliminarImagenesID(self,id):
        con=None
        cursor=None
        resp=None
        try:
            con=self.conexion_manager.conectar()
            con.autocommit=False
            cursor=con.cursor()
            sql='''DELETE FROM imagenes WHERE IdImagen='{}' '''.format(id)
            resp=cursor.execute(sql)
            con.commit()
            return resp
        except Exception as e:
            print(f'Error al Eliminar Imagen: {e}')
            return resp
        finally:
            self.conexion_manager.desconectar(con, cursor)
            
    def eliminarImagenesIDEmpleado(self,Empleado):
        con=None
        cursor=None
        if isinstance(Empleado, EmpleadoDTO):
            idEmpl=Empleado.getIdE()
 
        try:
            con=self.conexion_manager.conectar()
            con.autocommit=False
            cursor=con.cursor()
            sql='''DELETE FROM imagenes WHERE IdEmpleado='{}' '''.format(idEmpl)
            cursor.execute(sql)
            con.commit()
        except Exception as e:
            print(f'Error al Eliminar Imagenes: {e}')
        finally:
            self.conexion_manager.desconectar(con, cursor)

    def mostrarImagenesPorIDEmpl(self,idEmpl):
        con=None
        cursor=None
        ImagenesxID = []
        try:
            con=self.conexion_manager.conectar()
            cursor=con.cursor()
            sql='''SELECT * FROM imagenes WHERE IdEmpleado='{}' '''.format(idEmpl)
            cursor.execute(sql)
            datos= cursor.fetchall()
            for tupla in datos:
                id=tupla[0]
                idE=tupla[1]
                nombre = tupla[2]
                contenido=tupla[3]
                ImagenM = ImagenDTO(id,idE,nombre,contenido)
                ImagenesxID.append(ImagenM)
            return ImagenesxID
        except Exception as e:
            print(f'Error al Obtener Imagenes por ID: {e}')
        finally:
            self.conexion_manager.desconectar(con, cursor)
    
    def VisualizarImagenPorID(self,idImagen):
        con=None
        cursor=None
        
        try:
            con=self.conexion_manager.conectar()
            cursor=con.cursor()
            sql='''SELECT Imagen FROM imagenes WHERE IdImagen='{}' '''.format(idImagen)
            cursor.execute(sql)
            contenido_i =cursor.fetchone()
            if contenido_i:
                # Procesar la imagen desde el contenido binario
                image_array = np.frombuffer(contenido_i[0], np.uint8)
                image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)
            return image
    
        except Exception as e:
            print(f'Error al visualizar Imagen: {e}')
            return None
        finally:
            self.conexion_manager.desconectar(con, cursor)

    def ObtenerContenidoImagenes_NombresEmpleado(self):
        con=None
        cursor=None
        facesData = []
        labels = []
        Empleado_name_mapping = {}  # Un diccionario para hacer un seguimiento de los nombres de los Empleados
        Empleado_dni_mapping = {} 
        current_label = 0
        try:
            con = self.conexion_manager.conectar()
            cursor = con.cursor()
            sql = ''' SELECT imagenes.Imagen, empleado.Nombre,empleado.DNI
                      FROM imagenes
                      INNER JOIN empleado ON imagenes.IdEmpleado = empleado.IdEmpleado'''
            cursor.execute(sql)
            for contenido_i, nombre_s,dni in cursor:
                # Procesar la imagen desde el contenido binario
                image_array = np.frombuffer(contenido_i, np.uint8)
                image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)  # Leer en escala de grises
                # Agregar la imagen
                facesData.append(image)
                # Asociar una etiqueta única al nombre del sospechoso
                if nombre_s not in Empleado_name_mapping:
                    Empleado_name_mapping[nombre_s] = current_label
                    Empleado_dni_mapping[dni]=current_label
                    current_label += 1
                labels.append(Empleado_name_mapping[nombre_s])
                
                print(nombre_s)
            
            return facesData, labels, Empleado_name_mapping,Empleado_dni_mapping
        
        except Exception as e:
            print(f'Error al obtener Imagenes: {e}')
            return None
        finally:
            self.conexion_manager.desconectar(con, cursor)