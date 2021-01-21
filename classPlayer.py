import pygame
class player:

    eigenerSpeed = 5
    playerSize = 100
    playerX = 450
    playerY = 500
    live = 0
    maxLive = 0

    def __init__(self, curentPlayer):
        self.eigenerSpeed = curentPlayer.speedLevelArray[curentPlayer.speedLevel]
        self.playerSize = 150
        self.playerX = 450
        self.playerY = 720
        self.live = curentPlayer.healthLevelArray[curentPlayer.healthLevel]
        self.maxLive = curentPlayer.healthLevelArray[curentPlayer.healthLevel]
    def printLive(self,screen):
        pygame.draw.rect(screen,((1-(self.live/self.maxLive))*255,(self.live/self.maxLive)*255,0),(self.playerX, self.playerY+self.playerSize, int((self.live/self.maxLive)*self.playerSize), 3), 0)
