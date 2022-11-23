class Driver():
    def __init__(self, name, team, reaction, cornering, braking, accelerating, competetivness):
        self.name = name
        self.team = team
        self.reaction = reaction
        self.cornering = cornering
        self.braking = braking
        self.accelerating = accelerating
        self.competetivness = competetivness

    def __repr__(self) -> str:
        return "Name: " + str(self.name) + "\nTeam: " + str(self.team) + "\nReaction: " + str(self.reaction) + "\nCornering: " + str(self.cornering) + "\nBraking: " + str(self.braking) + '\nAccelerating: ' + str(self.accelerating) + '\nCompetetivness: '  + str(self.competetivness)

    def getName(self):
        return self.name
        
    def getTeam(self):
        return self.team
        
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

testName = Driver("Test Name", "Red Bull", 100, 100, 100, 100, 100)

print(testName)