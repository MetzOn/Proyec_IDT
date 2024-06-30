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
                # Verificar si el DNI ya existe
                con=self.conexion_manager.conectar()
                con.autocommit=False
                cursor=con.cursor()
                query = '''SELECT COUNT(*) FROM empleado WHERE DNI = '{}' '''.format(dniE)
                cursor.execute(query)
                result = cursor.fetchone()
                if result[0] > 0:
                    return False
            except Exception as e: 
                print(f'Error al agregar consultar dni: {e}')
            
            else:
                try:
                    con=self.conexion_manager.conectar()
                    con.autocommit=False
                    cursor=con.cursor()
                    sql='''INSERT INTO empleado (Nombre,Apellido,DNI,FechaRegistro,Telefono,Tipo,Permiso) VALUES('{}','{}','{}','{}','{}','{}','{}')'''.format(nombreE,apellidoE,dniE,fechaRegistroE,telefonoE,tipoE,permisoE)
                    cursor.execute(sql)
                    con.commit()
                    resp = cursor.rowcount > 0
                    return resp
                except Exception as e:
                    print(f'Error al agregar datos de Empleado: {e}')
                finally:
                    self.conexion_manager.desconectar(con, cursor)
            
    
    def mostrarDatosEmpleado(self):
        con=None
        cursor=None
        empleados = []
        try:
            con=self.conexion_manager.conectar()
            con.autocommit=False
            cursor=con.cursor()
            sql="SELECT * FROM empleado"
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
                empleado.setIdE(idE)
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
        
    def eliminarDatosEmpleado(self,id):
        resp = None
        con=None
        cursor=None
        try:
            con=self.conexion_manager.conectar()
            con.autocommit=False
            cursor=con.cursor()
            sql='''DELETE FROM empleado WHERE IdEmpleado='{}' '''.format(id)
            resp=cursor.execute(sql)
            con.commit()
        except Exception as e:
            print(f'Error al Obtener datos: {e}')
            resp =False
        finally:
            self.conexion_manager.desconectar(con, cursor)
        return resp
            
    def actualizarDatosEmpleado(self,empleado):
        resp =None
        con=None
        cursor=None
        if isinstance(empleado, EmpleadoDTO):
            idE=empleado.getIdE()
            nombreE=empleado.getNombreE()
            apellidoE=empleado.getApellidoE()
            dniE=empleado.getDniE()
            telefonoE=empleado.getTelefonoE()
            tipoE=empleado.getTipoE()
            permisoE=empleado.getPermisoE()
            
        try:
            con=self.conexion_manager.conectar()
            con.autocommit=False
            cursor=con.cursor()
            sql='''UPDATE empleado SET Nombre ='{}',Apellido = '{}',DNI = '{}',Telefono = '{}',Tipo = '{}',Permiso = '{}' WHERE id_m= '{}' '''.format(nombreE,apellidoE,dniE,telefonoE,tipoE,permisoE,idE)
            resp=cursor.execute(sql)
            dato=cursor.rowcount
            con.commit()
            return dato
        except Exception as e:
            print(f'Error al actualizar datos: {e}')
            resp =False
        finally:
            self.conexion_manager.desconectar(con, cursor)
        return resp
    
    def obtenerIDEmpleado(self,dni):
        resp =None
        con=None
        cursor=None
        try:
            con=self.conexion_manager.conectar()
            con.autocommit=False
            cursor=con.cursor()
            sql = '''SELECT IdEmpleado FROM empleado WHERE DNI ='{}' '''.format(dni)
            cursor.execute(sql)
            resultado = cursor.fetchone()
            con.commit()
            if resultado:
                id_obtenido = resultado[0]
                return id_obtenido
            else:
                return None
        except Exception as e:
            print("Error al obtener el ID del empleado:", e)
            return None
        finally:
            self.conexion_manager.desconectar(con, cursor)
    
    def obtenerEmpleadoxID(self,id):
        con=None
        cursor=None
        try:
            con=self.conexion_manager.conectar()
            con.autocommit=False
            cursor=con.cursor()
            sql = '''SELECT * FROM empleado WHERE IdEmpleado ='{}' '''.format(id)
            cursor.execute(sql)
            resultado = cursor.fetchone()
            con.commit()
            if resultado:
                idE=resultado[0]
                nombreE=resultado[1]
                apellidoE=resultado[2]
                dniE=resultado[3]
                fechaRegistroE=resultado[4]
                telefonoE=resultado[5]
                tipoE=resultado[6]
                permisoE=resultado[7]
                empleado = EmpleadoDTO()
                empleado.setIdE(idE)
                empleado.setNombreE(nombreE)
                empleado.setApellidoE(apellidoE)
                empleado.setDniE(dniE)
                empleado.setFechaRegistroE(fechaRegistroE)
                empleado.setTelefonoE(telefonoE)
                empleado.setTipoE(tipoE)
                empleado.setPermisoE(permisoE)
                return empleado
            else:
                return None
        except Exception as e:
            print("Error al obtener el empleado por ID:", e)
            return None
        finally:
            self.conexion_manager.desconectar(con, cursor)
    
