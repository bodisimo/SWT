class System:
    musicVolume = 0.5
    effectVolume = 0.5
    breite = 1200
    hoehe = int(0.6 * breite)

    menu = True
    levelModeActive = False
    endlesModeActive = False
    backToGame = False

    def __init__(self):
        self.musicVolume = 0.5
        self.effectVolume = 0.5
        self.breite = 1600
        self.hoehe = int(0.6 * self.breite)

    def changeMode(self, array):
        self.menu = array[0]
        self.levelModeActive = array[1]
        self.endlesModeActive = array[2]

