class EmpleadoDTO():
    def __init__(self,idE=None,nombreE=None,apellidoE=None,dniE=None,fechaRegistroE=None,telefonoE=None,tipoE=None,permisoE=None):
        self.idE=idE
        self.nombreE=nombreE
        self.apellidoE=apellidoE
        self.dniE=dniE
        self.fechaRegistroE=fechaRegistroE
        self.telefonoE=telefonoE
        self.tipoE=tipoE
        self.permisoE=permisoE


    def getIdE(self):
        return self.idE
    def setIdE(self,idE):
        self.idE=idE

    def getNombreE(self):
        return self.nombreE
    def setNombreE(self,nombreE):
        self.nombreE=nombreE

    def getApellidoE(self):
        return self.apellidoE
    def setApellidoE(self,apellidoE):
        self.apellidoE=apellidoE

    def getDniE(self):
        return self.dniE
    def setDniE(self,dniE):
        self.dniE=dniE

    def getFechaRegistroE(self):
        return self.fechaRegistroE
    def setFechaRegistroE(self,fechaRegistroE):
        self.fechaRegistroE=fechaRegistroE
    
    def getTelefonoE(self):
        return self.telefonoE
    def setTelefonoE(self,telefonoE):
        self.telefonoE=telefonoE

    def getTipoE(self):
        return self.tipoE
    def setTipoE(self,tipoE):
        self.tipoE=tipoE

    def getPermisoE(self):
        return self.permisoE
    def setPermisoE(self,permisoE):
        self.permisoE=permisoE
