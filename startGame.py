import pygame, sys
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import random

def speak(text):

    tts = gTTS(text = text, lang = "en")
    if os.path.exists(r"C:\Users\David Reski\Desktop\Space-Invader\musik\sprache.mp3"):
        os.remove(r"C:\Users\David Reski\Desktop\Space-Invader\musik\sprache.mp3")
    filename = r"C:\Users\David Reski\Desktop\Space-Invader\musik\sprache.mp3"
    tts.save(filename)
    #pygame.mixer.music.load("musik/sprache.mp3")
    #pygame.mixer.music.play(0, 0, 0)


def startLevelMode(playerQuestLevel, gegnerListe, screen,hintergrundBild, music, schreibSounds):
    gegnerType1 = 0
    gegnerType2 = 0
    gegnerType3 = 0
    gegnerType4 = 0
    bossFound = False

    for gegner in gegnerListe:
        if gegner.gegnerNr == 0:
            gegnerType1 +=1
        if gegner.gegnerNr == 1:
            gegnerType2 +=1
        if gegner.gegnerNr == 2:
            gegnerType3 +=1
        if gegner.gegnerNr >= 4:
            bossFound = True
            boss = gegner.name




    ausgabe1 = "Level " + str(playerQuestLevel)
    ausgabe2 = str(gegnerType1) + " Enemy Type 1"
    ausgabe3 = str(gegnerType2) + " Enemy Type 2"
    ausgabe4 = str(gegnerType3) + " Enemy Type 3"
    if not bossFound:
        ausgabe5 = "No Boss this Round"
    else:
        ausgabe5 = "Boss: " + boss

    ausgabeGes = (ausgabe1+ausgabe2+ausgabe3+ausgabe4+ausgabe5)
    size = 60
    stelle = len(ausgabe1)
    zeile = 1
    pos = 0
    coolDownTime = 4
    cooldownCnt = 0
    showText = True
    clock = pygame.time.Clock()
    music.musicPause()
    rand = 0

    while showText:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pressed = pygame.key.get_pressed()

        # mouseKlick[0] = linksklick, 1 ist laufrad, 2 ist rechte maustaste
        mouseKlick = pygame.mouse.get_pressed()
        screen.blit(hintergrundBild, (0, 0))
        if cooldownCnt == coolDownTime:
            cooldownCnt = 0
            pos += 1
            if rand == 2:
                rand = 0
            else:
                rand += 1
            #rand = 3*random.random()

            if rand < 1:
                pygame.mixer.Sound.play(schreibSounds[0])
            elif rand < 2:
                pygame.mixer.Sound.play(schreibSounds[1])
            else:
                pygame.mixer.Sound.play(schreibSounds[2])
        else:
            cooldownCnt += 1

        #speak(ausgabeGes)

        if zeile == 1:
            text1 = renderText(ausgabe1[0:pos+1], size)
            screen.blit(text1, (200, 200))
            if stelle == pos:
                pos = 0
                stelle = len(ausgabe2)
                zeile = 2

        elif zeile == 2:
            text1 = renderText(ausgabe1, 50)
            screen.blit(text1, (200, 200))
            text2 = renderText(ausgabe2[0:pos+1], size)
            screen.blit(text2, (200, 300))
            if stelle == pos:
                pos = 0
                stelle = len(ausgabe3)
                zeile = 3
                #speak(ausgabe2)
        elif zeile == 3:
            text1 = renderText(ausgabe1, 50)
            screen.blit(text1, (200, 200))
            text2 = renderText(ausgabe2, 50)
            screen.blit(text2, (200, 300))
            text3 = renderText(ausgabe3[0:pos+1], size)
            screen.blit(text3, (200, 400))
            if stelle == pos:
                pos = 0
                stelle = len(ausgabe4)
                zeile = 4
                #speak(ausgabe3)
        elif zeile == 4:
            text1 = renderText(ausgabe1, 50)
            screen.blit(text1, (200, 200))
            text2 = renderText(ausgabe2, 50)
            screen.blit(text2, (200, 300))
            text3 = renderText(ausgabe3, 50)
            screen.blit(text3, (200, 400))
            text4 = renderText(ausgabe4[0:pos+1], size)
            screen.blit(text4, (200, 500))
            if stelle == pos:
                pos = 0
                stelle = len(ausgabe5)
                zeile = 5
               # speak(ausgabe4)
        elif zeile == 5:
            text1 = renderText(ausgabe1, 50)
            screen.blit(text1, (200, 200))
            text2 = renderText(ausgabe2, 50)
            screen.blit(text2, (200, 300))
            text3 = renderText(ausgabe3, 50)
            screen.blit(text3, (200, 400))
            text4 = renderText(ausgabe4, size)
            screen.blit(text4, (200, 500))
            text5 = renderText(ausgabe5[0:pos+1], size)
            screen.blit(text5, (200, 600))
            if stelle == pos:
                zeile = 6
                coolDownTime = 1200
                text5 = renderText(ausgabe5, 50)
               # speak(ausgabe5)
        elif zeile == 6:
            screen.blit(text1, (200, 200))
            screen.blit(text2, (200, 300))
            screen.blit(text3, (200, 400))
            screen.blit(text4, (200, 500))
            screen.blit(text5, (200, 600))



        if cooldownCnt == 120:
            music.musicChoise(0)
        elif cooldownCnt == 240:
            showText = False

        if (mouseKlick[0] or pressed[pygame.K_SPACE]) and zeile > 1 :
            music.musicChoise(0)
            showText = False
        pygame.display.update()
        clock.tick(60)




def renderText(text, size, rot=200, grün=200, blau=200):
    sys_font = pygame.font.SysFont("none", size)
    rendered = sys_font.render(text, 0, (rot, grün, blau))
    return rendered
