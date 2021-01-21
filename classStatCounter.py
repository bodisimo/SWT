import pygame


class statCounter:
    money = 0
    gegnerGesammtLeben = 0
    neededKills = 100
    munze = 0
    textMünzen = 0


    def __init__(self, gegnerListe):
        self.money = 0
        self.fortschritt = 0
        image = pygame.image.load("Bilder/upgrades/munze.png")
        self.munze = pygame.transform.scale(image, (40, 40))
        leben = 0
        for gegner in gegnerListe:
            leben += gegner.live
        self.gegnerGesammtLeben = leben



    def resetStat(self):
        self.money = 0
        self.fortschritt = 0

    def increaseMoney(self, x):
        self.money += x

    def drawMoney(self, screen):
        screen.blit(self.munze, (10, 10))
        anzahl = self.renderText(str(self.money), 70)
        screen.blit(anzahl, (70, 10))


    def renderText(self, text, size, rot=255, grün=255, blau=255):
        sys_font = pygame.font.SysFont("none", size)
        rendered = sys_font.render(text, 0, (rot, grün, blau))
        return rendered

    def berechneFortschritt(self, gegnerListe, currentPlayer):
        gegnerLive = 0
        for gegner in gegnerListe:
            if gegner.live > 0:
                gegnerLive += gegner.live
        currentPlayer.xp = int((self.gegnerGesammtLeben-gegnerLive)/(self.gegnerGesammtLeben)*100)
        currentPlayer.savePlayerStat()


