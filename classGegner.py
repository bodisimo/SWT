import pygame
import random

class gegner:
    posX = 0
    posY = 0
    size = 0
    live = 0
    speed = 0
    gegnerNr = 0
    schaden = 0
    gegner0Size = 30
    gegner1Size = 50
    gegner2Size = 80
    gegnerBild = 0
    waffenBild = 0
    moveDownSpeed = 100
    startLive = 0
    waffeX = 0
    waffeY = 0
    schaden = 0
    plannedSchaden = 0
    schussProTausend = 10


    def __init__(self, posX=0, posY=0, gegnerNr=0, gegnerBild = 0, waffenBild = 0, leben = 1,schaden = 1, size = 1, speed = 4, moveDownSpeed = 50, schussProTausend = 10, name = "Boss"):


        #klasee 0 groß und langsam
        if gegnerNr == 0:
            self.posX = posX
            self.posY = posY
            self.size = size
            self.live = leben
            self.speed = speed
            self.gegnerNr = 0
            self.plannedSchaden = schaden
            self.gegnerBild = gegnerBild
            self.waffenBild = waffenBild
            self.moveDownSpeed = moveDownSpeed
            self.startLive = leben
            self.schussProTausend = schussProTausend

        #klasse 1 klein und langsam
        elif gegnerNr == 1:
            self.posX = posX
            self.posY = posY
            self.size = size
            self.live = leben
            self.speed = speed
            self.gegnerNr = 1
            self.plannedSchaden = schaden
            self.gegnerBild = gegnerBild
            self.waffenBild = waffenBild
            self.moveDownSpeed = moveDownSpeed
            self.startLive = leben
            self.schussProTausend = schussProTausend

        #klasse 3 klein und schnell
        elif gegnerNr == 2:
            self.posX = posX
            self.posY = posY
            self.size = size
            self.live = leben
            self.speed = speed
            self.gegnerNr = 2
            self.plannedSchaden = schaden
            self.gegnerBild = gegnerBild
            self.waffenBild = waffenBild
            self.moveDownSpeed = moveDownSpeed
            self.startLive = leben
            self.schussProTausend = schussProTausend

        #custom
        elif gegnerNr == 4:
            self.posX = posX
            self.posY = posY
            self.size = size
            self.live = leben
            self.speed = speed
            self.gegnerNr = 4
            self.plannedSchaden = schaden
            self.gegnerBild = gegnerBild
            self.waffenBild = waffenBild
            self.moveDownSpeed = moveDownSpeed
            self.startLive = leben
            self.name = name
            self.schussProTausend = schussProTausend
            # custom
        elif gegnerNr == 5:
            self.posX = posX
            self.posY = posY
            self.size = size
            self.live = leben
            self.speed = speed
            self.gegnerNr = 5
            self.plannedSchaden = schaden
            self.gegnerBild = gegnerBild
            self.waffenBild = waffenBild
            self.moveDownSpeed = moveDownSpeed
            self.startLive = leben
            self.name = name
            self.schussProTausend = schussProTausend
        elif gegnerNr == 6: # mithut montag
            self.posX = posX
            self.posY = posY
            self.size = size
            self.live = leben
            self.speed = speed
            self.gegnerNr = 5
            self.plannedSchaden = schaden
            self.gegnerBild = gegnerBild
            self.waffenBild = waffenBild
            self.moveDownSpeed = moveDownSpeed
            self.startLive = leben
            self.name = name
            self.schussProTausend = schussProTausend




    def zeichneGegner(self, screen):
        screen.blit(self.gegnerBild, (self.posX, self.posY))
        #zeichnet nur wen nicht tod
        self.shoot(screen)


    def checkTod(self, waffenBox):
        gegnerBox = pygame.Rect(self.posX, self.posY, self.size, self.size)

        if waffenBox.colliderect(pygame.Rect(self.waffeX, self.waffeY, 30,30)):
            self.schaden = 0
        if waffenBox.colliderect(gegnerBox):
            return True
        else:
            return False

    def moveDown(self, ):
        self.posY += self.moveDownSpeed

    def moveLeft(self):
        self.posX -= self.speed

    def moveRight(self):
        self.posX += self.speed
    def printLive(self,screen):
        pygame.draw.rect(screen,(255,0,0),(self.posX, self.posY-3, int((self.live/self.startLive)*self.size), 3), 0)

    def printName(self,screen):
        name = self.renderText(self.name, 44)
        screen.blit(name, (self.posX, self.posY - 30))


    def renderText(self,text, size, rot=255, grün=255, blau=255):
        sys_font = pygame.font.SysFont("none", size)
        rendered = sys_font.render(text, 0, (rot, grün, blau))
        return rendered

    def shoot(self,screen):
        if self.schaden == 0:
            if random.random() * 1000 > 1000-self.schussProTausend:
                self.schaden = self.plannedSchaden
                self.waffeX = self.posX
                self.waffeY = self.posY
                screen.blit(self.waffenBild,(self.waffeX-int(self.size/2), self.waffeY+self.size))



    def moveShoot(self,screen):
        self.waffeY += 4
        screen.blit(self.waffenBild, (self.waffeX, self.waffeY))
        if self.waffeY > 1200:
            self.schaden = 0



    def checkPlayerGetroffen(self,player, hit):
        waffenBox = pygame.Rect(self.waffeX, self.waffeY, 10,10)
        playerBox = pygame.Rect(player.playerX, player.playerY, player.playerSize, player.playerSize)
        if playerBox.colliderect(waffenBox):
            pygame.mixer.Sound.play(hit)
            player.live -= self.schaden
            self.schaden = 0
