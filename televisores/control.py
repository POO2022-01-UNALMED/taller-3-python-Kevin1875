from televisores.tv import TV

class Control:
    
    def __init__(self):
        self.tv = ""
      
    def turnOn(self):
      self.tv.turnOn()
      

    def turnOff(self):
      self.tv.turnOff()
      
      
    def canalUp(self):
      if self.tv._estado==True:
        self.tv.canalUp()
      
    
    def canalDown(self):
      if self.tv._estado==True:
        self.tv.canalDown()

    def volumenUp(self):
      if self.tv._estado==True:
        self.tv.volumenUp()

    def volumenDown(self):
      if self.tv._estado==True:
        self.tv.volumenDown()

    def setCanal(self, canal):
      if self.tv._estado==True:
        self.tv.setCanal(canal)
      

    def enlazar(self, tv):
      self.tv = tv
      self.tv.setControl(Control)
      

    def setTv(self, tv):
      self.tv= tv
    
    def getTv(self):
      return self.tv
      
    
  
    