import pygame
import sys
import math

import clasSystem
import classMusic
import classPlayer
import classPlayerStat
import classGegner
import classWaffe
import classGameLevel
import classCooldown
import classAnimation
import classStatCounter
import startGame
import random
import classHitanimation

#textTryAgain = pygame.transform.scale(textTryAgain, (2 * textSize1, textSize1))
#textNextLevel = pygame.transform.scale(textNextLevel, (2 * textSize1, textSize1))
#textMissionFailed = pygame.transform.scale(textMissionFailed, (2 * textSize1, textSize1))
#textLevelComplete = pygame.transform.scale(textLevelComplete, (2 * textSize1, textSize1))



def zeichneGewonnen():
    levelCompleteBox = pygame.Rect((5 / 10) * settings.breite - textSize1, (1 / 10) * settings.hoehe, 2 * textSize1,textSize1)
    nextLevelBox = pygame.Rect(pygame.Rect((3 / 10) * settings.breite - textSize1, (8 / 10) * settings.hoehe, 2 * textSize1,textSize1))
    menuBox = pygame.Rect(pygame.Rect((7 / 10) * settings.breite - textSize1, (8 / 10) * settings.hoehe, 2 * textSize1,textSize1))


    zeichne = True
    while zeichne:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                currentPlayerStat.savePlayerStat()
                sys.exit()
        pressed2 = pygame.key.get_pressed()
        mousePos2 = pygame.mouse.get_pos()
        # mouseKlick[0] = linksklick, 1 ist laufrad, 2 ist rechte maustaste
        mouseKlick2 = pygame.mouse.get_pressed()


        # hintergrund
        screen.blit(hintergrundBild, (0, 0))
        screen.blit(textLevelComplete, ((5 / 10) * settings.breite - textSize1, (1 / 10) * settings.hoehe))

        money = renderText("You earned " + str(statCounter.money) + " coins", 50)
        screen.blit(money, ((5 / 10) * settings.breite-int(money.get_width()/2) , (4 / 10) * settings.hoehe))

        if nextLevelBox.collidepoint(mousePos2) or pressed2[pygame.K_SPACE]:
            textNextLevelGros = pygame.transform.scale(textNextLevel, (2 * textSize1 + 40, textSize1 + 20))
            screen.blit(textNextLevelGros, ((3 / 10) * settings.breite - textSize1 - 20, (8 / 10) * settings.hoehe -10))
            if mouseKlick2[0] or pressed2[pygame.K_SPACE]:
                zeichne = False
                settings.changeMode([False, True, False])
                settings.backToGame = True

        else:
            screen.blit(textNextLevel, nextLevelBox)

        if menuBox.collidepoint(mousePos2) or pressed2[pygame.K_m]:
            textMenuGros = pygame.transform.scale(textMenu, (2 * textSize1 + 40, textSize1 + 20))
            screen.blit(textMenuGros, ((7 / 10) * settings.breite - textSize1 - 20, (8 / 10) * settings.hoehe -10))
            if mouseKlick2[0] or pressed2[pygame.K_m]:
                zeichne = False
                settings.changeMode([True, False, False])
        else:
            screen.blit(textMenu, menuBox)

        pygame.display.update()

def zeichneVerloren():
    tryAgainBox = pygame.Rect(pygame.Rect((3 / 10) * settings.breite - textSize1, (8 / 10) * settings.hoehe, 2 * textSize1,textSize1))
    menuBox = pygame.Rect(pygame.Rect((7 / 10) * settings.breite - textSize1, (8 / 10) * settings.hoehe, 2 * textSize1,textSize1))


    zeichne = True
    while zeichne:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                currentPlayerStat.savePlayerStat()
                sys.exit()
        pressed2 = pygame.key.get_pressed()
        mousePos2 = pygame.mouse.get_pos()
        # mouseKlick[0] = linksklick, 1 ist laufrad, 2 ist rechte maustaste
        mouseKlick2 = pygame.mouse.get_pressed()


        # hintergrund
        screen.blit(hintergrundBild, (0, 0))
        screen.blit(textMissionFailed, ((5 / 10) * settings.breite - textSize1, (1 / 10) * settings.hoehe))

        money = renderText("You earned " + str(statCounter.money) + " coins", 50)
        screen.blit(money, ((5 / 10) * settings.breite-int(money.get_width()/2) , (4 / 10) * settings.hoehe))


        if tryAgainBox.collidepoint(mousePos2) or pressed2[pygame.K_SPACE]:
            textTryAgainGros = pygame.transform.scale(textTryAgain, (2 * textSize1 + 40, textSize1 + 20))
            screen.blit(textTryAgainGros, ((3 / 10) * settings.breite - textSize1 - 20, (8 / 10) * settings.hoehe -10))
            if mouseKlick2[0] or pressed2[pygame.K_SPACE]:
                zeichne = False
                settings.changeMode([False, True, False])
                settings.backToGame = True
        else:
            screen.blit(textTryAgain, tryAgainBox)

        if menuBox.collidepoint(mousePos2) or pressed2[pygame.K_m]:
            textMenuGros = pygame.transform.scale(textMenu, (2 * textSize1 + 40, textSize1 + 20))
            screen.blit(textMenuGros, ((7 / 10) * settings.breite - textSize1 - 20, (8 / 10) * settings.hoehe -10))
            if mouseKlick2[0] or pressed2[pygame.K_m]:
                zeichne = False
                settings.changeMode([True, False, False])

        else:
            screen.blit(textMenu, menuBox)

        pygame.display.update()












def moveEnemyRainmode():
    for gegner in gegnerListe:
        gegner.moveDown()

def zeichneRainmode(statCounter):
    screen.blit(hintergrundBild, (0, 0))
    screen.blit(spielerBild, (player.playerX, player.playerY))
    player.printLive(screen)

    for gegner in gegnerListe:
        if gegner.live > 0:
            gegner.zeichneGegner(screen)
            gegner.printLive(screen)
            if gegner.schaden > 0:
                gegner.moveShoot(screen)
                gegner.checkPlayerGetroffen(player, hit1)

        if player.live <= 0 or playerCollideEnemyOrGround(player):
            settings.changeMode([True,False,False])
            currentPlayerStat.money += statCounter.money





    #hier werden auch die münzen gezählt
    moveWaffen(statCounter)
    cooldown.drawCooldown(screen)
    zahnradBox = pygame.Rect(settings.breite-50,10,40,40)
    if zahnradBox.collidepoint(mousePos):
        if mouseKlick[0]:
            pauseMenu()

    screen.blit(zahnrad, zahnradBox)
    statCounter.drawMoney(screen)
    screen.blit(time, (settings.breite/2 - 60,0))

    pygame.display.update()



def appendReihe(gegnerListe, neue):
    for gegner in neue:
        gegnerListe.append(gegner)
    return gegnerListe

def makeGegnerReihe(anzahl, gegnerNr=0, leben=1, schaden=1, size=1, speed=4, moveDownSpeed=50,schussProTausend=10, name="boss"):
    bilder = []
    bilder.append(pygame.transform.scale(gegnerBilder[0], (size, size)))
    bilder.append(pygame.transform.scale(gegnerBilder[1], (size, size)))
    bilder.append(pygame.transform.scale(gegnerBilder[2], (size, size)))
    bilder.append(pygame.transform.scale(gegnerBilder[3], (int(size / 5), int(size / 5))))
    bilder.append(pygame.transform.scale(gegnerBilder[4], (size, int(1.2 * size))))

    abstand = int(settings.screenX / (anzahl + 1))
    ausgabe = []
    for i in range(1, anzahl + 1):
        ausgabe.append(classGegner.gegner(i * abstand - size / 2, -100, gegnerNr, bilder, leben, schaden, size, speed,moveDownSpeed, schussProTausend, name))
    return ausgabe


def generateGegnerLine(gegnerListe,currentLive, anzahl, size, speed, moveDownSpeed):
    currentLive += 0.05
    return gegnerListe.append(makeGegnerReihe(anzahl, int(random()*2), currentLive, 1, size, speed, moveDownSpeed, 10+random()*50)), currentLive




def generateGegner(gegnerListe,currentLive):
    return gegnerListe.append(classGegner.gegner(int(random()*settings.breite), -50, int(random()*2), gegnerBilder, currentLive, 1, int(20+random()*20), 3+random()*3, int(2+random()*4),10+random()*100))



