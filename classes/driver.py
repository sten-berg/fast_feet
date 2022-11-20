class Driver():
    def __init__(self, name, car, reaction, cornering, braking, accelerating, competetivness):
        self.name = name
        self.car = car
        self.reaction = reaction
        self.cornering = cornering
        self.braking = braking
        self.accelerating = accelerating
        self.competetivness = competetivness

    def __repr__(self):
        return self.name + " drives for " + self.car + "!"

    def getName(self):
        return self.name
        
    def getCar(self):
        return self.car
        
    def getReaction(self):
        return self.reaction
        
    def getCornering(self):
        return self.cornering
        
    def getBraking(self):
        return self.braking
        
    def getAccelerating(self):
        return self.accelerating
        
    def getCompetetivness(self):
        return self.competetivness
