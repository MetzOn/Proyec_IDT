
class AutenticacionDTO: 
    def __init__(self,idAut=None,idE=None,usuario=None,contra=None):
        self.idAut=idAut
        self.idE=idE
        self.usuario=usuario
        self.contra=contra

    def getIdAut(self):
        return self.idAut

    def getIdE(self):
        return self.idE
    
    def getUsuario(self):
        return self.usuario
    
    def getContra(self):
        return self.contra


  

        