def pauseMenu():
    pause = True
    while pause:
        textExitBox = pygame.Rect((5 / 10) * settings.breite - textSize1, (8 / 10) * settings.hoehe, 2 * textSize1,
                                  textSize1)
        textMusicVolumeBox = pygame.Rect((1 / 10) * settings.breite, (1 / 15) * settings.hoehe, 2 * textSize1,
                                         textSize1)
        textEffectVolumeBox = pygame.Rect((1 / 10) * settings.breite, (4 / 15) * settings.hoehe, 2 * textSize1,
                                          textSize1)
        textBackBox = pygame.Rect((1 / 2 * settings.breite - textEffectVolumeBox.size[0] / 2),
                                         (8 / 15) * settings.hoehe, 2 * textSize1, textSize1)

        musicVolumeBalken = pygame.Rect(settings.breite * (9 / 20), (10 / 62) * settings.hoehe,
                                        settings.breite * (1 / 2), settings.hoehe / 100)
        effectVolumeBalken = pygame.Rect(settings.breite * (9 / 20), (22 / 62) * settings.hoehe,
                                         settings.breite * (1 / 2), settings.hoehe / 100)

        musicVolumeCircle = pygame.draw.circle(screen, (100, 100, 255), (
            settings.musicVolume * settings.breite / 2 + musicVolumeBalken.bottomleft[0],
            musicVolumeBalken.center[1]),
                                               25)
        effectVolumeCircle = pygame.draw.circle(screen, (100, 100, 255), (
            settings.effectVolume * settings.breite / 2 + effectVolumeBalken.bottomleft[0],
            effectVolumeBalken.center[1]), 25)

        pause = True
        while pause:
            # eingabeüberprüfung
            frameCountMusic = 0
            enableMusicChange = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    currentPlayerStat.savePlayerStat()
                    sys.exit()
            pressed2 = pygame.key.get_pressed()
            mousePos2 = pygame.mouse.get_pos()
            # mouseKlick[0] = linksklick, 1 ist laufrad, 2 ist rechte maustaste
            mouseKlick2 = pygame.mouse.get_pressed()
            # hintergrund
            screen.blit(hintergrundBild, (0, 0))
            # verschieben von exit und überprüfen ob maus drauf zeigt
            if not textExitBox.collidepoint(mousePos2):
                screen.blit(textExit, textExitBox)
            if textExitBox.collidepoint(mousePos2):
                textExitgroß = pygame.transform.scale(textExit, (2 * textSize1 + 40, textSize1 + 20))
                screen.blit(textExitgroß,
                            ((5 / 10) * settings.breite - textSize1 - 20, (8 / 10) * settings.hoehe - 10))



                if mouseKlick2[0]:
                    settings.changeMode([True,False,False])
                    pause = False





            # überprüfung ob maus auf payer reset
            if not textBackBox.collidepoint(mousePos2) or pressed2[pygame.K_SPACE]:
                screen.blit(textBack, textBackBox)
            if textBackBox.collidepoint(mousePos2):
                textBackGroß = pygame.transform.scale(textBack, (2 * textSize1 + 40, textSize1 + 20))
                screen.blit(textBackGroß, (
                    (((1 / 2) * settings.breite - textEffectVolumeBox.size[0] / 2) - 20),
                    ((8 / 15) * settings.hoehe - 10)))
                if mouseKlick2[0]:
                    pause = False

            # wenn die maus auf dem musikknopf ist lässt sich der knopf bewegen
            if musicVolumeCircle.collidepoint(mousePos2) and mouseKlick2[0]:
                if mousePos2[0] > musicVolumeBalken.bottomleft[0] and mousePos2[0] < musicVolumeBalken.bottomright[
                    0]:
                    settings.musicVolume = (mousePos2[0] - musicVolumeBalken.bottomleft[0]) / (
                            musicVolumeBalken.bottomright[0] - musicVolumeBalken.bottomleft[0])

            if musicVolumeBalken.collidepoint(mousePos2) and mouseKlick2[0]:
                settings.musicVolume = (mousePos2[0] - musicVolumeBalken.bottomleft[0]) / (
                        musicVolumeBalken.bottomright[0] - musicVolumeBalken.bottomleft[0])

            # wenn die maus auf dem soundknopf ist lässt sich der knopf bewegen
            if effectVolumeCircle.collidepoint(mousePos2) and mouseKlick2[0]:
                if mousePos2[0] > effectVolumeBalken.bottomleft[0] and mousePos2[0] < \
                        effectVolumeBalken.bottomright[0]:
                    settings.effectVolume = (mousePos2[0] - effectVolumeBalken.bottomleft[0]) / (
                            effectVolumeBalken.bottomright[0] - effectVolumeBalken.bottomleft[0])
            if effectVolumeBalken.collidepoint(mousePos2) and mouseKlick2[0]:
                settings.effectVolume = (mousePos2[0] - effectVolumeBalken.bottomleft[0]) / (
                        effectVolumeBalken.bottomright[0] - effectVolumeBalken.bottomleft[0])

            if frameCountMusic < 30 and not frameCountMusic:
                frameCountMusic += 1
            else:
                frameCountMusic = 0
                enableMusicChange = True

            if textMusicVolumeBox.collidepoint(mousePos2) and mouseKlick2[0] and enableMusicChange:
                enableMusicChange = False
                music.playNextSong()

            # anzeigen der Texte
            screen.blit(textMusicVolume, textMusicVolumeBox)
            screen.blit(textEffectVolume, textEffectVolumeBox)
            # anzeigen der linien der lautstärkeregelung
            pygame.draw.rect(screen, (255, 255, 255), musicVolumeBalken, 0)
            pygame.draw.rect(screen, (255, 255, 255), effectVolumeBalken, 0)
            # anzeigen der punkte für die lautstärkeregelung
            musicVolumeCircle = pygame.draw.circle(screen, (100, 100, 255), (
                settings.musicVolume * settings.breite / 2 + musicVolumeBalken.bottomleft[0],
                musicVolumeBalken.center[1]), 25)
            effectVolumeCircle = pygame.draw.circle(screen, (100, 100, 255), (
                settings.effectVolume * settings.breite / 2 + effectVolumeBalken.bottomleft[0],
                effectVolumeBalken.center[1]), 25)
            # aktualisierung der lautstärke
            akualisiereVolume()
            pygame.display.update()



def set_score(name, score, platz):
    f = open("score", "r")
    stats = f.read()
    f.close()
    einzeln = stats.split("\n")
    f = open("score", "w")
    f.write("Player Score")
    if platz == 1:
        return True


def check_score(own_score):
    f = open("score", "r")
    plat = 0
    for line in f:
        stats = line.split(" ")
        intstat = int(stats[1])
        if intstat < own_score:
            plat = plat + 1
    return 4 - plat



def zeichnen(statCounter):
    screen.blit(hintergrundBild, (0, 0))
    screen.blit(spielerBild, (player.playerX, player.playerY))
    player.printLive(screen)
    gewonnen = True
    verloren = False

    for gegner in gegnerListe:
        if gegner.live > 0:
            gewonnen = False
            gegner.zeichneGegner(screen)
            gegner.printLive(screen)
            if gegner.gegnerNr >= 4:
                gegner.printName(screen)
            if gegner.schaden > 0:
                gegner.moveShoot(screen)
                gegner.checkPlayerGetroffen(player, hit3)
            if player.live <= 0:
                statCounter.berechneFortschritt(gegnerListe, currentPlayerStat)
                currentPlayerStat.money += statCounter.money
                zeichneVerloren()
                return

    verloren = playerCollideEnemyOrGround(player)

    if verloren:
        statCounter.berechneFortschritt(gegnerListe, currentPlayerStat)
        currentPlayerStat.money += statCounter.money
        zeichneVerloren()
        return

    if gewonnen:
        statCounter.money += (currentPlayerStat.questlevel**2)*2
        currentPlayerStat.money += statCounter.money
        currentPlayerStat.nextQuestlevel()
        currentPlayerStat.xp = 0
        currentPlayerStat.savePlayerStat()
        zeichneGewonnen()
        return


    #hier werden auch die münzen gezählt
    moveWaffen(statCounter)
    cooldown.drawCooldown(screen)

    for animation in animationListe:
        if not animation.enable:
            animation.printAnimation(screen)




    zahnradBox = pygame.Rect(settings.breite-50,10,40,40)
    if zahnradBox.collidepoint(mousePos) or pressed[pygame.K_ESCAPE]:
        if mouseKlick[0] or pressed[pygame.K_ESCAPE]:
            pauseMenu()

    screen.blit(zahnrad, zahnradBox)
    statCounter.drawMoney(screen)


    pygame.display.update()




def moveGegner():

    gegnerBoxLinks = pygame.Rect(gegnerListe[0].posX, 0, 1, settings.hoehe)
    gegnerBoxRechts = pygame.Rect(gegnerListe[-1].posX + gegnerListe[-1].size, 0, 1, settings.hoehe)


    if gegnerBoxLinks.colliderect(leftWall) and not gegnerRichtungRight:
        for gegner in gegnerListe:
            gegner.moveDown()
        return True
    elif gegnerBoxRechts.colliderect(rightWall) and gegnerRichtungRight:
        for gegner in gegnerListe:
            gegner.moveDown()
        return False
    if gegnerRichtungRight:
        for gegner in gegnerListe:
            gegner.moveRight()
        return True
    elif not gegnerRichtungRight:
        for gegner in gegnerListe:
            gegner.moveLeft()
        return False



def moveWaffen(statCounter) :
    #laser
    for laser in laserListe:
        laser.moveLaserAndCheck(gegnerListe, screen,statCounter, hit1,animationListe)
    #bombe
    for bomb in kanonenListe:
       bomb.moveBombAndCheck(gegnerListe, screen,statCounter, hit2,animationListe)
    #shotgun
    for shotgun in shotgunList:
        winkel = berechneShotgunWinkel(shotgun)
        num = -1
        for schrot in shotgun:
            num += 1
            schrot.moveSchrotAndCheck(gegnerListe, screen, winkel, num,statCounter,hit1,animationListe)

def berechneShotgunWinkel(shotgun):
    num = -1
    for schrot in shotgun:
        num += 1
    winkel = (math.pi / 2) / num
    return winkel

def shootLaser():
    for waffe in laserListe:
        if waffe.schaden <= 0:
            waffe.schaden = currentPlayerStat.laserSchadenLevelArray[currentPlayerStat.laserDmgLevel] * currentPlayerStat.waffenLevelArray[currentPlayerStat.waffenLevel]
            waffe.posX = player.playerX + player.playerSize / 2 - laserSize
            waffe.posY = player.playerY
            pygame.mixer.Sound.play(laser)
            return False
    return False


def shootKanone():
    for waffe in kanonenListe:
        if waffe.schaden <= 0:
            waffe.schaden = currentPlayerStat.bombSchadenLevelArray[currentPlayerStat.bombDmgLevel] * currentPlayerStat.waffenLevelArray[currentPlayerStat.waffenLevel]
            waffe.posX = player.playerX + player.playerSize / 2 - 3 * laserSize
            waffe.posY = player.playerY


def shootShotgun():
    for schrot in shotgun:
        schrot.schaden = currentPlayerStat.shotgunSchadenLevelArray[currentPlayerStat.shotgunDmgLevel] * currentPlayerStat.waffenLevelArray[currentPlayerStat.waffenLevel]
        schrot.posX = player.playerX + player.playerSize / 2 - laserSize
        schrot.posY = player.playerY


def akualisiereVolume():
    pygame.mixer.Sound.set_volume(laser, settings.effectVolume)
    pygame.mixer.Sound.set_volume(kanone, settings.effectVolume)
    pygame.mixer.Sound.set_volume(shotgunSound, settings.effectVolume)
    pygame.mixer.Sound.set_volume(gekauftSound, settings.effectVolume)
    pygame.mixer.Sound.set_volume(schreiben1, 0.7*settings.effectVolume)
    pygame.mixer.Sound.set_volume(schreiben2, 0.7*settings.effectVolume)
    pygame.mixer.Sound.set_volume(schreiben3, 0.7*settings.effectVolume)
    pygame.mixer.Sound.set_volume(hit1, 1.5*settings.effectVolume)
    pygame.mixer.Sound.set_volume(hit2, 1.5*settings.effectVolume)
    pygame.mixer.Sound.set_volume(hit3, settings.effectVolume)

    pygame.mixer.music.set_volume(0.8*settings.musicVolume)


def playerCollideEnemyOrGround(player):
    playerBox = pygame.Rect(player.playerX, player.playerY, player.playerSize, player.playerSize)
    for gegner in gegnerListe:
        gegnerBox = pygame.Rect(gegner.posX, gegner.posY, gegner.size, gegner.size)
        if gegner.live > 0 and playerBox.colliderect(gegnerBox):
            return True
        elif gegner.live > 0 and gegnerBox.colliderect(bottomWall):
            return True
    return False


