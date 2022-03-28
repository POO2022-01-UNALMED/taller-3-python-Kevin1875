from televisores.marca import Marca
from televisores.control import Control

class TV:
    _numTV = 0
    def __init__(self, marca,estado):
      self.marca = marca
      self.canal = 1
      self.precio=500
      self._estado= estado
      self.volumen =1
      self.control= ""
      TV._numTV+=1

    def setTipoModulo(self, marca,estado):
        if estado == "turnOn":
          return (self.marca + "Esta encendido")
        else:
           return (self.marca + "No esta encendido")
    
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
        self.canal = canal

    def getCanal(self):
        return self.canal

    def setEstado(self, estado):
        if estado =="turnOn" or "turnOff":
          self._estado = estado
                 
      
    def getEstado(self):
        return self._estado

    def getCanal(self):
        return self.canal

    def canalUp(self):
      a=self.canal =+1
      if a >120 and self._estado=="turnOn":
        self.canal +=1
      
    def canalDown(self):
      a=self.canal =-1
      if a<0 and self._estado=="turnOn":
        self.canal -=1

    def volumenUp(self):
      a=self.volumen =+1
      if a > 7 and self._estado=="turnOn":  
        self.volumen +=1
      
    def volumenDown(self):
      a=self.volumen =-1
      if a<0 and self._estado=="turnOn":
        self.volumen -=1

    
    @staticmethod 
    def getCantidad():
        return TV._numTV