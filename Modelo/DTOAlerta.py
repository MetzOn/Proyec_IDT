class AlertaDTO():
    def __init__(self,idA=None,idH=None,capturaA=None):
        self.idA=idA
        self.idH=idH
        self.capturaA=capturaA

    def getIdA(self):
        return self.idA
    def setIdA(self,idA):
        self.idA=idA
      
    def getIdH(self):
        return self.idH
    def setIdH(self,idH):
        self.idH=idH

    def getCapturaA(self):
        return self.capturaA
    def setCapturaA(self,capturaA):
        self.capturaA=capturaA

  
