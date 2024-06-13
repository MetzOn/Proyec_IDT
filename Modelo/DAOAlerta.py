from ConexionBD import Conexion
from DTOAlerta import AlertaDTO

class AlertaDAO:
    def __init__(self):
        self.conexion_manager=Conexion()

    def createAlerta(self,Alerta):
        resp = False
        con=None
        cursor=None
        if isinstance(Alerta, AlertaDTO):
            
            idH=Alerta.getIdH()
            captura=Alerta.getCapturaA()
            
            try:
                con=self.conexion_manager.conectar()
                con.autocommit=False
                cursor=con.cursor()
                sql='''INSERT INTO alerta (IdHistorial, Captura) VALUES('{}','{}')'''.format(idH,captura)
                resp=cursor.execute(sql)
                con.commit()
            except Exception as e:
                print(f'Error al agregar datos de Alerta: {e}')
            finally:
                self.conexion_manager.desconectar(con, cursor)
            return resp
    
    def mostrarDatosA(self):
        con=None
        cursor=None
        Alertas = []
        try:
            con=self.conexion_manager.conectar()
            con.autocommit=False
            cursor=con.cursor()
            sql="SELECT * FROM alerta"
            cursor.execute(sql)
            datos= cursor.fetchall()
            for tupla in datos:
                idA=tupla[0]
                idH=tupla[1]
                captura=tupla[2]
                
                alerta = AlertaDTO(idA,idH,captura)
                
                Alertas.append(alerta)
            con.commit()
        except Exception as e:
            print(f'Error al Obtener Alertas: {e}')
        finally:
            self.conexion_manager.desconectar(con, cursor)
        return Alertas