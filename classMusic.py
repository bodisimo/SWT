import pygame

class music:
    soundtrack = 0
    songNr = 0

    def __init__(self):
        self.soundtrack = pygame.mixer.music.load("musik/vitas.ogg")
        pygame.mixer.music.play(0, 0, 3000)

    def playMusic(self):

        if self.songNr == 0:
            self.soundtrack = pygame.mixer.music.load("musik/soundtrack.ogg")
            pygame.mixer.music.play(0, 0, 3000)
        if self.songNr == 1:
            self.soundtrack = pygame.mixer.music.load("musik/soundtrack2.ogv")
            pygame.mixer.music.play(0, 0, 3000)
        if self.songNr == 2:
            self.soundtrack = pygame.mixer.music.load("musik/vitas.ogg")
            pygame.mixer.music.play(0, 0, 3000)
        if self.songNr == 3:
            self.soundtrack = pygame.mixer.music.load("musik/vitas2.ogg")
            pygame.mixer.music.play(0, 0, 3000)


    def playNextSong(self):
        if self.songNr >= 3:
            self.songNr = 0
        else:
            self.songNr += 1
        self.playMusic()


    def musicChoise(self,nr):
        self.songNr = nr
        self.playMusic()

    def musicPause(self):
        pygame.mixer.music.stop()

    #def changeMusicVolume(self, volume):
