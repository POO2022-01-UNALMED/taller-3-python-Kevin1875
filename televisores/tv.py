class TV:
    NumTV = 0
    def __init__(self, marca,estado):
      self.marca = marca
      self.canal = 1
      self.precio=500
      self._estado= estado
      self.volumen =1
      self.control= ""
      TV.NumTV +=1
      

    
    
    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca
      
    def setControl(self, control):
        self.control = control

    def getControl(self):
        return self.control
      
    def setPrecio(self, precio):
        self.precio = precio

    def getPrecio(self):
        return self.precio

    def setVolumen(self, volumen):
       self.volumen = volumen

    def getVolumen(self):
        return self.volumen

    def setCanal(self, canal):
      a=list(range(0,121))
      if canal in a and self._estado==True:
        self.canal = canal

    def getCanal(self):
        return self.canal

    def turnOff(self):
        self._estado = False
    
    def turnOn(self):
      self._estado = True
                 
      
    def getEstado(self):
        return self._estado

    def getCanal(self):
        return self.canal

    def canalUp(self):
      if (self.canal + 1)<122 and self._estado== True:
        self.canal +=1
      
    def canalDown(self):
      if (self.canal - 1)>0 and self._estado==True:
        self.canal -=1

    def volumenUp(self):
      
      if (self.volumen + 1)<8 and self._estado==True:  
        self.volumen +=1
      
    def volumenDown(self):
      if (self.volumen - 1)>0 and self._estado==True:
        self.volumen -=1

    
    @classmethod
    def getNumTV(cls):
        return cls.NumTV
      
    def setNumTV(num):
        TV.NumTV=num