def printMenu():


    pressed = pygame.key.get_pressed()



    if settings.menu == True and settings.levelModeActive == True:
        settings.changeMode([False, True, False])




    screen.blit(hintergrundBild, (0, 0))


    pygame.draw.polygon(screen, (200,200,200), [(0,150),(150,150),(200,200),(0,200)])
    pygame.draw.polygon(screen, (200,200,200), [(250,150),(2000,150),(2000,200),(300,200)])

    pygame.draw.polygon(screen, (200,200,200), [(0,450),(450,450),(500,500),(0,500)])
    pygame.draw.polygon(screen, (200,200,200), [(550,450),(2000,450),(2000,500),(600,500)])

    pygame.draw.polygon(screen, (200,200,200), [(0,850),(850,850),(900,900),(0,900)])
    pygame.draw.polygon(screen, (200,200,200), [(950,850),(2000,850),(2000,900),(1000,900)])

    animation.printPlayerAnimation(screen)
    animation.printSonntagAnimation(screen)


    textLevelBox = pygame.Rect((1 / 10) * settings.breite, (2 / 10) * settings.hoehe, 2 * textSize1, textSize1)
    textEndlessBox = pygame.Rect(settings.breite - 2 * textSize1 - (1 / 10) * settings.breite,
                                 (2 / 10) * settings.hoehe, 2 * textSize1, textSize1)
    textSettingsBox = pygame.Rect((1 / 20) * settings.breite, (6 / 10) * settings.hoehe, 2 * textSize1, textSize1)
    textExitBox = pygame.Rect((5 / 10) * settings.breite - textSize1, (6 / 10) * settings.hoehe, 2 * textSize1,
                              textSize1)
    textUpgradesBox = pygame.Rect((19 / 20) * settings.breite - 2 * textSize1, (6 / 10) * settings.hoehe, 2 * textSize1,
                                  textSize1)

    if textLevelBox.collidepoint(mousePos)  or pressed[pygame.K_SPACE]:
        textLevelgroß = pygame.transform.scale(textLevel, (2 * textSize1 + 40, textSize1 + 20))
        screen.blit(textLevelgroß, ((1 / 10) * settings.breite - 20, (2 / 10) * settings.hoehe - 10))
        if mouseKlick[0] or pressed[pygame.K_SPACE]:
            # beendet das Menü
            return [False, True, False]
    else:
        screen.blit(textLevel, textLevelBox)

    if textEndlessBox.collidepoint(mousePos):
        textEndlessgroß = pygame.transform.scale(textEndless, (2 * textSize1 + 40, textSize1 + 20))
        screen.blit(textEndlessgroß,
                    (settings.breite - 2 * textSize1 - (1 / 10) * settings.breite - 20, (2 / 10) * settings.hoehe - 10))
        if mouseKlick[0]:
            return [False, False, True]
    else:
        screen.blit(textEndless, textEndlessBox)

    if textSettingsBox.collidepoint(mousePos):
        textSettingsgroß = pygame.transform.scale(textSettings, (2 * textSize1 + 40, textSize1 + 20))
        screen.blit(textSettingsgroß, ((1 / 20) * settings.breite - 20, (6 / 10) * settings.hoehe - 10))

        if mouseKlick[0]:

            textExitBox = pygame.Rect((5 / 10) * settings.breite - textSize1, (8 / 10) * settings.hoehe, 2 * textSize1,
                                      textSize1)
            textMusicVolumeBox = pygame.Rect((1 / 10) * settings.breite, (1 / 15) * settings.hoehe, 2 * textSize1,
                                             textSize1)
            textEffectVolumeBox = pygame.Rect((1 / 10) * settings.breite, (4 / 15) * settings.hoehe, 2 * textSize1,
                                              textSize1)
            textResetPlayerBox = pygame.Rect((1 / 2 * settings.breite - textEffectVolumeBox.size[0] / 2),
                                             (7 / 15) * settings.hoehe, 2 * textSize1, textSize1)

            musicVolumeBalken = pygame.Rect(settings.breite * (9 / 20), (10 / 62) * settings.hoehe,
                                            settings.breite * (1 / 2), settings.hoehe / 100)
            effectVolumeBalken = pygame.Rect(settings.breite * (9 / 20), (22 / 62) * settings.hoehe,
                                             settings.breite * (1 / 2), settings.hoehe / 100)

            musicVolumeCircle = pygame.draw.circle(screen, (100, 100, 255), (
                settings.musicVolume * settings.breite / 2 + musicVolumeBalken.bottomleft[0],
                musicVolumeBalken.center[1]),
                                                   25)
            effectVolumeCircle = pygame.draw.circle(screen, (100, 100, 255), (
                settings.effectVolume * settings.breite / 2 + effectVolumeBalken.bottomleft[0],
                effectVolumeBalken.center[1]), 25)

            while True:
                # eingabeüberprüfung
                frameCountMusic = 0
                enableMusicChange = True
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        currentPlayerStat.savePlayerStat()
                        sys.exit()
                pressed2 = pygame.key.get_pressed()
                mousePos2 = pygame.mouse.get_pos()
                # mouseKlick[0] = linksklick, 1 ist laufrad, 2 ist rechte maustaste
                mouseKlick2 = pygame.mouse.get_pressed()
                # hintergrund
                screen.blit(hintergrundBild, (0, 0))
                # verschieben von exit und überprüfen ob maus drauf zeigt
                if not textExitBox.collidepoint(mousePos2):
                    screen.blit(textExit, textExitBox)
                if textExitBox.collidepoint(mousePos2):
                    textExitgroß = pygame.transform.scale(textExit, (2 * textSize1 + 40, textSize1 + 20))
                    screen.blit(textExitgroß,
                                ((5 / 10) * settings.breite - textSize1 - 20, (8 / 10) * settings.hoehe - 10))
                    if mouseKlick2[0]: break

                # überprüfung ob maus auf payer reset
                if not textResetPlayerBox.collidepoint(mousePos2):
                    screen.blit(textResetPlayer, textResetPlayerBox)
                if textResetPlayerBox.collidepoint(mousePos2):
                    textResetPlayergroß = pygame.transform.scale(textResetPlayer, (2 * textSize1 + 40, textSize1 + 20))
                    screen.blit(textResetPlayergroß, (
                        (((1 / 2) * settings.breite - textEffectVolumeBox.size[0] / 2) - 20),
                        ((7 / 15) * settings.hoehe - 10)))
                    if mouseKlick2[0] and mouseKlick2[2]:
                        currentPlayerStat.resetPlayerStat(currentPlayerStat)


                # wenn die maus auf dem musikknopf ist lässt sich der knopf bewegen
                if musicVolumeCircle.collidepoint(mousePos2) and mouseKlick2[0]:
                    if mousePos2[0] > musicVolumeBalken.bottomleft[0] and mousePos2[0] < musicVolumeBalken.bottomright[
                        0]:
                        settings.musicVolume = (mousePos2[0] - musicVolumeBalken.bottomleft[0]) / (
                                musicVolumeBalken.bottomright[0] - musicVolumeBalken.bottomleft[0])

                if musicVolumeBalken.collidepoint(mousePos2) and mouseKlick2[0]:
                    settings.musicVolume = (mousePos2[0] - musicVolumeBalken.bottomleft[0]) / (
                            musicVolumeBalken.bottomright[0] - musicVolumeBalken.bottomleft[0])

                # wenn die maus auf dem soundknopf ist lässt sich der knopf bewegen
                if effectVolumeCircle.collidepoint(mousePos2) and mouseKlick2[0]:
                    if mousePos2[0] > effectVolumeBalken.bottomleft[0] and mousePos2[0] < \
                            effectVolumeBalken.bottomright[0]:
                        settings.effectVolume = (mousePos2[0] - effectVolumeBalken.bottomleft[0]) / (
                                effectVolumeBalken.bottomright[0] - effectVolumeBalken.bottomleft[0])
                if effectVolumeBalken.collidepoint(mousePos2) and mouseKlick2[0]:
                    settings.effectVolume = (mousePos2[0] - effectVolumeBalken.bottomleft[0]) / (
                            effectVolumeBalken.bottomright[0] - effectVolumeBalken.bottomleft[0])

                if frameCountMusic < 30 and not frameCountMusic:
                    frameCountMusic += 1
                else:
                    frameCountMusic = 0
                    enableMusicChange = True

                if textMusicVolumeBox.collidepoint(mousePos2) and mouseKlick2[0] and enableMusicChange:
                    enableMusicChange = False
                    music.playNextSong()

                # anzeigen der Texte
                screen.blit(textMusicVolume, textMusicVolumeBox)
                screen.blit(textEffectVolume, textEffectVolumeBox)
                # anzeigen der linien der lautstärkeregelung
                pygame.draw.rect(screen, (255, 255, 255), musicVolumeBalken, 0)
                pygame.draw.rect(screen, (255, 255, 255), effectVolumeBalken, 0)
                # anzeigen der punkte für die lautstärkeregelung
                musicVolumeCircle = pygame.draw.circle(screen, (100, 100, 255), (
                    settings.musicVolume * settings.breite / 2 + musicVolumeBalken.bottomleft[0],
                    musicVolumeBalken.center[1]), 25)
                effectVolumeCircle = pygame.draw.circle(screen, (100, 100, 255), (
                    settings.effectVolume * settings.breite / 2 + effectVolumeBalken.bottomleft[0],
                    effectVolumeBalken.center[1]), 25)
                # aktualisierung der lautstärke
                akualisiereVolume()
                pygame.display.update()
    else:
        screen.blit(textSettings, textSettingsBox)

    if textExitBox.collidepoint(mousePos) or pressed[pygame.K_ESCAPE]:
        textExitgroß = pygame.transform.scale(textExit, (2 * textSize1 + 40, textSize1 + 20))
        screen.blit(textExitgroß, ((5 / 10) * settings.breite - textSize1 - 20, (6 / 10) * settings.hoehe - 10))
        if mouseKlick[0] or pressed[pygame.K_ESCAPE]:
            currentPlayerStat.savePlayerStat()
            sys.exit()
    else:
        screen.blit(textExit, textExitBox)



    if textUpgradesBox.collidepoint(mousePos) or pressed[pygame.K_u]:
        textUpgradegroß = pygame.transform.scale(textUpgrades, (2 * textSize1 + 40, textSize1 + 20))
        screen.blit(textUpgradegroß, ((19 / 20) * settings.breite - 2 * textSize1 - 20, (6 / 10) * settings.hoehe - 10))
        if mouseKlick[0] or pressed[pygame.K_u]:
            # münzen aktualisieren
            textMünzenAnzahl = renderText(str(currentPlayerStat.money), int(settings.hoehe / 12), 200)

            hitboxPlayer = pygame.Rect(settings.breite * (1 / 10), settings.hoehe * (2 / 10), int(settings.breite/6),int(settings.breite/6))
            hitboxBombe = pygame.Rect(settings.breite * (3 / 10), settings.hoehe * (2 / 10), int(settings.breite/6),int(settings.breite/6))
            hitboxLaser = pygame.Rect(settings.breite * (5 / 10), settings.hoehe * (2 / 10), int(settings.breite/6),int(settings.breite/6))
            hitboxShotgun = pygame.Rect(settings.breite * (7 / 10), settings.hoehe * (2 / 10), int(settings.breite/6),int(settings.breite/6))

            #screen.blit(spielerBildGros, (settings.breite * (1 / 10), settings.hoehe * (2 / 10)))
            #screen.blit(bildVonBombeGros, (settings.breite * (3 / 10), settings.hoehe * (2 / 10)))
            #screen.blit(bildVonLaserGros, (settings.breite * (5 / 10), settings.hoehe * (2 / 10)))
            #screen.blit(bildVonShotgunGros, (settings.breite * (7 / 10), settings.hoehe * (2 / 10)))

            textLeben = renderText("Health Lv " + str(currentPlayerStat.healthLevel),int(settings.hoehe / 12), 200)
            textSpeed = renderText("Speed Lv " + str(currentPlayerStat.speedLevel),int(settings.hoehe / 12), 200)
            textWaffen = renderText("Weapons Lv " + str(currentPlayerStat.waffenLevel),int(settings.hoehe / 12), 200)

            textCost1 = renderText(str(currentPlayerStat.healthLevelCost[currentPlayerStat.healthLevel]),int(settings.hoehe / 12), 200)
            textCost2 = renderText(str(currentPlayerStat.speedLevelCost[currentPlayerStat.speedLevel]),int(settings.hoehe / 12), 200)
            textCost3 = renderText(str(currentPlayerStat.waffenLevelCost[currentPlayerStat.waffenLevel]),int(settings.hoehe / 12), 200)

            textFunktion1 = renderText(str(currentPlayerStat.healthLevelArray[currentPlayerStat.healthLevel]) + " live -> " +
                                       str(currentPlayerStat.healthLevelArray[currentPlayerStat.healthLevel+1]) + " live",int(settings.hoehe / 15), 200)
            textFunktion2 = renderText(str(currentPlayerStat.speedLevelArray[currentPlayerStat.speedLevel]) + " m/s -> " +
                                       str(currentPlayerStat.speedLevelArray[currentPlayerStat.speedLevel+1]) + " m/s" ,int(settings.hoehe / 15), 200)
            textFunktion3 = renderText(str(currentPlayerStat.waffenLevelArray[currentPlayerStat.waffenLevel]) + "x -> " +
                                       str(currentPlayerStat.waffenLevelArray[currentPlayerStat.waffenLevel+1]) + "x" ,int(settings.hoehe / 15), 200)


            plusBox1 = pygame.Rect(settings.breite * (4 / 20), settings.hoehe * (7 / 10) - 10, 60, 60 )
            plusBox2 = pygame.Rect(settings.breite * (11 / 20), settings.hoehe * (7 / 10) - 10, 60, 60 )
            plusBox3 = pygame.Rect(settings.breite * (18 / 20), settings.hoehe * (7 / 10) - 10, 60, 60 )

            cooldown = True
            cooldownCnt = 0
            quadratposition = 1

            cooldownCnt2 = 0
            cooldown2 = True

            while True:
                # eingabeüberprüfung
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        currentPlayerStat.savePlayerStat()
                        sys.exit()
                pressed2 = pygame.key.get_pressed()
                mousePos2 = pygame.mouse.get_pos()
                # mouseKlick[0] = linksklick, 1 ist laufrad, 2 ist rechte maustaste
                mouseKlick2 = pygame.mouse.get_pressed()



                if cooldownCnt < 15  and not cooldown:
                    cooldownCnt += 1
                else:
                    cooldownCnt = 0
                    cooldown = True

                if cooldownCnt2 < 15  and not cooldown2:
                    cooldownCnt2 += 1
                else:
                    cooldownCnt2 = 0
                    cooldown2 = True

                if pressed2[pygame.K_RIGHT] and cooldown2:
                    cooldown2 = False
                    if quadratposition < 4:
                        quadratposition += 1
                    else:
                        quadratposition = 1
                if pressed2[pygame.K_LEFT] and cooldown2:
                    cooldown2 = False
                    if quadratposition > 1:
                        quadratposition -= 1
                    else:
                        quadratposition = 4


                # hintergrund und münzen zeichnen
                screen.blit(hintergrundBild, (0, 0))
                screen.blit(textMünzen, (settings.breite * (3 / 10), settings.hoehe / 10))
                screen.blit(textMünzenAnzahl, (settings.breite * (6 / 10), settings.hoehe / 10))

                textMünzenAnzahl = renderText(str(currentPlayerStat.money), int(settings.hoehe / 12), 200)
                textExitBox = pygame.Rect((5 / 10) * settings.breite - textSize1, (8 / 10) * settings.hoehe,
                                          2 * textSize1, textSize1)
                if not textExitBox.collidepoint(mousePos2):
                    screen.blit(textExit, textExitBox)
                if textExitBox.collidepoint(mousePos2) or pressed2[pygame.K_BACKSPACE]:
                    textExitgroß = pygame.transform.scale(textExit, (2 * textSize1 + 40, textSize1 + 20))
                    screen.blit(textExitgroß,
                                ((5 / 10) * settings.breite - textSize1 - 20, (8 / 10) * settings.hoehe - 10))
                    if mouseKlick2[0] or pressed2[pygame.K_BACKSPACE]: break

                screen.blit(spielerBildGros, (settings.breite * (1/10)+30, settings.hoehe * (2/10)))
                screen.blit(bildVonBombeGros, (settings.breite * (3/10)+30, settings.hoehe * (2/10)))
                screen.blit(bildVonLaserGros, (settings.breite * (5/10)+30, settings.hoehe * (2/10)))
                screen.blit(bildVonShotgunGros, (settings.breite * (7/10)+30, settings.hoehe * (2/10)))

                pygame.draw.line(screen, (140, 140, 140), (0, settings.hoehe * (2/10)-30), (settings.breite, settings.hoehe * (2/10)-30), 7)
                pygame.draw.line(screen, (140, 140, 140), (0, settings.hoehe * (2/10)+int(settings.breite/8)+30), (settings.breite, settings.hoehe * (2/10)+int(settings.breite/8)+30), 7)








                if hitboxPlayer.collidepoint(mousePos2) and mouseKlick2[0] or quadratposition == 1:
                    quadratposition = 1

                    textLeben = renderText("Health Lv " + str(currentPlayerStat.healthLevel),int(settings.hoehe / 12), 200)
                    textSpeed = renderText("Speed Lv " + str(currentPlayerStat.speedLevel), int(settings.hoehe / 12), 200)
                    textWaffen = renderText("Weapons Lv " + str(currentPlayerStat.waffenLevel), int(settings.hoehe / 12),200)

                    textCost1 = renderText(str(currentPlayerStat.healthLevelCost[currentPlayerStat.healthLevel]),int(settings.hoehe / 12), 200)
                    textCost2 = renderText(str(currentPlayerStat.speedLevelCost[currentPlayerStat.speedLevel]),int(settings.hoehe / 12), 200)
                    textCost3 = renderText(str(currentPlayerStat.waffenLevelCost[currentPlayerStat.waffenLevel]),int(settings.hoehe / 12), 200)

                    textFunktion1 = renderText(
                        str(currentPlayerStat.healthLevelArray[currentPlayerStat.healthLevel]) + " live -> " +
                        str(currentPlayerStat.healthLevelArray[currentPlayerStat.healthLevel + 1]) + " live",
                        int(settings.hoehe / 15), 200)
                    textFunktion2 = renderText(
                        str(currentPlayerStat.speedLevelArray[currentPlayerStat.speedLevel]) + " m/s -> " +
                        str(currentPlayerStat.speedLevelArray[currentPlayerStat.speedLevel + 1]) + " m/s",
                        int(settings.hoehe / 15), 200)
                    textFunktion3 = renderText(
                        str(currentPlayerStat.waffenLevelArray[currentPlayerStat.waffenLevel]) + "x -> " +
                        str(currentPlayerStat.waffenLevelArray[currentPlayerStat.waffenLevel + 1]) + "x",
                        int(settings.hoehe / 15), 200)

                if hitboxBombe.collidepoint(mousePos2) and mouseKlick2[0] or quadratposition == 2:
                    quadratposition = 2
                    textSchaden = renderText("Damage Lv " + str(currentPlayerStat.bombDmgLevel),int(settings.hoehe / 12), 200)
                    textSize = renderText("Size Lv " + str(currentPlayerStat.bombSizeLevel),int(settings.hoehe / 12), 200)
                    textReloadtime = renderText("Reload Lv " + str(currentPlayerStat.bombReloadLevel),int(settings.hoehe / 12), 200)

                    textCost1 = renderText(str(currentPlayerStat.bombDmgLevelCost[currentPlayerStat.bombDmgLevel]),int(settings.hoehe / 12), 200)
                    textCost2 = renderText(str(currentPlayerStat.bombSizeLevelCost[currentPlayerStat.bombSizeLevel]),int(settings.hoehe / 12), 200)
                    textCost3 = renderText(str(currentPlayerStat.bombReloadLevelCost[currentPlayerStat.bombReloadLevel]),int(settings.hoehe / 12), 200)

                    textFunktion1 = renderText(
                        str(currentPlayerStat.bombSchadenLevelArray[currentPlayerStat.bombDmgLevel]) + " dmg -> " +
                        str(currentPlayerStat.bombSchadenLevelArray[currentPlayerStat.bombDmgLevel + 1]) + " dmg",
                        int(settings.hoehe / 15), 200)
                    textFunktion2 = renderText(
                        str(currentPlayerStat.bombSizeLevelArray[currentPlayerStat.bombSizeLevel]) + " m -> " +
                        str(currentPlayerStat.bombSizeLevelArray[currentPlayerStat.bombSizeLevel + 1]) + " m",
                        int(settings.hoehe / 15), 200)
                    textFunktion3 = renderText(
                        str(round(currentPlayerStat.bombReloadSpeedLevelArray[currentPlayerStat.bombReloadLevel] / 60,2)) + "s -> " +
                        str(round(currentPlayerStat.bombReloadSpeedLevelArray[currentPlayerStat.bombReloadLevel + 1] / 60,2)) + "s",
                        int(settings.hoehe / 15), 200)

                if hitboxLaser.collidepoint(mousePos2) and mouseKlick2[0] or quadratposition == 3:
                    quadratposition = 3
                    textSchaden = renderText("Damage Lv " + str(currentPlayerStat.laserDmgLevel),int(settings.hoehe / 12), 200)
                    textSpeed = renderText("Speed Lv " + str(currentPlayerStat.laserSpeedLevel), int(settings.hoehe / 12), 200)
                    textReloadtime = renderText("Reload Lv " + str(currentPlayerStat.laserReloadLevel),int(settings.hoehe / 12), 200)

                    textCost1 = renderText(str(currentPlayerStat.laserDmgLevelCost[currentPlayerStat.laserDmgLevel]),int(settings.hoehe / 12), 200)
                    textCost2 = renderText(str(currentPlayerStat.laserSpeedLevelCost[currentPlayerStat.laserSpeedLevel]),int(settings.hoehe / 12), 200)
                    textCost3 = renderText(str(currentPlayerStat.laserReloadLevelCost[currentPlayerStat.laserReloadLevel]),int(settings.hoehe / 12), 200)

                    textFunktion1 = renderText(
                        str(currentPlayerStat.laserSchadenLevelArray[currentPlayerStat.laserDmgLevel]) + " dmg -> " +
                        str(currentPlayerStat.laserSchadenLevelArray[currentPlayerStat.laserDmgLevel + 1]) + " dmg",
                        int(settings.hoehe / 15), 200)
                    textFunktion2 = renderText(
                        str(currentPlayerStat.laserSpeedLevelArray[currentPlayerStat.laserSpeedLevel]) + " m/s -> " +
                        str(currentPlayerStat.laserSpeedLevelArray[currentPlayerStat.laserSpeedLevel + 1]) + " m/s",
                        int(settings.hoehe / 15), 200)
                    textFunktion3 = renderText(
                        str(round(currentPlayerStat.laserReloadSpeedLevelArray[currentPlayerStat.laserReloadLevel] / 60,2)) + "s -> " +
                        str(round(currentPlayerStat.laserReloadSpeedLevelArray[currentPlayerStat.laserReloadLevel + 1] / 60,2)) + "s",
                        int(settings.hoehe / 15), 200)


                if hitboxShotgun.collidepoint(mousePos2) and mouseKlick2[0] or quadratposition == 4:
                    quadratposition = 4
                    textSchaden = renderText("Damage Lv " + str(currentPlayerStat.shotgunDmgLevel),int(settings.hoehe / 12), 200)
                    textBullet = renderText("Bullet Lv " + str(currentPlayerStat.shotgunBulletLevel), int(settings.hoehe / 12), 200)
                    textReloadtime = renderText("Reload Lv " + str(currentPlayerStat.shotgunReloadLevel),int(settings.hoehe / 12), 200)

                    textCost1 = renderText(str(currentPlayerStat.shotgunDmgLevelCost[currentPlayerStat.shotgunDmgLevel]),int(settings.hoehe / 12), 200)
                    textCost2 = renderText(str(currentPlayerStat.shotgunBulletLevelCost[currentPlayerStat.shotgunBulletLevel]),int(settings.hoehe / 12), 200)
                    textCost3 = renderText(str(currentPlayerStat.shotgunReloadLevelCost[currentPlayerStat.shotgunReloadLevel]),int(settings.hoehe / 12), 200)

                    textFunktion1 = renderText(
                        str(currentPlayerStat.shotgunSchadenLevelArray[currentPlayerStat.shotgunDmgLevel]) + " dmg -> " +
                        str(currentPlayerStat.shotgunSchadenLevelArray[currentPlayerStat.shotgunDmgLevel + 1]) + " dmg",
                        int(settings.hoehe / 15), 200)
                    textFunktion2 = renderText(
                        str(currentPlayerStat.shotgunShrotLevelArray[currentPlayerStat.shotgunBulletLevel]) + " bullets -> " +
                        str(currentPlayerStat.shotgunShrotLevelArray[currentPlayerStat.shotgunBulletLevel + 1]) + " bullets",
                        int(settings.hoehe / 15), 200)
                    textFunktion3 = renderText(
                        str(round(currentPlayerStat.shotgunReloadTimeLevelArray[currentPlayerStat.shotgunReloadLevel] / 60,2)) + "s -> " +
                        str(round(currentPlayerStat.shotgunReloadTimeLevelArray[currentPlayerStat.shotgunReloadLevel + 1] / 60,2)) + "s",
                        int(settings.hoehe / 15), 200)

