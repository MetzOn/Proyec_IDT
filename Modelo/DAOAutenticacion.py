from .ConexionBD import Conexion
from .DTOAutenticacion import AutenticacionDTO

class AutenticacionDAO:
    def __init__(self) :
        self.conexion_manager=Conexion()

    def AutenticarUsuario(self, Usuario):
        
        con=None
        cursor=None
        if isinstance(Usuario, AutenticacionDTO): 
            usu=Usuario.getUsuario()
            contraseña=Usuario.getContra()
            try:
                con=self.conexion_manager.conectar()
                con.autocommit=False
                cursor=con.cursor()
                sql="SELECT Usuario, Contraseña FROM autenticacion"
                cursor.execute(sql)
                datos= cursor.fetchall()
                for tupla in datos:
                    if tupla[0]==usu and tupla[1]==contraseña:
                        return True
                con.commit()
            except Exception as e:
                print(f'Error al Obtener Usuarios: {e}')
            finally:
                self.conexion_manager.desconectar(con, cursor)
            return False