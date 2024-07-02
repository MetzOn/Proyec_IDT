from .ConexionBD import Conexion
from .DTOHistorial import HistorialDTO
class HistorialDAO:
    def __init__(self):
        self.conexion_manager=Conexion()
   
    
    def createHistorial(self,historial):
        resp = False
        con=None
        cursor=None
        if isinstance(historial, HistorialDTO):
            idE=historial.getIdE()
            
            
            try:
                con=self.conexion_manager.conectar()
                con.autocommit=False
                cursor=con.cursor()
                sql='''INSERT INTO historial (IdEmpleado) VALUES('{}')'''.format(idE)
                cursor.execute(sql)
                con.commit()
                resp = cursor.rowcount > 0
            except Exception as e:
                print(f'Error al agregar datos de historial: {e}')
                return False
            finally:
                self.conexion_manager.desconectar(con, cursor)
            return resp
    
    def mostrarDatosH(self):
        con = None
        cursor = None
        Historiales = []
        try:
            con = self.conexion_manager.conectar()
            con.autocommit = False
            cursor = con.cursor()
            sql = """
                SELECT h.IdHistorial, h.IdEmpleado, h.Fecha, h.Hora, e.Nombre, e.DNI
                FROM historial h
                INNER JOIN empleado e ON h.IdEmpleado = e.IdEmpleado
                """
            cursor.execute(sql)
            datos = cursor.fetchall()
            for tupla in datos:
                idH = tupla[0]
                idE = tupla[1]
                fecha = tupla[2]
                hora = tupla[3]
                nombre = tupla[4]
                dni = tupla[5]
                historial = HistorialDTO(idH, idE, fecha, hora, nombre, dni)
                Historiales.append(historial)
            con.commit()
        except Exception as e:
            print(f'Error al obtener datos: {e}')
        finally:
            self.conexion_manager.desconectar(con, cursor)
        return Historiales