#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif
                if quadratposition == 1:
                    zeichneQuadrat(settings.breite * (1/10)+30, settings.hoehe * (2/10),200,7)
                    zeichneUpgrades(upgradeLeben, upgradeSpeed, upgradeWaffen, textCost1, textCost2, textCost3, textFunktion1, textFunktion2, textFunktion3)

                    screen.blit(textLeben, (settings.breite / 6 - int(settings.breite / 10), settings.hoehe * 6 / 10+20))
                    screen.blit(textSpeed, (settings.breite *5 / 12 - 10, settings.hoehe * 6 / 10 +20))
                    screen.blit(textWaffen, (settings.breite *8 / 11 , settings.hoehe * 6 / 10+20))

                    if ((plusBox1.collidepoint(mousePos2) and mouseKlick2[0]) or pressed2[pygame.K_1]) and cooldown:
                        cooldown = False
                        currentPlayerStat.upgradeHealth(gekauftSound)
                        #werte aktuallisieren
                        textLeben = renderText("Health Lv " + str(currentPlayerStat.healthLevel),int(settings.hoehe / 12), 200)
                        textCost1 = renderText(str(currentPlayerStat.healthLevelCost[currentPlayerStat.healthLevel]),int(settings.hoehe / 12), 200)
                        textFunktion1 = renderText(
                            str(currentPlayerStat.healthLevelArray[currentPlayerStat.healthLevel]) + " live -> " +
                            str(currentPlayerStat.healthLevelArray[currentPlayerStat.healthLevel + 1]) + " live",
                            int(settings.hoehe / 15), 200)

                    if ((plusBox2.collidepoint(mousePos2) and mouseKlick2[0]) or pressed2[pygame.K_2]) and cooldown:
                        cooldown = False
                        currentPlayerStat.upgradePlayerSpeed(gekauftSound)
                        #werte aktuallisieren
                        textSpeed = renderText("Speed Lv " + str(currentPlayerStat.speedLevel), int(settings.hoehe / 12), 200)
                        textCost2 = renderText(str(currentPlayerStat.speedLevelCost[currentPlayerStat.speedLevel]),int(settings.hoehe / 12), 200)
                        textFunktion2 = renderText(
                            str(currentPlayerStat.speedLevelArray[currentPlayerStat.speedLevel]) + " m/s -> " +
                            str(currentPlayerStat.speedLevelArray[currentPlayerStat.speedLevel + 1]) + " m/s",
                            int(settings.hoehe / 15), 200)

                    if ((plusBox3.collidepoint(mousePos2) and mouseKlick2[0]) or pressed2[pygame.K_3]) and cooldown:
                        cooldown = False
                        currentPlayerStat.upgradeWaffen(gekauftSound)
                        #werte aktuallisieren
                        textWaffen = renderText("Weapons Lv " + str(currentPlayerStat.waffenLevel), int(settings.hoehe / 12),200)
                        textCost3 = renderText(str(currentPlayerStat.waffenLevelCost[currentPlayerStat.waffenLevel]),int(settings.hoehe / 12), 200)
                        textFunktion3 = renderText(
                            str(currentPlayerStat.waffenLevelArray[currentPlayerStat.waffenLevel]) + "x -> " +
                            str(currentPlayerStat.waffenLevelArray[currentPlayerStat.waffenLevel + 1]) + "x",
                            int(settings.hoehe / 15), 200)
