from ConexionBD import Conexion
from DTOHistorial import HistorialDTO
class HistorialDao:
    def __init__(self):
        self.conexion_manager=Conexion()
   
    
    def createHistoria(self,historial):
        resp = False
        con=None
        cursor=None
        if isinstance(historial, HistorialDTO):
            idE=historial.getIdE
            fechaH=historial.getFechaH
            hora=historial.getHoraH
            
            try:
                con=self.conexion_manager.conectar()
                con.autocommit=False
                cursor=con.cursor()
                sql='''INSERT INTO historial (IdEmpleado,Fecha,Hora) VALUES('{}','{}','{}')'''.format(idE,fechaH,hora)
                resp=cursor.execute(sql)
                con.commit()
            except Exception as e:
                print(f'Error al agregar datos de historial: {e}')
            finally:
                self.conexion_manager.desconectar(con, cursor)
            return resp
    
    def mostrarDatosH(self):
        con=None
        cursor=None
        Historiales = []
        try:
            con=self.conexion_manager.conectar()
            con.autocommit=False
            cursor=con.cursor()
            sql="SELECT * FROM historial"
            cursor.execute(sql)
            datos= cursor.fetchall()
            for tupla in datos:
                idH=tupla[0]
                idE=tupla[1]
                fecha=tupla[2]
                hora=tupla[3]
                historial = HistorialDTO(idH,idE,fecha,hora)
                
                Historiales.append(historial)
            con.commit()
        except Exception as e:
            print(f'Error al Obtener datos: {e}')
        finally:
            self.conexion_manager.desconectar(con, cursor)
        return Historiales