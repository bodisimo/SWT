import pygame

class animation:
    playerX = 0
    playerY = 0
    sonntagX = 0
    sonntagY = 0

    
    laserX = -100
    laserY = -100
    laserShoot = True

    cooldownCnt = 0
    cooldown = True




    #playerImage = 0

    def __init__(self):
        self.sonntagX = 1650
        self.sonntagY = 1600
        
        self.playerX = 1850
        self.playerY = 1800
        image = pygame.image.load("Bilder/alien/alien.png")
        image = pygame.transform.rotate(image, 45)
        self.playerImage = pygame.transform.scale(image, (70, 70))
        image = pygame.image.load("Bilder/alien/sonntag.png")
        image = pygame.transform.rotate(image, 45)
        self.sonntagImage = pygame.transform.scale(image, (100, 100))





        image = pygame.image.load("Bilder/explosion/fire1.png")
        image = pygame.transform.scale(image, (20, 20))
        self.fireImage = image




    def printSonntagAnimation(self,screen):
        self.sonntagX -= 4
        self.sonntagY -= 4


        screen.blit(self.sonntagImage,(self.sonntagX,self.sonntagY))






    def printPlayerAnimation(self, screen):

        if self.playerY < -100:
            self.laserShoot = True
            self.playerX = 1850
            self.playerY = 1800
            self.sonntagX = 1650
            self.sonntagY = 1600
        if self.playerY < 700:
            if self.laserShoot:
                self.laserX = self.playerX
                self.laserY = self.playerY
                self.laserShoot = False
            self.printFire(screen)
        self.playerX -= 4
        self.playerY -= 4
        screen.blit(self.playerImage,(self.playerX,self.playerY))
        
    def printFire(self,screen):
        self.laserX -= 5
        self.laserY -= 5
        screen.blit(self.fireImage,(self.laserX,self.laserY))




