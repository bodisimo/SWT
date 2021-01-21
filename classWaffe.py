import pygame
import math
import classPlayerStat


class waffe:
    # waffenliste
    # 0 ist laser
    # 1 ist kanone

    posX = 0
    posY = 0
    speed = 0
    waffenNr = 0
    size = 0
    schaden = 0
    waffenBild = 0

    laserReloadSpeedLevel = [0,60,55,50,45,40,35,30,25,20,15,10,9,8,7,6,5, "max"]
    laserSchadenLevel = [0,1,2,3,4,5,6,7,8,9,10, "max"]
    laserSpeedLevel = [0,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32, "max"]

    bombSchadenLevel = [0,10,25,40,60,100,200,400,600,1000,2000,5000,10000, "max"]
    bombSizeLevel = [0,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220, "max"]
    bombReloadSpeedLevel = [0,360,330,300,270,240,210,180,160,140, 120, 110, 101, "max"]

    shotgunSchadenLevel = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,9,10, "max"]
    shotgunShrotLevel = [0,2,5,9,14,21,30,41,52,63,74,85,100,120,150,200,250,300, "max"]
    shotgunReloadTimeLevel = [0,600,560,520,480,440,400,360,320,280,240,220,200,180,160,140,120,100,80,70,60, "max"]




    def __init__(self,waffenBilder ,waffenNr, currentPlayer):
        # laser
        if waffenNr == 0:
            self.posX = 0
            self.posY = 0
            self.speed = self.laserSpeedLevel[currentPlayer.laserSpeedLevel]
            self.waffenNr = waffenNr
            self.size = 10
            self.schaden = 0
            self.waffenBild = waffenBilder[waffenNr]
        # kanone
        elif waffenNr == 1:
            self.posX = 0
            self.posY = 0
            self.speed = 5
            self.waffenNr = waffenNr
            self.size = self.bombSizeLevel[currentPlayer.bombSizeLevel]
            self.schaden = 0
            self.waffenBild = pygame.transform.scale(waffenBilder[waffenNr],(self.bombSizeLevel[currentPlayer.bombSizeLevel],self.bombSizeLevel[currentPlayer.bombSizeLevel]))
        elif waffenNr == 2:
            self.posX = 0
            self.posY = 0
            self.speed = 3
            self.waffenNr = waffenNr
            self.size = 8
            self.schaden = 0
            self.waffenBild = waffenBilder[waffenNr]




    def moveAndShow(self, screen):
        self.posY -= self.speed
        screen.blit(self.waffenBild, (self.posX, self.posY))

    def moveLaserAndCheck(self,gegnerListe, screen,statCounter, hit,animationListe):
        if self.posY < -self.size:
            self.schaden = 0
        if self.schaden > 0:
            self.moveAndShow(screen)
            waffenBox = pygame.Rect(self.posX, self.posY, self.size, self.size)
            for gegner in gegnerListe:
                if gegner.live > 0:
                    if gegner.checkTod(waffenBox):

                        for animation in animationListe:
                            if animation.enable:
                                animation.startAnimation(gegner.posX, gegner.posY, gegner.size)
                                break


                        pygame.mixer.Sound.play(hit)

                        schaden = self.schaden
                        self.schaden = schaden - gegner.live
                        gegner.live = gegner.live - schaden
                        if self.schaden < 0:
                            self.schaden = 0
                        if gegner.live <= 0:
                            statCounter.increaseMoney(int(gegner.startLive/2))
                        statCounter.increaseMoney(int(schaden))

    def moveBombAndCheck(self, gegnerListe, screen,statCounter,hit,animationListe):
        if self.posY < -self.size:
            self.schaden = 0
        if self.schaden > 0:
            self.moveAndShow(screen)
            waffenBox = pygame.Rect(self.posX, self.posY, self.size, self.size)
            for gegner in gegnerListe:
                if gegner.live > 0:
                    if gegner.checkTod(waffenBox):

                        for animation in animationListe:
                            if animation.enable:
                                animation.startAnimation(gegner.posX, gegner.posY, gegner.size)
                                break
                        pygame.mixer.Sound.play(hit)
                        schaden = self.schaden
                        self.schaden = schaden - gegner.live
                        gegner.live = gegner.live - schaden
                        if self.schaden < 0:
                            self.schaden = 0
                        if gegner.live <= 0:
                            statCounter.increaseMoney(int(gegner.startLive/2))
                        if int(schaden) > 5000:
                            statCounter.increaseMoney(5000)
                        else:
                            statCounter.increaseMoney(int(schaden))

    def moveSchrotAndCheck(self, gegnerListe, screen, winkel, num,statCounter,hit,animationListe ):
        if self.posY < -self.size:
            self.schaden = 0
        if self.schaden > 0:
            self.posX = self.posX + self.speed * math.sin((-math.pi / 4) + num * winkel)
            self.posY = self.posY - self.speed * math.cos((-math.pi / 4) + num * winkel)
            screen.blit(self.waffenBild, (self.posX, self.posY))
            waffenBox = pygame.Rect(self.posX, self.posY, self.size, self.size)
            for gegner in gegnerListe:
                if gegner.live > 0:
                    if gegner.checkTod(waffenBox):

                        for animation in animationListe:
                            if animation.enable:
                                animation.startAnimation(gegner.posX, gegner.posY, gegner.size)
                                break
                        pygame.mixer.Sound.play(hit)
                        schaden = self.schaden
                        self.schaden = schaden - gegner.live
                        gegner.live = gegner.live - schaden
                        if self.schaden < 0:
                            self.schaden = 0
                        if gegner.live <= 0:
                            statCounter.increaseMoney(int(gegner.startLive/2))
                        statCounter.increaseMoney(int(schaden))

