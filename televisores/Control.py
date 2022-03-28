from televisores.TV import TV

class Control:
    
    def __init__(self):
        self._tv = ""
      
    def turnOn(self):
      TV.setEstado(self, "turnOn")
      

    def turnOff(self):
      TV.setEstado(self, "turnOff")
      
      
    def canalUp(self):
      TV.canalUp(self)
    
    def canalDown(self):
      TV.canalDown(self)

    def volumenUp(self):
      TV.volumenUp(self)

    def volumenDown(self):
      TV.volumenDown(self)

    def setCanal(self, canal):
      TV.setCanal(self, canal)
      

    def enlazar(self, tv):
      self._tv = tv
      TV.setControl(self, Control)
      

    def setTv(self, tv):
      self._tv= tv
    
    def getTv(self, tv):
      return self._tv
      
    
  
    