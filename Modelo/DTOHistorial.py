class HistorialDTO():
    def __init__(self,idH=None,idE=None,fechaH=None,horaH=None):
        self.idH=idH
        self.idE=idE
        self.fechaH=fechaH
        self.horaH=horaH
        

    def getIdH(self):
        return self.idH
    def setIdH(self,idH):
        self.idH=idH
    
    def getIdE(self):
        return self.idE
    def setIdE(self,idE):
        self.idE=idE

    def getFechaH(self):
        return self.fechaH
    def setFechaH(self,fechaH):
        self.fechaH=fechaH

    def getHoraH(self):
        return self.horaH
    def setHoraH(self,horaH):
        self.horaH=horaH
