import math
import pygame
import clasSystem

class Cooldown:


    frameCountLaser = 0
    enableLaser = True
    frameCountBombe = 0
    enableBombe = True
    frameCountShotgun = 0
    enableShotgun = True
    kanonenListe = 0
    shotgunList = 0
    player = 0
    laserSize = 0
    laserX = []
    laserY = []
    bombeX = []
    bombeY = []
    shotgunX = []
    shotgunY = []
    cooldownLaser = 0
    cooldownBombe = 0
    cooldownShotgun = 0
    radius = 35
    bildVonLaser = 0
    bildVonBombe = 0
    bildVonShotgun = 0
    settings = 0


    def __init__(self, kanonenListe, shotgunList, player, laserSize,bildVonLaser, bildVonBombe, bildVonShotgun,settings, playerStat):
        self.kanonenListe = kanonenListe
        self.player = player
        self.shotgunList = shotgunList
        self.laserSize = laserSize
        self.bildVonLaser = bildVonLaser
        self.bildVonBombe = bildVonBombe
        self.bildVonShotgun = bildVonShotgun
        self.settings = settings
        self.cooldownLaser = playerStat.laserReloadSpeedLevelArray[playerStat.laserReloadLevel]
        self.cooldownBombe = playerStat.bombReloadSpeedLevelArray[playerStat.bombReloadLevel]
        self.cooldownShotgun = playerStat.shotgunReloadTimeLevelArray[playerStat.shotgunReloadLevel]

    def ceckCooldown(self, player, playerStat):
        #aktualliesiere player
        self.player = player
        # Cooldown Laser
        if self.frameCountLaser < playerStat.laserReloadSpeedLevelArray[playerStat.laserReloadLevel] and not self.enableLaser:
            self.frameCountLaser += 1

        else:
            self.laserX = []
            self.laserY = []
            self.frameCountLaser = 0
            self.enableLaser = True

        # Cooldown Bombe
        if self.frameCountBombe < playerStat.bombReloadSpeedLevelArray[playerStat.bombReloadLevel] and not self.enableBombe:
            self.frameCountBombe += 1
            # delay für schluss, dass der sound mit der kanone übereinstimmt
            if self.frameCountBombe == 100:
                self.shootKanone(playerStat)
        else:
            self.bombeX = []
            self.bombeY = []
            self.frameCountBombe = 0
            self.enableBombe = True


        # Cooldown Shotgun
        if self.frameCountShotgun < playerStat.shotgunReloadTimeLevelArray[playerStat.shotgunReloadLevel] and not self.enableShotgun:
            self.frameCountShotgun += 1
            if self.frameCountShotgun == 30:
                self.shootShotgun(playerStat)
        else:
            self.shotgunX = []
            self.shotgunY = []
            self.frameCountShotgun = 0
            self.enableShotgun = True




    def shootKanone(self,playerStat):
        for waffe in self.kanonenListe:
            if waffe.schaden <= 0:
                print("kein schaden")
                waffe.schaden = playerStat.bombSchadenLevelArray[playerStat.bombDmgLevel] * playerStat.waffenLevelArray[playerStat.waffenLevel]
                waffe.posX = self.player.playerX + self.player.playerSize / 2 - 0.5* waffe.size
                waffe.posY = self.player.playerY
                return


    def shootShotgun(self,playerStat):
        for shotgun in self.shotgunList:
            dmgSum = 0
            for schrot in shotgun:
                dmgSum += schrot.schaden
            if dmgSum == 0:
                for schrot in shotgun:
                    schrot.schaden = playerStat.shotgunSchadenLevelArray[playerStat.shotgunDmgLevel] * playerStat.waffenLevelArray[playerStat.waffenLevel]
                    schrot.posX = self.player.playerX + self.player.playerSize / 2 -10
                    schrot.posY = self.player.playerY
                return






    def drawCooldown(self, screen):

#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun
        screen.blit(self.bildVonShotgun, (self.settings.breite / 2 +72, self.settings.hoehe -  69))

        self.shotgunX.append(int(self.radius * math.sin((2*math.pi/self.cooldownShotgun)*self.frameCountShotgun) + self.settings.breite/2 + 100))
        self.shotgunY.append(int(self.radius * math.cos((2*math.pi/self.cooldownShotgun)*self.frameCountShotgun)+self.settings.hoehe - 40))

        if self.enableShotgun:

            pygame.draw.circle(screen, (0, 200, 50), (self.settings.breite/2 + 100, self.settings.hoehe - 40), self.radius, 2)
        else:
            for i in range(0,len(self.shotgunX)):
                pygame.draw.rect(screen,(200,0,0), (self.shotgunX[i], self.shotgunY[i], 2,2))





#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe
        screen.blit(self.bildVonBombe, (self.settings.breite / 2 -130, self.settings.hoehe - 67))

        self.bombeX.append(int(self.radius * math.sin((2*math.pi/self.cooldownBombe)*self.frameCountBombe) + self.settings.breite/2 - 100))
        self.bombeY.append(int(self.radius * math.cos((2*math.pi/self.cooldownBombe)*self.frameCountBombe)+self.settings.hoehe - 40))

        if self.enableBombe:
            pygame.draw.circle(screen, (0, 200, 50), (self.settings.breite/2 - 100, self.settings.hoehe - 40), self.radius, 2)
        else:
            for i in range(0,len(self.bombeX)):
                pygame.draw.rect(screen,(200,0,0), (self.bombeX[i], self.bombeY[i], 2,2))






#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser
        screen.blit(self.bildVonLaser, (self.settings.breite/2-30, self.settings.hoehe - 67))

        self.laserX.append(int(self.radius * math.sin((2*math.pi/self.cooldownLaser)*self.frameCountLaser) + self.settings.breite/2))
        self.laserY.append(int(self.radius * math.cos((2*math.pi/self.cooldownLaser)*self.frameCountLaser)+self.settings.hoehe - 40))

        if self.enableLaser:
            pygame.draw.circle(screen, (0, 200, 50), (self.settings.breite/2, self.settings.hoehe - 40), self.radius, 2)
        else:
            for i in range(0,len(self.laserX)):
                pygame.draw.rect(screen,(200,0,0), (self.laserX[i], self.laserY[i], 2,2))