#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif#schif


#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe
                elif quadratposition == 2:
                    zeichneQuadrat(settings.breite * (3/10)+30, settings.hoehe * (2/10),200,7)
                    zeichneUpgrades(upgradeSchaden, upgradeGroese, upgradeNachladen, textCost1, textCost2, textCost3, textFunktion1, textFunktion2, textFunktion3)

                    screen.blit(textSchaden, (settings.breite / 6 - int(settings.breite / 10), settings.hoehe * 6 / 10+20))
                    screen.blit(textSize, (settings.breite *5 / 12 +10, settings.hoehe * 6 / 10 +20))
                    screen.blit(textReloadtime, (settings.breite *8 / 11 +10 , settings.hoehe * 6 / 10+20))

                    if ((plusBox1.collidepoint(mousePos2) and mouseKlick2[0]) or pressed2[pygame.K_1]) and cooldown:
                        cooldown = False
                        currentPlayerStat.upgradeBombDmg(gekauftSound)
                        #werte aktuallisieren
                        textSchaden = renderText("Damage Lv " + str(currentPlayerStat.bombDmgLevel),int(settings.hoehe / 12), 200)
                        textCost1 = renderText(str(currentPlayerStat.bombDmgLevelCost[currentPlayerStat.bombDmgLevel]),int(settings.hoehe / 12), 200)
                        textFunktion1 = renderText(
                            str(currentPlayerStat.bombSchadenLevelArray[currentPlayerStat.bombDmgLevel]) + " dmg -> " +
                            str(currentPlayerStat.bombSchadenLevelArray[currentPlayerStat.bombDmgLevel + 1]) + " dmg",
                            int(settings.hoehe / 15), 200)

                    if ((plusBox2.collidepoint(mousePos2) and mouseKlick2[0]) or pressed2[pygame.K_2]) and cooldown:
                        cooldown = False
                        currentPlayerStat.upgradeBombSize(gekauftSound)
                        #werte aktuallisieren
                        textSize = renderText("Size Lv " + str(currentPlayerStat.bombSizeLevel),int(settings.hoehe / 12), 200)
                        textCost2 = renderText(str(currentPlayerStat.bombSizeLevelCost[currentPlayerStat.bombSizeLevel]),int(settings.hoehe / 12), 200)
                        textFunktion2 = renderText(
                            str(currentPlayerStat.bombSizeLevelArray[currentPlayerStat.bombSizeLevel]) + " m -> " +
                            str(currentPlayerStat.bombSizeLevelArray[currentPlayerStat.bombSizeLevel + 1]) + " m",
                            int(settings.hoehe / 15), 200)

                    if ((plusBox3.collidepoint(mousePos2) and mouseKlick2[0]) or pressed2[pygame.K_3]) and cooldown:
                        cooldown = False
                        currentPlayerStat.upgradeBombReload(gekauftSound)
                        #werte aktuallisieren
                        textReloadtime = renderText("Reload Lv " + str(currentPlayerStat.bombReloadLevel),int(settings.hoehe / 12), 200)
                        textCost3 = renderText(str(currentPlayerStat.bombReloadLevelCost[currentPlayerStat.bombReloadLevel]),int(settings.hoehe / 12), 200)
                        textFunktion3 = renderText(
                            str(round(currentPlayerStat.bombReloadSpeedLevelArray[currentPlayerStat.bombReloadLevel] /60, 2 )) + "s -> " +
                            str(round(currentPlayerStat.bombReloadSpeedLevelArray[currentPlayerStat.bombReloadLevel + 1] / 60, 2 )) + "s",
                            int(settings.hoehe / 15), 200)
