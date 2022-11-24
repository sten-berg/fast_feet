class Corner():
    def __init__(self, name, position, exitSpeed, difficulty):
        self.name = name
        self.position = position
        self.exitSpeed = exitSpeed
        self.difficulty = difficulty

class Track():
    def __init__(self, name, trackTemperature):
        self.name = name
        self.trackTemperature = trackTemperature
        self.finishPosition = 50
        self.startPosition = 0

    def getStart(self):
        return self.startPosition

    def getFinish(self):
        return self.finishPosition

    def getName(self):
        return self.name

spaFrancorchamps = Track("Spa-Francorchamps", 50)

print(spaFrancorchamps.getStart())