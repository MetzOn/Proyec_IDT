class ImagenDTO():
    def __init__(self,idI=None,idE=None,nombreI=None,contenidoI=None):
        self.idI=idI
        self.idE=idE
        self.nombreI=nombreI
        self.contenidoI=contenidoI
        

    def getIdI(self):
        return self.idI
    def setIdI(self,idI):
        self.idI=idI
    
    def getIdE(self):
        return self.idE
    def setIdE(self,idE):
        self.idE=idE

    def getNombreI(self):
        return self.nombreI
    def setNombreE(self,nombreI):
        self.nombreI=nombreI

    def getContenidoI(self):
        return self.contenidoI
    def setContenidoI(self,contenidoI):
        self.contenidoI=contenidoI
