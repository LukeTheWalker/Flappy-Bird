class Bird:
    def __init__(self, x, y, advance, accel):
        self.x = x
        self.y = y
        self.accel = accel
        self.sizex = 68
        self.sizey = 48
        self.speedy = 0
        self.speedx = 0
        self.baseJ = 0
        self.maxJ = 80
        self.img = loadImage("bird.png")
        self.img.resize(self.sizex, 0)
  
    def printShape (self):
        #fill(255,0,0)
        #ellipse(self.x, self.y, 10,10) 
        #ellipse(self.x+self.sizex-10, self.y+self.sizex-10, 10,10) 
        image(self.img, self.x, self.y)
        
  
    def fall(self):
        self.speedy+=self.accel
        #if (self.y < self.baseJ - self.maxJ):
            #self.speedy = abs(self.speedy)
            #self.accel = abs(self.accel)
        self.y += self.speedy
        self.x += self.speedx
        
  
    def jump (self): 
        #self.speedy = abs(self.speedy) * -1;
        #self.accel = abs(self.accel) * -1;
        self.speedy = -8
        #self.baseJ=self.y;
    
    def run (self):
        self.printShape()
        self.fall()
