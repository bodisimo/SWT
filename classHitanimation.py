
import pygame


class hitanimation:

    posX = 0
    posY = 0
    enable = True
    cnt = 0
    size = 0
    bild = 0

    def __init__(self,bild):
        self.bild = bild

    def startAnimation(self, posX, posY, size):
        self.posX = posX
        self.posY = posY
        self.size = size
        self.enable = False

    def printAnimation(self,screen):
        if self.cnt < 5 and self.enable == False:
            screen.blit(pygame.transform.scale(self.bild, (self.size, self.size)), (self.posX, self.posY))
            self.cnt += 1
        else:
            self.cnt = 0
            self.enable = True