#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe#bombe

#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser
                elif quadratposition == 3:
                    zeichneQuadrat(settings.breite * (5/10)+30, settings.hoehe * (2/10),200,7)
                    zeichneUpgrades(upgradeSchaden, upgradeSpeed, upgradeNachladen, textCost1, textCost2, textCost3, textFunktion1, textFunktion2, textFunktion3)

                    screen.blit(textSchaden, (settings.breite / 6 - int(settings.breite / 10), settings.hoehe * 6 / 10+20))
                    screen.blit(textSpeed, (settings.breite *5 / 12 - 10, settings.hoehe * 6 / 10 +20))
                    screen.blit(textReloadtime, (settings.breite *8 / 11 +10 , settings.hoehe * 6 / 10+20))

                    if ((plusBox1.collidepoint(mousePos2) and mouseKlick2[0]) or pressed2[pygame.K_1]) and cooldown:
                        cooldown = False
                        currentPlayerStat.upgradeLaserDmg(gekauftSound)
                        #werte aktuallisieren
                        textSchaden = renderText("Damage Lv " + str(currentPlayerStat.laserDmgLevel),int(settings.hoehe / 12), 200)
                        textCost1 = renderText(str(currentPlayerStat.laserDmgLevelCost[currentPlayerStat.laserDmgLevel]),int(settings.hoehe / 12), 200)
                        textFunktion1 = renderText(
                            str(currentPlayerStat.laserSchadenLevelArray[currentPlayerStat.laserDmgLevel]) + " dmg -> " +
                            str(currentPlayerStat.laserSchadenLevelArray[currentPlayerStat.laserDmgLevel + 1]) + " dmg",
                            int(settings.hoehe / 15), 200)

                    if ((plusBox2.collidepoint(mousePos2) and mouseKlick2[0]) or pressed2[pygame.K_2]) and cooldown:
                        cooldown = False
                        currentPlayerStat.upgradeLaserSpeed(gekauftSound)
                        #werte aktuallisieren
                        textSpeed = renderText("Speed Lv " + str(currentPlayerStat.laserSpeedLevel), int(settings.hoehe / 12), 200)
                        textCost2 = renderText(str(currentPlayerStat.laserSpeedLevelCost[currentPlayerStat.laserSpeedLevel]),int(settings.hoehe / 12), 200)
                        textFunktion2 = renderText(
                            str(currentPlayerStat.laserSpeedLevelArray[currentPlayerStat.laserSpeedLevel]) + " m/s -> " +
                            str(currentPlayerStat.laserSpeedLevelArray[currentPlayerStat.laserSpeedLevel + 1]) + " m/s",
                            int(settings.hoehe / 15), 200)

                    if ((plusBox3.collidepoint(mousePos2) and mouseKlick2[0]) or pressed2[pygame.K_3]) and cooldown:
                        cooldown = False
                        currentPlayerStat.upgradeLaserReload(gekauftSound)
                        #werte aktuallisieren
                        textReloadtime = renderText("Reload Lv " + str(currentPlayerStat.laserReloadLevel),int(settings.hoehe / 12), 200)
                        textCost3 = renderText(str(currentPlayerStat.laserReloadLevelCost[currentPlayerStat.laserReloadLevel]),int(settings.hoehe / 12), 200)
                        textFunktion3 = renderText(
                            str(round(currentPlayerStat.laserReloadSpeedLevelArray[
                                    currentPlayerStat.laserReloadLevel] /60, 2 )) + "s -> " +
                            str(round(currentPlayerStat.laserReloadSpeedLevelArray[
                                    currentPlayerStat.laserReloadLevel + 1] /60, 2 )) + "s",
                            int(settings.hoehe / 15), 200)
#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser#laser

#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun
                elif quadratposition == 4:
                    zeichneQuadrat(settings.breite * (7/10)+30, settings.hoehe * (2/10),200,7)
                    zeichneUpgrades(upgradeSchaden, upgradeSchrot, upgradeNachladen, textCost1, textCost2, textCost3, textFunktion1, textFunktion2, textFunktion3, 60)

                    screen.blit(textSchaden, (settings.breite / 6 - int(settings.breite / 10), settings.hoehe * 6 / 10+20))
                    screen.blit(textBullet, (settings.breite *5 / 12 - 10, settings.hoehe * 6 / 10 +20))
                    screen.blit(textReloadtime, (settings.breite *8 / 11 +10 , settings.hoehe * 6 / 10+20))

                    if ((plusBox1.collidepoint(mousePos2) and mouseKlick2[0]) or pressed2[pygame.K_1]) and cooldown:
                        cooldown = False
                        currentPlayerStat.upgradeShotgunDmg(gekauftSound)
                        #werte aktuallisieren
                        textSchaden = renderText("Damage Lv " + str(currentPlayerStat.shotgunDmgLevel),int(settings.hoehe / 12), 200)
                        textCost1 = renderText(str(currentPlayerStat.shotgunDmgLevelCost[currentPlayerStat.shotgunDmgLevel]),int(settings.hoehe / 12), 200)

                        textFunktion1 = renderText(
                            str(currentPlayerStat.shotgunSchadenLevelArray[currentPlayerStat.shotgunDmgLevel]) + " dmg -> " +
                            str(currentPlayerStat.shotgunSchadenLevelArray[currentPlayerStat.shotgunDmgLevel + 1]) + " dmg",
                            int(settings.hoehe / 15), 200)


                    if ((plusBox2.collidepoint(mousePos2) and mouseKlick2[0]) or pressed2[pygame.K_2]) and cooldown:
                        cooldown = False
                        currentPlayerStat.upgradeShotgunBullet(gekauftSound)
                        #werte aktuallisieren
                        textBullet = renderText("Bullet Lv " + str(currentPlayerStat.shotgunBulletLevel), int(settings.hoehe / 12), 200)
                        textCost2 = renderText(str(currentPlayerStat.shotgunBulletLevelCost[currentPlayerStat.shotgunBulletLevel]),int(settings.hoehe / 12), 200)
                        textFunktion2 = renderText(
                            str(currentPlayerStat.shotgunShrotLevelArray[currentPlayerStat.shotgunBulletLevel]) + " bullets -> " +
                            str(currentPlayerStat.shotgunShrotLevelArray[currentPlayerStat.shotgunBulletLevel + 1]) + " bullets",
                            int(settings.hoehe / 15), 200)

                    if ((plusBox3.collidepoint(mousePos2) and mouseKlick2[0]) or pressed2[pygame.K_3]) and cooldown:
                        cooldown = False
                        currentPlayerStat.upgradeShotgunReload(gekauftSound)
                        #werte aktuallisieren
                        textReloadtime = renderText("Reload Lv " + str(currentPlayerStat.shotgunReloadLevel),int(settings.hoehe / 12), 200)
                        textCost3 = renderText(str(currentPlayerStat.shotgunReloadLevelCost[currentPlayerStat.shotgunReloadLevel]),int(settings.hoehe / 12), 200)
                        textFunktion3 = renderText(
                            str(round(currentPlayerStat.shotgunReloadTimeLevelArray[
                                    currentPlayerStat.shotgunReloadLevel] /60, 2 )) + "s -> " +
                            str(round(currentPlayerStat.shotgunReloadTimeLevelArray[
                                    currentPlayerStat.shotgunReloadLevel + 1] /60, 2 )) + "s",
                            int(settings.hoehe / 15), 200)
#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun#shotgun




                pygame.display.update()

    else:
        screen.blit(textUpgrades, textUpgradesBox)

    # xp balken und level  aktualisieren
    levelBalkenInnen = pygame.Rect(settings.breite / 3 + 3, settings.hoehe / 20 + 3,
                                   ((int(currentPlayerStat.xp) / 100) * (settings.breite / 2)) - 6,
                                   settings.hoehe / 20 - 6)
    textLevelNr = renderText(str(currentPlayerStat.questlevel), int(settings.hoehe / 12), 200)

    # anzeige für level
    screen.blit(textLevelNr, (settings.breite / 4, settings.hoehe / 20))
    screen.blit(textLevelLevel, (settings.breite / 10, settings.hoehe / 20))
    # anzeige für levelbalken
    pygame.draw.rect(screen, (255, 255, 255), levelBalkenBasis, 0)
    pygame.draw.rect(screen, (255, 0, 255), levelBalkenInnen, 0)

    pygame.display.update()
    return [True, False, False]


def renderText(text, size, rot=255, grün=255, blau=255):
    sys_font = pygame.font.SysFont("none", size)
    rendered = sys_font.render(text, 0, (rot, grün, blau))
    return rendered

def zeichneQuadrat(startX,startY, size, dicke):
    pygame.draw.line(screen,(0,140,140),(startX, startY),(startX,startY+size), dicke)
    pygame.draw.line(screen, (0, 140, 140), (startX, startY), (startX + size, startY), dicke)
    pygame.draw.line(screen, (0, 140, 140), (startX+size, startY), (startX+size, startY + size), dicke)
    pygame.draw.line(screen, (0, 140, 140), (startX, startY+size), (startX+size, startY + size), dicke)

def zeichneUpgrades(bild1, bild2, bild3, textCost1, textCost2, textCost3, textFunktion1,textFunktion2,textFunktion3,delta = 0):
    screen.blit(bild1, (settings.breite / 6 - int(settings.breite / 24), settings.hoehe * 5 / 10 -30))
    screen.blit(bild2, (settings.breite *2/ 4 - int(settings.breite / 24), settings.hoehe * 5 / 10-30))
    screen.blit(bild3, (settings.breite *5/ 6 - int(settings.breite / 24), settings.hoehe * 5 / 10-30))

    screen.blit(munze, (settings.breite * (3 / 20), settings.hoehe * (7 / 10)))
    screen.blit(munze, (settings.breite * (10 / 20), settings.hoehe * (7 / 10)))
    screen.blit(munze, (settings.breite * (17 / 20), settings.hoehe * (7 / 10)))

    screen.blit(plus, (settings.breite * (4 / 20), settings.hoehe * (7 / 10) - 10))
    screen.blit(plus, (settings.breite * (11 / 20), settings.hoehe * (7 / 10) - 10))
    screen.blit(plus, (settings.breite * (18 / 20), settings.hoehe * (7 / 10) - 10))

    screen.blit(textCost1, (settings.breite * (0 / 20)+10, settings.hoehe * (7 / 10) - 10))
    screen.blit(textCost2, (settings.breite * (7 / 20)+10, settings.hoehe * (7 / 10) - 10))
    screen.blit(textCost3, (settings.breite * (14 / 20)+10, settings.hoehe * (7 / 10) - 10))

    screen.blit(textFunktion1, (settings.breite * (1 / 20), settings.hoehe * (8 / 10) - 10))
    screen.blit(textFunktion2, (settings.breite * (8 / 20) - delta, settings.hoehe * (8 / 10) - 10))
    screen.blit(textFunktion3, (settings.breite * (15 / 20), settings.hoehe * (8 / 10) - 10))




