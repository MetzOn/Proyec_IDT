from .ConexionBD import Conexion
from .DTOEmpleado import EmpleadoDTO

class EmpleadoDAO():
    def __init__(self):
        self.conexion_manager=Conexion()
             
    def CreateEmpleado(self,empleado):
        resp = False
        con=None
        cursor=None
        if isinstance(empleado, EmpleadoDTO):
            nombreE=empleado.getNombreE()
            apellidoE=empleado.getApellidoE()
            dniE=empleado.getDniE()
            fechaRegistroE=empleado.getFechaRegistroE()
            telefonoE=empleado.getTelefonoE()
            tipoE=empleado.getTipoE()
            permisoE=empleado.getPermisoE()
            try:
                con=self.conexion_manager.conectar()
                con.autocommit=False
                cursor=con.cursor()
                sql='''INSERT INTO empleado (Nombre,Apellido,DNI,FechaRegistro,Telefono,Tipo,Permiso) VALUES('{}','{}','{}','{}','{}','{}','{}')'''.format(nombreE,apellidoE,dniE,fechaRegistroE,telefonoE,tipoE,permisoE)
                resp=cursor.execute(sql)
                con.commit()
            except Exception as e:
                print(f'Error al agregar datos de Empleado: {e}')
            finally:
                self.conexion_manager.desconectar(con, cursor)
            return resp
    
    def mostrarDatosMiemb(self):
        con=None
        cursor=None
        empleados = []
        try:
            con=self.conexion_manager.conectar()
            con.autocommit=False
            cursor=con.cursor()
            sql="SELECT * FROM miembro"
            cursor.execute(sql)
            datos= cursor.fetchall()
            for tupla in datos:
                idE=tupla[0]
                nombreE=tupla[1]
                apellidoE=tupla[2]
                dniE=tupla[3]
                fechaRegistroE=tupla[4]
                telefonoE=tupla[5]
                tipoE=tupla[6]
                permisoE=tupla[7]
                empleado = EmpleadoDTO()
                empleado.setIdE()
                empleado.setNombreE(nombreE)
                empleado.setApellidoE(apellidoE)
                empleado.setDniE(dniE)
                empleado.setFechaRegistroE(fechaRegistroE)
                empleado.setTelefonoE(telefonoE)
                empleado.setTipoE(tipoE)
                empleado.setPermisoE(permisoE)
                empleados.append(empleado)
            con.commit()
        except Exception as e:
            print(f'Error al Obtener datos: {e}')
        finally:
            self.conexion_manager.desconectar(con, cursor)
        return empleados
        
    def eliminarDatosMiemb(self,id):
        resp = None
        con=None
        cursor=None
        try:
            con=self.conexion_manager.conectar()
            con.autocommit=False
            cursor=con.cursor()
            sql='''DELETE FROM empleado WHERE IdEmpleado='{}' '''.format(int(id))
            resp=cursor.execute(sql)
            con.commit()
        except Exception as e:
            print(f'Error al Obtener datos: {e}')
            resp =False
        finally:
            self.conexion_manager.desconectar(con, cursor)
        return resp
            
    def actualizarDatosMiemb(self,empleado):
        resp =None
        con=None
        cursor=None
        if isinstance(empleado, EmpleadoDTO):
            idE=empleado.getIdE()
            nombreE=empleado.getNombreE()
            apellidoE=empleado.getApellidoE()
            dniE=empleado.getDniE()
            fechaRegistroE=empleado.getFechaRegistroE()
            telefonoE=empleado.getTelefonoE()
            tipoE=empleado.getTipoE()
            permisoE=empleado.getPermisoE()
            
        try:
            con=self.conexion_manager.conectar()
            con.autocommit=False
            cursor=con.cursor()
            sql='''UPDATE miembro SET Nombre ='{}',Apellido = '{}',DNI = '{}',FechaRegistro = '{}',Telefono = '{}',Tipo = '{}',Permiso = '{}' WHERE id_m= '{}' '''.format(nombreE,apellidoE,dniE,fechaRegistroE,telefonoE,tipoE,permisoE,idE)
            resp=cursor.execute(sql)
            dato=cursor.rowcount
            con.commit()
            return dato
        except Exception as e:
            print(f'Error al Obtener datos: {e}')
            resp =False
        finally:
            self.conexion_manager.desconectar(con, cursor)
        return resp