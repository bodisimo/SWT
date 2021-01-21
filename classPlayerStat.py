import pygame
class playerStat:


    level = 0
    xp = 0

    laserDmgLevel = 0
    laserSpeedLevel = 0
    laserReloadLevel = 0

    bombDmgLevel = 0
    bombSizeLevel = 0
    bombReloadLevel = 0

    shotgunDmgLevel = 0
    shotgunBulletLevel = 0
    shotgunReloadLevel = 0
    money = 0
    questlevel = 0

    healthLevel = 0
    speedLevel = 0
    waffenLevel = 0



    healthLevelArray = [0,1,5,10,20,50,100,200,500,1000,2000, "max"]
    speedLevelArray = [0,3,4,5,6,7,8,9,10,11,12, "max"]
    waffenLevelArray = [0,1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,9,10, "max"]

    laserReloadSpeedLevelArray = [0,60,55,50,45,40,35,30,25,20,15,10,9,8,7,6,5, 99.99*60]
    laserSchadenLevelArray = [0,1,2,3,4,5,6,7,8,9,10, "max"]
    laserSpeedLevelArray = [0,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32, "max"]

    bombSchadenLevelArray = [0,10,25,40,60,100,200,400,600,1000,2000,5000,10000, "max"]
    bombSizeLevelArray = [0,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220, "max"]
    bombReloadSpeedLevelArray = [0,360,330,300,270,240,210,180,160,140, 120, 110, 101, 99.99*60]

    shotgunSchadenLevelArray = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,9,10, "max"]
    shotgunShrotLevelArray = [0,2,5,9,14,21,30,41,52,63,74,85,100,120,150,200,250,300, "max"]
    shotgunReloadTimeLevelArray = [0,600,560,520,480,440,400,360,320,280,240,220,200,180,160,140,120,100,80,70,60, 99.99*60]



    def __init__(self):
        attribut = self.getPlayer()
        self.level = int(attribut[0])
        self.xp = int(attribut[1])
        self.laserDmgLevel = int(attribut[2])
        self.laserSpeedLevel = int(attribut[3])
        self.laserReloadLevel = int(attribut[4])
        self.bombDmgLevel = int(attribut[5])
        self.bombSizeLevel = int(attribut[6])
        self.bombReloadLevel = int(attribut[7])
        self.shotgunDmgLevel = int(attribut[8])
        self.shotgunBulletLevel = int(attribut[9])
        self.shotgunReloadLevel = int(attribut[10])
        self.money = int(attribut[11])
        self.questlevel = int(attribut[12])

        self.healthLevel = int(attribut[13])
        self.speedLevel = int(attribut[14])
        self.waffenLevel = int(attribut[15])

        self.healthLevelCost = [0,50, 500, 1000, 5000, 10000, 25000, 100000, 500000, 1000000, "max"]
        self.speedLevelCost = [0,10, 50, 100, 250, 500, 1000, 2000, 5000, 10000, "max"]
        self.waffenLevelCost = [0,1000, 5000, 10000, 25000, 50000, 80000, 100000, 200000, 500000,1000000,1000000,1000000,1000000, "max"]

        self.laserDmgLevelCost = [0,10, 50, 100, 250, 500, 1000, 2000, 5000, 10000, "max"]
        self.laserSpeedLevelCost = [0,5, 25, 75, 100, 200, 400, 750, 1000, 1500,2000,2500,4000,7500,10000,13000,15000,20000,25000,40000,60000,100000,120000,150000,200000,250000,300000, "max"]
        self.laserReloadLevelCost = [0,10, 50, 100, 250, 500, 1000, 2000, 5000, 10000,20000,50000,100000,200000,500000,1000000, "max"]

        self.bombDmgLevelCost = [0,100, 200, 500, 1000, 4000, 10000, 25000, 100000, 200000, 500000, 1000000, "max"]
        self.bombSizeLevelCost = [0,20, 50, 200, 500, 2000,5000, 10000, 20000, 50000, 100000,200000,300000,400000,500000,600000,700000,800000,"max"]
        self.bombReloadLevelCost = [0,10, 50, 200, 1000, 5000, 10000, 50000,150000, 300000,500000,750000, "max"]

        self.shotgunDmgLevelCost = [0,10, 50, 200, 700, 2000, 8000, 18000, 24000, 50000,100000,200000,500000,800000,1000000, "max"]
        self.shotgunBulletLevelCost = [0,10, 100, 500, 2500, 5000, 10000, 20000, 50000, 80000,100000,200000,300000,400000,500000,700000,1000000, "max"]
        self.shotgunReloadLevelCost = [0,10, 50, 100, 250, 500, 2000, 10000, 50000, 100000, 300000,500000,750000,1000000,1000000,1000000,1000000,1000000,1000000,1000000, "max"]






    def savePlayerStat(self):
        f = open("playerstat", "w")
        saveText = ""
        saveText = saveText + str(self.level) + " "
        saveText = saveText + str(self.xp) + " "
        saveText = saveText + str(self.laserDmgLevel) + " "
        saveText = saveText + str(self.laserSpeedLevel) + " "
        saveText = saveText + str(self.laserReloadLevel) + " "
        saveText = saveText + str(self.bombDmgLevel) + " "
        saveText = saveText + str(self.bombSizeLevel) + " "
        saveText = saveText + str(self.bombReloadLevel) + " "
        saveText = saveText + str(self.shotgunDmgLevel) + " "
        saveText = saveText + str(self.shotgunBulletLevel) + " "
        saveText = saveText + str(self.shotgunReloadLevel) + " "
        saveText = saveText + str(self.money) + " "
        saveText = saveText + str(self.questlevel) + " "
        saveText = saveText + str(self.healthLevel) + " "
        saveText = saveText + str(self.speedLevel) + " "
        saveText = saveText + str(self.waffenLevel)


        f.write(saveText)
        f.close()

    def getPlayer(self):
        # level
        # xp
        # laser dmg level
        # laser dmg level
        # laser dmg level
        # bomb dmg level
        # bomb dmg level
        # bomb dmg level
        # shotgun dmg level
        # shotgun dmg level
        # shotgun dmg level
        # money
        # questlevel
        f = open("playerstat", "r")

        output = ""
        for line in f:
            output = output + line

        output = output.split(" ")
        return output

    def resetPlayerStat(self,currentPlayerStat):

        f = open("playerstat", "w")
        saveText = "1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1"
        f.write(saveText)
        currentPlayerStat = playerStat()
        f.close()






    def upgradeHealth(self, gekauftSound):
        if len(self.healthLevelArray)-2 > self.healthLevel:
            if self.healthLevelCost[self.healthLevel] <= self.money:
                self.money -= self.healthLevelCost[self.healthLevel]
                self.healthLevel += 1
                self.savePlayerStat()
                pygame.mixer.Sound.play(gekauftSound)

    def upgradePlayerSpeed(self, gekauftSound):
        if len(self.speedLevelArray)-2 > self.speedLevel:
            if self.speedLevelCost[self.speedLevel] <= self.money:
                self.money -= self.speedLevelCost[self.speedLevel]
                self.speedLevel += 1
                self.savePlayerStat()
                pygame.mixer.Sound.play(gekauftSound)
    def upgradeWaffen(self, gekauftSound):
        if len(self.waffenLevelArray)-2 > self.waffenLevel:
            print(len(self.waffenLevelArray))
            print("<= ")
            print(self.waffenLevel)
            print(self.waffenLevelCost[self.waffenLevel])
            if self.waffenLevelCost[self.waffenLevel] <= self.money:
                self.money -= self.waffenLevelCost[self.waffenLevel]
                self.waffenLevel += 1
                self.savePlayerStat()
                pygame.mixer.Sound.play(gekauftSound)
    def upgradeShotgunReload(self, gekauftSound):
        if len(self.shotgunReloadTimeLevelArray)-2> self.shotgunReloadLevel:
            if self.shotgunReloadLevelCost[self.shotgunReloadLevel] <= self.money:
                self.money -= self.shotgunReloadLevelCost[self.shotgunReloadLevel]
                self.shotgunReloadLevel += 1
                self.savePlayerStat()
                pygame.mixer.Sound.play(gekauftSound)
    def upgradeShotgunBullet(self, gekauftSound):
        if len(self.shotgunShrotLevelArray)-2> self.shotgunBulletLevel:
            if self.shotgunBulletLevelCost[self.shotgunBulletLevel] <= self.money:
                self.money -= self.shotgunBulletLevelCost[self.shotgunBulletLevel]
                self.shotgunBulletLevel += 1
                self.savePlayerStat()
                pygame.mixer.Sound.play(gekauftSound)
    def upgradeShotgunDmg(self, gekauftSound):
        if len(self.shotgunSchadenLevelArray)-2> self.shotgunDmgLevel:
            if self.shotgunDmgLevelCost[self.shotgunDmgLevel] <= self.money:
                self.money -= self.shotgunDmgLevelCost[self.shotgunDmgLevel]
                self.shotgunDmgLevel += 1
                self.savePlayerStat()
                pygame.mixer.Sound.play(gekauftSound)
    def upgradeBombDmg(self, gekauftSound):
        if len(self.bombSchadenLevelArray)-2> self.bombDmgLevel:
            if self.bombDmgLevelCost[self.bombDmgLevel] <= self.money:
                self.money -= self.bombDmgLevelCost[self.bombDmgLevel]
                self.bombDmgLevel += 1
                self.savePlayerStat()
                pygame.mixer.Sound.play(gekauftSound)
    def upgradeBombSize(self, gekauftSound):
        if len(self.bombSizeLevelArray)-2> self.bombSizeLevel:
            if self.bombSizeLevelCost[self.bombSizeLevel] <= self.money:
                self.money -= self.bombSizeLevelCost[self.bombSizeLevel]
                self.bombSizeLevel += 1
                self.savePlayerStat()
                pygame.mixer.Sound.play(gekauftSound)
    def upgradeBombReload(self, gekauftSound):
        if len(self.bombReloadSpeedLevelArray)-2> self.bombReloadLevel:
            if self.bombReloadLevelCost[self.bombReloadLevel] <= self.money:
                self.money -= self.bombReloadLevelCost[self.bombReloadLevel]
                self.bombReloadLevel += 1
                self.savePlayerStat()
                pygame.mixer.Sound.play(gekauftSound)
    def upgradeLaserDmg(self, gekauftSound):
        if len(self.laserSchadenLevelArray)-2> self.laserDmgLevel:
            if self.laserDmgLevelCost[self.laserDmgLevel] <= self.money:
                self.money -= self.laserDmgLevelCost[self.laserDmgLevel]
                self.laserDmgLevel += 1
                self.savePlayerStat()
                pygame.mixer.Sound.play(gekauftSound)
    def upgradeLaserSpeed(self, gekauftSound):
        if len(self.laserSpeedLevelArray)-2> self.laserSpeedLevel:
            if self.laserSpeedLevelCost[self.laserSpeedLevel] <= self.money:
                self.money -= self.laserSpeedLevelCost[self.laserSpeedLevel]
                self.laserSpeedLevel += 1
                self.savePlayerStat()
                pygame.mixer.Sound.play(gekauftSound)
    def upgradeLaserReload(self, gekauftSound):
        if len(self.laserReloadSpeedLevelArray)-2> self.laserReloadLevel:
            print(len(self.laserReloadSpeedLevelArray)-2)
            print(self.laserReloadLevel)
            if self.laserReloadLevelCost[self.laserReloadLevel] <= self.money:
                self.money -= self.laserReloadLevelCost[self.laserReloadLevel]
                self.laserReloadLevel += 1
                self.savePlayerStat()
                pygame.mixer.Sound.play(gekauftSound)

    def nextQuestlevel(self):
        self.questlevel += 1
        self.savePlayerStat()