if __name__ == "__main__":

    # system
    settings = clasSystem.System()
    clock = pygame.time.Clock()
    animation = classAnimation.animation()

    # player
    currentPlayerStat = classPlayerStat.playerStat()
    player = classPlayer.player(currentPlayerStat)


    # enemy
    gegnerSpeed = 2
    gegnerSpeedDown = 60
    gegner0Size = 60
    gegner1Size = 60
    gegner2Size = 80
    gegnerRichtungRight = True

    # weapons
    laserSize = 20
    enableLaser = True
    enableBombe = True
    enableShotgun = True

    # game
    frameCountLaser = 0
    frameCountBombe = 0
    frameCountShotgun = 0












    levelModeActive = False
    endlesModeActive = False
    menu = True






























    pygame.init()
    screen = pygame.display.set_mode([settings.breite, settings.hoehe], pygame.RESIZABLE)
    pygame.display.set_caption("Space Invaders")

    # define Images
    hintergrundBild = pygame.image.load("bilder/hintergrund.jpg")
    iconBild = pygame.image.load("bilder/Schiff.PNG")
    # enemy
    gegnerBild1 = pygame.image.load("bilder/alien/alien8.png")
    gegnerBild2 = pygame.image.load("bilder/alien/alien7.png")
    gegnerBild3 = pygame.image.load("bilder/alien/alien6.png")
    sonntagImage = pygame.image.load("bilder/alien/sonntag2.png")
    melzerBild = pygame.image.load("bilder/alien/melzer.png")
    mithut = pygame.image.load("bilder/alien/sonntag4.png")
    marker = pygame.image.load("bilder/marker.png")




    # player
    spielerBild = pygame.image.load("bilder/alien/alien.png")

    #pausemenü
    zahnrad = pygame.image.load("bilder/settings.png")



    # wappons
    bildVonLaser = pygame.image.load("laser.png")
    bildVonBombe = pygame.image.load("bombe.png")
    bildVonShotgun = pygame.image.load("shotgun.png")
    #upgrades
    upgradeLeben = pygame.image.load("bilder/upgrades/herz.png")
    upgradeSpeed = pygame.image.load("bilder/upgrades/geschwindigkeit.png")
    upgradeWaffen = pygame.image.load("bilder/upgrades/geschwindigkeit.png")
    upgradeSchaden = pygame.image.load("bilder/upgrades/schaden.png")
    upgradeGroese = pygame.image.load("bilder/upgrades/grose.png")
    upgradeNachladen = pygame.image.load("bilder/upgrades/zukunft.png")
    upgradeSchrot = pygame.image.load("bilder/upgrades/kugeln.png")
    munze = pygame.image.load("bilder/upgrades/munze.png")
    plus = pygame.image.load("bilder/upgrades/plus.png")



    #bild von waffenanimation
    #laserBild = pygame.image.load("bilder/explosion/explosion_blue.png")
    laserBild = pygame.image.load("bilder/explosion/explosion_blue_purple.png")
    feuerBild = pygame.image.load("bilder/explosion/fire1.png")
    shotgunBild = pygame.image.load("bilder/explosion/explosion_white.png")
    # text
    textSettings = pygame.image.load("bilder/text/settings.png")
    textBomb = pygame.image.load("bilder/text/bomb.png")
    textLaser = pygame.image.load("bilder/text/laser.png")
    textEndless = pygame.image.load("bilder/text/endless.png")
    textLevel = pygame.image.load("bilder/text/level.png")
    textShip = pygame.image.load("bilder/text/ship.png")
    textShotgun = pygame.image.load("bilder/text/shotgun.png")
    textUpgrades = pygame.image.load("bilder/text/upgrades.png")
    textExit = pygame.image.load("bilder/text/exit.png")
    textMusicVolume = pygame.image.load("bilder/text/musicvolume.png")
    textEffectVolume = pygame.image.load("bilder/text/effectvolume.png")
    textResetPlayer = pygame.image.load("bilder/text/resetplayer.png")
    textBack = pygame.image.load("bilder/text/back.png")

    textTryAgain = pygame.image.load("bilder/text/tryAgain.png")
    textNextLevel = pygame.image.load("bilder/text/nextLevel.png")
    textMissionFailed = pygame.image.load("bilder/text/mussionFailed.png")
    textLevelComplete = pygame.image.load("bilder/text/levelComplete.png")
    textMenu = pygame.image.load("bilder/text/menu.png")



    # scale Images
    hintergrundBild = pygame.transform.scale(hintergrundBild, (settings.breite, settings.hoehe))
    zahnrad = pygame.transform.scale(zahnrad, (40, 40))

    #upgradebilder
    bildVonLaserGros = pygame.transform.scale(bildVonLaser, (int(settings.breite/8), int(settings.breite/8)))
    bildVonBombeGros = pygame.transform.scale(bildVonBombe, (int(settings.breite/8), int(settings.breite/8)))
    bildVonShotgunGros = pygame.transform.scale(bildVonShotgun, (int(settings.breite/8), int(settings.breite/8)))
    spielerBildGros = pygame.transform.scale(spielerBild, (int(settings.breite/8), int(settings.breite/8)))
    #upgrades
    upgradeLeben = pygame.transform.scale(upgradeLeben, (int(settings.breite / 12), int(settings.breite / 12)))
    upgradeSpeed = pygame.transform.scale(upgradeSpeed, (int(settings.breite / 12), int(settings.breite / 12)))
    upgradeWaffen = pygame.transform.scale(upgradeWaffen, (int(settings.breite / 12), int(settings.breite / 12)))
    upgradeSchaden = pygame.transform.scale(upgradeSchaden, (int(settings.breite / 15), int(settings.breite / 15)))
    upgradeGroese = pygame.transform.scale(upgradeGroese, (int(settings.breite / 15), int(settings.breite / 15)))
    upgradeNachladen = pygame.transform.scale(upgradeNachladen, (int(settings.breite / 15), int(settings.breite / 15)))
    upgradeSchrot = pygame.transform.scale(upgradeSchrot, (int(settings.breite / 15), int(settings.breite / 15)))
    munze = pygame.transform.scale(munze, (40, 40))
    plus = pygame.transform.scale(plus, (60, 60))
    #wapons in game
    bildVonLaser = pygame.transform.scale(bildVonLaser, (53, 53))
    bildVonBombe = pygame.transform.scale(bildVonBombe, (53, 53))
    bildVonShotgun = pygame.transform.scale(bildVonShotgun, (57, 57))
    laserBild = pygame.transform.scale(laserBild, (laserSize, laserSize))
    feuerBild = pygame.transform.scale(feuerBild, (200, 200))
    shotgunBild = pygame.transform.scale(shotgunBild, (16,16))



    #marker = pygame.transform.scale(marker, (16,16))



    # player
    spielerBild = pygame.transform.scale(spielerBild, (player.playerSize, player.playerSize))
    # textsizes
    textSize1 = 0.15 * settings.breite
    textSize2 = 0.1 * settings.breite
    textSize1 = int(textSize1)
    textSize2 = int(textSize2)
    # transform to size1
    textSettings = pygame.transform.scale(textSettings, (2 * textSize1, textSize1))
    textEndless = pygame.transform.scale(textEndless, (2 * textSize1, textSize1))
    textLevel = pygame.transform.scale(textLevel, (2 * textSize1, textSize1))
    textUpgrades = pygame.transform.scale(textUpgrades, (2 * textSize1, textSize1))
    textExit = pygame.transform.scale(textExit, (2 * textSize1, textSize1))
    textMusicVolume = pygame.transform.scale(textMusicVolume, (2 * textSize1, textSize1))
    textEffectVolume = pygame.transform.scale(textEffectVolume, (2 * textSize1, textSize1))
    textResetPlayer = pygame.transform.scale(textResetPlayer, (2 * textSize1, textSize1))
    textBack = pygame.transform.scale(textBack, (2 * textSize1, textSize1))


    textTryAgain = pygame.transform.scale(textTryAgain, (2 * textSize1, textSize1))
    textNextLevel = pygame.transform.scale(textNextLevel, (2 * textSize1, textSize1))
    textMissionFailed = pygame.transform.scale(textMissionFailed, (2 * textSize1, textSize1))
    textLevelComplete = pygame.transform.scale(textLevelComplete, (2 * textSize1, textSize1))
    textMenu = pygame.transform.scale(textMenu, (2 * textSize1, textSize1))



    # transform to size2
    textBomb = pygame.transform.scale(textBomb, (2 * textSize2, textSize2))
    textLaser = pygame.transform.scale(textLaser, (2 * textSize2, textSize2))
    textShip = pygame.transform.scale(textShip, (2 * textSize2, textSize2))
    textShotgun = pygame.transform.scale(textShotgun, (2 * textSize2, textSize2))

    # create list of images
    waffenBilder = [laserBild, feuerBild, shotgunBild]
    gegnerBilder = [gegnerBild1, gegnerBild2, gegnerBild3,laserBild,sonntagImage,melzerBild,mithut ]

    #define music
    music = classMusic.music()

    #define sounds
    laser = pygame.mixer.Sound("sound/laser.wav")
    kanone = pygame.mixer.Sound("sound/bombe.wav")
    shotgunSound = pygame.mixer.Sound("sound/shotgun.ogg")
    gekauftSound =  pygame.mixer.Sound("sound/gekauft.ogg")
    schreiben1 = pygame.mixer.Sound("sound/schreiben1.wav")
    schreiben2 = pygame.mixer.Sound("sound/schreiben2.wav")
    schreiben3 = pygame.mixer.Sound("sound/schreiben3.wav")
    hit1 = pygame.mixer.Sound("sound/hit1.wav")
    hit2 = pygame.mixer.Sound("sound/hit2.wav")
    hit3 = pygame.mixer.Sound("sound/hit3.wav")

    # akualisiere volume
    akualisiereVolume()

    schreibSounds = [schreiben1, schreiben2,schreiben3]




    # defineWalls
    leftWall = pygame.Rect(-10, 0, 10, settings.hoehe)
    rightWall = pygame.Rect(settings.breite, 0, 10, settings.hoehe)
    bottomWall = pygame.Rect(0, settings.hoehe, settings.breite, 10)
    # define Icon Oben links
    pygame.display.set_icon(iconBild)

    #textrendering
    textLevelNr = renderText(str(currentPlayerStat.questlevel), int(settings.hoehe / 12), 200)
    textLevelLevel = renderText("Level:", int(settings.hoehe / 12), 200)
    textMünzen = renderText("Münzen:", int(settings.hoehe / 12), 200)
    textMünzenAnzahl = renderText(str(currentPlayerStat.money), int(settings.hoehe / 12), 200)

    levelBalkenBasis = pygame.Rect(settings.breite / 3, settings.hoehe / 20, settings.breite / 2, settings.hoehe / 20)
    levelBalkenInnen = pygame.Rect(settings.breite / 3 + 3, settings.hoehe / 20 + 3,
                                   ((int(currentPlayerStat.xp) / 100) * (settings.breite / 2)) - 6,
                                   settings.hoehe / 20 - 6)


    # make game contents
    levelMaker = classGameLevel.gameLevel(gegnerBilder, settings.breite, settings.hoehe)

    gegnerListe = levelMaker.makeLevel(int(currentPlayerStat.questlevel))





    animationListe = []
    for i in range(0, 3*len(gegnerListe)):
        animationListe.append(classHitanimation.hitanimation(marker))








    laserListe = []
    for i in range(0, 50):
        laserListe = laserListe + [classWaffe.waffe(waffenBilder, 0,currentPlayerStat)]
    kanonenListe = []
    for i in range(0, 3):
        kanonenListe = kanonenListe + [classWaffe.waffe(waffenBilder, 1,currentPlayerStat)]
    shotgun = []
    for i in range(0, currentPlayerStat.shotgunShrotLevelArray[currentPlayerStat.shotgunBulletLevel]):
        shotgun = shotgun + [classWaffe.waffe(waffenBilder, 2,currentPlayerStat)]

    cooldown = classCooldown.Cooldown(kanonenListe,shotgun,player,laserSize,bildVonLaser, bildVonBombe, bildVonShotgun, settings, currentPlayerStat)


    while True:
        #level aktualisieren
        textLevelNr = renderText(str(currentPlayerStat.questlevel), int(settings.hoehe / 12), 200)
        #statCounter = classStatCounter.statCounter(gegnerListe)
        # menü
        while settings.menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    currentPlayerStat.savePlayerStat()
                    sys.exit()
            pressed = pygame.key.get_pressed()
            mousePos = pygame.mouse.get_pos()
            # mouseKlick[0] = linksklick, 1 ist laufrad, 2 ist rechte maustaste
            mouseKlick = pygame.mouse.get_pressed()
            settings.changeMode(printMenu())

        # spiel
        #level erneuern


        if settings.levelModeActive:
            laserListe = []
            for i in range(0, 50):
                laserListe = laserListe + [classWaffe.waffe(waffenBilder, 0, currentPlayerStat)]
            kanonenListe = []
            for i in range(0, 3):
                kanonenListe = kanonenListe + [classWaffe.waffe(waffenBilder, 1, currentPlayerStat)]

            shotgunList = []
            for i in range(0,8):
                shotgun = []
                for i in range(0, currentPlayerStat.shotgunShrotLevelArray[currentPlayerStat.shotgunBulletLevel]):
                    shotgun = shotgun + [classWaffe.waffe(waffenBilder, 2, currentPlayerStat)]
                shotgunList.append(shotgun)

            cooldown = classCooldown.Cooldown(kanonenListe, shotgunList, player, laserSize, bildVonLaser, bildVonBombe, bildVonShotgun, settings, currentPlayerStat)


            player = classPlayer.player(currentPlayerStat)

            gegnerListe = levelMaker.makeLevel(int(currentPlayerStat.questlevel))





            startGame.startLevelMode(currentPlayerStat.questlevel, gegnerListe, screen,hintergrundBild ,music,schreibSounds)





            statCounter = classStatCounter.statCounter(gegnerListe)
            settings.backToGame = False

        while settings.levelModeActive and not settings.backToGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    currentPlayerStat.savePlayerStat()
                    sys.exit()
            mousePos = pygame.mouse.get_pos()
            # mouseKlick[0] = linksklick, 1 ist laufrad, 2 ist rechte maustaste
            mouseKlick = pygame.mouse.get_pressed()

            playerRect = pygame.Rect(player.playerX, player.playerY, player.playerSize, player.playerSize)

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_RIGHT] and not playerRect.colliderect(rightWall):
                player.playerX += player.eigenerSpeed
            if pressed[pygame.K_LEFT] and not playerRect.colliderect(leftWall):
                player.playerX -= player.eigenerSpeed
            if pressed[pygame.K_UP] and cooldown.enableBombe:
                pygame.mixer.Sound.play(kanone)
                cooldown.enableBombe = False
            if pressed[pygame.K_SPACE] and cooldown.enableLaser:
                cooldown.enableLaser = shootLaser()

            if pressed[pygame.K_DOWN] and cooldown.enableShotgun:
                cooldown.enableShotgun = False
                pygame.mixer.Sound.play(shotgunSound)


            cooldown.ceckCooldown(player, currentPlayerStat)
            gegnerRichtungRight = moveGegner()
            zeichnen(statCounter)
            clock.tick(60)


        if settings.endlesModeActive:

            laserListe = []
            for i in range(0, 50):
                laserListe = laserListe + [classWaffe.waffe(waffenBilder, 0, currentPlayerStat)]

            kanonenListe = []
            for i in range(0, 3):
                kanonenListe = kanonenListe + [classWaffe.waffe(waffenBilder, 1, currentPlayerStat)]

            shotgunList = []
            for i in range(0,8):
                shotgun = []
                for i in range(0, currentPlayerStat.shotgunShrotLevelArray[currentPlayerStat.shotgunBulletLevel]):
                    shotgun = shotgun + [classWaffe.waffe(waffenBilder, 2, currentPlayerStat)]
                shotgunList.append(shotgun)






            cooldown = classCooldown.Cooldown(kanonenListe, shotgunList, player, laserSize, bildVonLaser, bildVonBombe,
                                              bildVonShotgun, settings, currentPlayerStat)

            player = classPlayer.player(currentPlayerStat)
            currentLive = 1

            gegnerListe = []
            for i in range(0, 20):

                gegnerBild = pygame.transform.scale(gegnerBilder[0], (100, 100))
                waffenBild = pygame.transform.scale(gegnerBilder[3], (int(100 / 5), int(100 / 5)))
                gegnerListe.append(classGegner.gegner(0,0,0,gegnerBild, waffenBild, 0,1,100,1,1))

                gegnerBild = pygame.transform.scale(gegnerBilder[1], (60, 60))
                waffenBild = pygame.transform.scale(gegnerBilder[3], (int(60 / 5), int(60 / 5)))
                gegnerListe.append(classGegner.gegner(0,0,1,gegnerBild, waffenBild, 0,1,60,1,1))

                gegnerBild = pygame.transform.scale(gegnerBilder[2], (80, 80))
                waffenBild = pygame.transform.scale(gegnerBilder[3], (int(80 / 5), int(80 / 5)))
                gegnerListe.append(classGegner.gegner(0,0,1,gegnerBild, waffenBild, 0,1,80,1,1))
                #posX = 0, posY = 0, gegnerNr = 0, gegnerBild = 0, waffenBild = 0, leben = 1, schaden = 1, size = 1, speed = 4, moveDownSpeed = 50, schussProTausend = 10

            statCounter = classStatCounter.statCounter(gegnerListe)
            speedCnt = 0
            endlessCnt = 120
            cnt = 0
            sec = 0
            msec = 0
            min = 0


            animationListe = []
            for i in range(0, 3 * len(gegnerListe)):
                animationListe.append(classHitanimation.hitanimation(marker))




        while settings.endlesModeActive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    currentPlayerStat.savePlayerStat()
                    sys.exit()

            playerRect = pygame.Rect(player.playerX, player.playerY, player.playerSize, player.playerSize)

            pressed = pygame.key.get_pressed()
            mousePos = pygame.mouse.get_pos()
            # mouseKlick[0] = linksklick, 1 ist laufrad, 2 ist rechte maustaste
            mouseKlick = pygame.mouse.get_pressed()

            if pressed[pygame.K_RIGHT] and not playerRect.colliderect(rightWall):
                player.playerX += player.eigenerSpeed
            if pressed[pygame.K_LEFT] and not playerRect.colliderect(leftWall):
                player.playerX -= player.eigenerSpeed



            if pressed[pygame.K_UP] and cooldown.enableBombe:
                pygame.mixer.Sound.play(kanone)
                cooldown.enableBombe = False
            if pressed[pygame.K_SPACE] and cooldown.enableLaser:
                cooldown.enableLaser = shootLaser()
            if pressed[pygame.K_DOWN] and cooldown.enableShotgun:
                cooldown.enableShotgun = False
                pygame.mixer.Sound.play(shotgunSound)

            cooldown.ceckCooldown(player, currentPlayerStat)

            if cnt < endlessCnt:
                cnt +=1
            else:
                for gegner in gegnerListe:
                    if gegner.live <= 0:
                        gegner.live = currentLive
                        gegner.startLive = currentLive
                        gegner.posX = 200 + (random.random()*(settings.breite-400))
                        gegner.posY = -100
                        gegner.moveDownSpeed = 1 + random.random()
                        currentLive += 0.05
                        gegner.plannedSchaden = currentLive
                        cnt = 0
                        speedCnt += 1
                        break
            if speedCnt == 10:
                speedCnt = 0
                endlessCnt -= 10


            #if msec%10 == 0:
                #for gegner in gegnerListe:
                    #gegner.moveDownSpeed *= 1.10


            msec += 1
            if msec == 60:
                sec += 1
                msec = 0
            if sec == 60:
                sec = 0
                min += 1

            if min > 9 and sec > 9:
                time = renderText(str(min) + ":" + str(sec) + ":" + str(int((msec/60)*100)) , 80, 200)
            elif min < 10 and sec > 9:
                time = renderText("0" + str(min) + ":" + str(sec) + ":" + str(int((msec / 60) * 100)), 80, 200)
            elif min > 9 and sec < 10:
                time = renderText(str(min) + ":" + "0" + str(sec) + ":" + str(int((msec/60)*100)) , 80, 200)
            else:
                time = renderText("0" + str(min) + ":" + "0" + str(sec) + ":" + str(int((msec / 60) * 100)), 80, 200)






            moveEnemyRainmode()
            zeichneRainmode(statCounter)
            clock.tick(60)








