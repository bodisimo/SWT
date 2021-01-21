import classGegner
import pygame

class gameLevel:
    gegnerBilder = 0
    screenX = 0
    screenY = 0

    def __init__(self, gegnerBilder, screenX, screenY):
        self.gegnerBilder = gegnerBilder
        self.screenX = screenX
        self.screenY = screenY





        #styleguide
        #klasee 0 groß und langsam
            #self.size = 80
            #self.speed = 3
        #klasse 1 klein und langsam
            #self.size = 40
            #self.speed = 3
        #klasse 3 klein und schnell
            #self.size = 40
            #self.speed = 6

    #posY, anzahl, gegnerNr=0, leben = 1, schaden = 1, size = 1, speed = 4, moveDownSpeed = 50, schussProTausend = 10, name = "boss")





    def makeLevel(self, level):

        if level == 1:
            return self.makeGegnerReihe(100,-1,1,0,1,1,-1,-1,50) #abstand oben, - , anzahl, typ, leben, schaden, - , - , moveDown, spt, name#
        if level == 2:
            return self.makeGegnerReihe(100,-1,2,0,1,1,-1,-1,50)
        if level == 3:
            return self.makeGegnerReihe(100,-1,4,0,1,1,-1,-1,50)
        if level == 4:
            return self.makeGegnerReihe(100,-1,4,0,1,1,-1,-1,50)
        if level == 5:
            return self.makeGegnerReihe(100,300,4,0,1,1,-1,-1,50)
        if level == 6:
            return self.makeGegnerReihe(100,-1,1,0,1,1,-1,-1,50,100)
        if level == 7:
            return self.makeGegnerReihe(100,100,5,0,1,1,-1,-1,50)
        if level == 8:
            return self.makeGegnerKarofeld(2,2,50,600,300,0,2,2,-1,-1,50) #reihen, spalten, abstand oben, abstand unten, abstand seiten, gegnerNr, leben, schaden, - , - , moveDownSpeed, s.p.t, name
        if level == 9:
            return self.makeGegnerReihe(60,-1,4,0,3,1,-1,-1,50)
        if level == 10:
            return self.makeGegnerKarofeld(3,3,50,600,400,0,1,1,-1,-1,50) #reihen, spalten, abstand oben, abstand unten, abstand seiten, gegnerNr, leben, schaden, - , - , moveDownSpeed, s.p.t, name
        if level == 11:
            return self.makeGegnerKarofeld(4,4,50,600,400,0,1,1,-1,-1,50)
        if level == 12:
            return self.makeGegnerKarofeld(5,5,50,600,400,0,1,1,-1,-1,50)
        if level == 13:
            return self.makeGegnerKarofeld(3,4,50,600,400,0,3,1,-1,-1,50)
        if level == 14:
            return self.makeGegnerKarofeld(2,2,50,700,400,0,8,1,-1,-1,200)
        if level == 15:
            ausgabe = self.makeGegnerReihe(100,200,10,0,1,1,100,4,50,1000)
            ausgabe = self.appendReihe(ausgabe,self.makeGegnerReihe(200,200,2,0,1,1,100,4,50))
            ausgabe = self.appendReihe(ausgabe,self.makeGegnerReihe(300, 200,3,0,10,1,100,4,50))
            return ausgabe
        if level == 16:
            ausgabe = self.makeGegnerReihe(60, 300,20,0,3,1,60,4,50)

            return ausgabe
        if level == 17:
            return self.makeGegnerKarofeld(3,3,50,650,200,0,20,1,-1,-1,30)
        if level == 18:
            return self.makeGegnerKarofeld(2,6,50,600,400,0,15,5,-1,-1,50)
        if level == 19:
            return self.makeGegnerKarofeld(4,4,50,600,300,0,1,5,-1,-1,50, 500)
        if level == 20:
            ausgabe = self.makeGegnerReihe(60, 300,4,0,1,1,60,4,50)
            ausgabe = self.appendReihe(ausgabe,self.makeGegnerReihe(120,0,1,4,600,10,200,4,30,200, "Mitko Montag"))
            ausgabe = self.appendReihe(ausgabe,self.makeGegnerReihe(330,100,4,0,1,1,60,4,50))
            return ausgabe




        if level == 21:
            return self.makeGegnerReihe(100,300,2,1,10,5,-1,-1,50)
        if level == 22:
            return self.makeGegnerReihe(100,200,4,1,40,10,-1,-1,100, 100)
        if level == 23:
            return self.makeGegnerReihe(100,0,6,1,15,10,-1,-1,50)
        if level == 24:
            return self.makeGegnerReihe(100,0,8,1,20,5,-1,-1,50)
        if level == 25:
            return self.makeGegnerKarofeld(2,2,50,600,400,1,60,6,-1,-1,50)
        if level == 26:
            return self.makeGegnerKarofeld(2,3,50,700,400,1,70,5,-1,-1,50)
        if level == 27:
            return self.makeGegnerKarofeld(5,5,50,600,300,1,40,3,-1,-1,50)
        if level == 28:
            return self.makeGegnerKarofeld(4,5,50,600,0,1,60,3,-1,-1,50)
        if level == 29:
            return self.makeGegnerKarofeld(7,5,50,600,100,1,65,1,-1,-1,50)
        if level == 30:
            return self.makeGegnerKarofeld(2,4,50,600,50,1,110,15,-1,-1,50)
        if level == 31:
            return self.makeGegnerKarofeld(5,3,50,600,400,1,120,10,-1,-1,50)
        if level == 32:
            return self.makeGegnerKarofeld(9,2,50,750,200,1,100,10,-1,-1,50)
        if level == 33:
            return self.makeGegnerKarofeld(2,8,50,600,400,1,130,10,-1,-1,50)
        if level == 34:
            return self.makeGegnerKarofeld(5,5,50,600,500,1,150,12,-1,-1,50)
        if level == 35:
            return self.makeGegnerKarofeld(1,1,50,400,400,1,20,600,-1,-1,500)
        if level == 36:
            return self.makeGegnerKarofeld(2,7,50,600,0,1,120,17,-1,-1,38)
        if level == 37:
            return self.makeGegnerKarofeld(3,6,50,600,200,1,200,17,-1,-1,50)

        if level == 38:
            ausgabe = self.makeGegnerReihe(0, 0, 5, 1, 40, 10, 60, 4, 50)
            ausgabe = self.appendReihe(ausgabe, self.makeGegnerReihe(50, 0, 4, 1, 80, 10, 60, 4, 50))
            ausgabe = self.appendReihe(ausgabe, self.makeGegnerReihe(100, 0, 3, 1, 80, 10, 60, 4, 50))
            ausgabe = self.appendReihe(ausgabe, self.makeGegnerReihe(150, 0, 2, 1, 80, 10, 60, 4, 50))
            ausgabe = self.appendReihe(ausgabe, self.makeGegnerReihe(200, 0, 1, 1, 80, 10, 60, 4, 50))

            return ausgabe
        if level == 39:
            return self.makeGegnerKarofeld(5,5,50,600,400,1,20,100,-1,-1,50)


        if level == 40:
            ausgabe = self.makeGegnerReihe(60,100 ,6,0,50,10,60,4,50)
            ausgabe = self.appendReihe(ausgabe,self.makeGegnerReihe(120,0,1,5,5000,10,200,4,50,100, "Pfälzer Melzer"))
            ausgabe = self.appendReihe(ausgabe,self.makeGegnerReihe(330,100, 4,1,30,1,60,4,50))
            return ausgabe



        if level == 60:
            ausgabe = self.makeGegnerReihe(60,100 ,8,0,50,10,60,4,50)
            ausgabe = self.appendReihe(ausgabe,self.makeGegnerReihe(120,0,1,6,10000,10,200,4,50,100, "Mithut Mitwoch"))
            ausgabe = self.appendReihe(ausgabe,self.makeGegnerReihe(330,100, 4,1,30,1,60,4,50))
            return ausgabe











    def makeGegnerReihe(self,posY,abstandSeiten = 0, anzahl = 1, gegnerNr=0, leben = 1, schaden = 1, size = 1, speed = 4, moveDownSpeed = 50,schussProTausend = 10, name = "boss"):
        if gegnerNr == 0:
            groese = 120
            geschw = 3
        elif gegnerNr == 1:
            groese = 60
            geschw = 3
        elif gegnerNr == 2:
            groese = 80
            geschw = 6
        else:
            groese = size
            geschw = speed

        gegnerBild = pygame.transform.scale(self.gegnerBilder[gegnerNr], (groese, groese))
        waffenBild = pygame.transform.scale(self.gegnerBilder[3], (int(groese / 5), int(groese / 5)))
        if gegnerNr == 5:
            pi = pygame.image.load("bilder/explosion/pi.png")
            waffenBild = pygame.transform.scale(pi, (int(groese / 5), int(groese / 5)))

        abstand = int((self.screenX-2*abstandSeiten)/(anzahl+1))
        ausgabe = []
        for i in range(1,anzahl+1):
            ausgabe.append(classGegner.gegner(abstandSeiten + i*abstand-groese /2, posY, gegnerNr, gegnerBild, waffenBild, leben, schaden, groese,geschw, moveDownSpeed,schussProTausend, name))
        return ausgabe


    def makeGegnerKarofeld(self,reihen=1, spalten=1, abstandOben = 0, abstandUnten = 0, abstandSeiten = 0, gegnerNr=0, leben = 1, schaden = 1, size = 1, speed = 4, moveDownSpeed = 50 ,schussProTausend = 10, name = "Boss"):
        # berechnen des abschtandes der einzelnen gegner
        ySpace = int(((self.screenY-abstandOben)-abstandUnten) / (spalten + 1))
        gegnerListe = []
        output = []
        for x in range(1, reihen + 1):
            print("make reihe")
            gegnerListe = self.makeGegnerReihe(abstandOben+x*ySpace,abstandSeiten,  spalten, gegnerNr, leben, schaden, size, speed, moveDownSpeed,schussProTausend)
            for gegner in gegnerListe:
                output.append(gegner)
            gegnerliste = []
        return output

    def makeGegner(self, posX, posY, gegnerNr=0, leben=1, schaden=1, size=1, speed=4, moveDownSpeed=50,schussProTausend = 10, name = "boss"):
        if gegnerNr == 0:
            groese = 120
            geschw = 3
        elif gegnerNr == 1:
            groese = 60
            geschw = 3
        elif gegnerNr == 2:
            groese = 80
            geschw = 6
        else:
            groese = size
            geschw = speed


        gegnerBild = pygame.transform.scale(self.gegnerBilder[gegnerNr], (groese, groese))
        waffenBild = pygame.transform.scale(self.gegnerBilder[3], (int(groese / 5), int(groese / 5)))
        if gegnerNr == 5:
            pi = pygame.image.load("bilder/explosion/pi.png")
            waffenBild = pygame.transform.scale(pi, (int(groese / 5), int(groese / 5)))

        ausgabe = []
        ausgabe.append(classGegner.gegner(posX - groese / 2, posY, gegnerNr, gegnerBild, waffenBild, leben, schaden, size, geschw, moveDownSpeed,schussProTausend, name))
        return ausgabe

    def appendReihe(self, gegnerListe, neue):
        for gegner in neue:
            gegnerListe.append(gegner)
        return gegnerListe


