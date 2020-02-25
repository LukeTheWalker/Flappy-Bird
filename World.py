class World:

    def __init__(self, advance, mimmo):
        self.speed = advance
        self.img = [loadImage("tubeUp.png"), loadImage("tubeDown.png")]
        self.lineBg = loadImage("line.png")
        self.lineBg.resize(0, height) 
        self.tubes = []
        self.tubes.append(height / 2)
        self.offset = 1000
        self.cnt = 0
        self.mimmo = mimmo
        self.dist = 300
        self.sizeTubex = 117
        self.sizeTubey = 720
        self.window = 200
        self.font = createFont("flappyFont.ttf", 100)
        textFont(self.font)
        
        for img in self.img:
            img.resize(117, 0) #117 x 720
        for i in range(0, 12):
            self.createTube()

    def createTube(self):
        self.tubes.append(random(self.tubes[-1] - 150, self.tubes[-1] + 150))
        if self.tubes[-1] > height-100:
            self.tubes[-1] = height-100
        if self.tubes[-1]-self.window < 100:
           self.tubes[-1] = 100 + self.window

    def printWorld(self):
        #fill(255,0,0)
        #ellipse(self.cnt * self.dist + self.offset,                 self.tubes[self.cnt],10,10)
        #ellipse(self.cnt * self.dist + self.offset +self.sizeTubex, self.tubes[self.cnt],10,10)
        #ellipse(self.cnt * self.dist + self.offset,                 self.tubes[self.cnt]-self.window,10,10)
        #ellipse(self.cnt * self.dist + self.offset +self.sizeTubex, self.tubes[self.cnt]-self.window,10,10)
        for i in range(self.cnt, self.cnt+6):
            #pushMatrix();
            #translate(5.0-self.cnt, 0);
            image(self.img[0], i * self.dist + self.offset, self.tubes[i])
            image(self.img[1], i * self.dist + self.offset, self.tubes[i] - self.window - self.sizeTubey)
            #popMatrix();
        for i in range (self.cnt/4-1, self.cnt/4+2):
            image(self.lineBg, self.offset+width*i,0)
        fill(0,0,0)
        text(self.cnt, width-200, 200)
    
    def advance(self):
        self.offset -= self.speed
        if self.cnt * self.dist + self.offset + self.sizeTubex < 0:
            self.cnt+=1
            self.createTube()
        
    def isAlligned (self):
        return (self.mimmo.x+self.mimmo.sizex-10 >= (self.cnt*self.dist+self.offset)) and ((self.cnt*self.dist+self.offset)+self.sizeTubex >= self.mimmo.x-10)
    
    def isInter(self):
        return self.mimmo.y+10 < self.tubes[self.cnt]-self.window or self.mimmo.y + self.mimmo.sizey -10  > self.tubes[self.cnt]
    
    def checkCollision(self):
        #print (str(-(self.cnt*self.dist+self.offset)) + " vs " + str(self.mimmo.x))
        if self.isAlligned() and self.isInter():
            background(0)
            fill(255,255,255)
            textAlign(CENTER, CENTER)
            text("GAME OVER",width/2,height/2)
            fill(255,0,0)
            #ellipse(width/2,height/2, 10,10)
            delay(1000)
    
    def run(self):
        self.advance()
        self.printWorld()
        self.checkCollision()
