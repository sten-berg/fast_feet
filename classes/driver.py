from car import Car
from textwrap import dedent

class Driver(Car):
    def __init__(self, name, skill, competetivness, constructor, speed, age, compound, weight):
        Car.__init__(self, constructor, speed, age, compound)
        self.name = name
        self.skill = skill
        self.competetivness = competetivness
        self.position = 0
        self.lap = 0
        self.lapTime = 0

    def __repr__(self):
        return dedent(f"""
            Name: {self.getName()}
            Skill: {self.getSkill()}
            Competetivness: {self.getCompetetivness()}
            Constructor: {Car.getConstructorName(self)}
            Speed: {Car.getSpeed(self)}
            Tyre Age: {Car.getTyreAge(self)}
            Tyre Compound: {Car.getTyreCompound(self)}""")

    def getName(self):
        return self.name
        
    def getSkill(self):
        return self.skill

    def getCompetetivness(self):
        return self.competetivness

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position += position

    def getLap(self):
        return self.lap

    def setLap(self):
        self.lap += 1
    
    def getLapTime(self):
        return self.lapTime

    def setLapTime(self, time):
        self.lapTime = time

maxVerstappen = Driver('Max Verstappen', 100, 77, 'Red Bull', 56, 2, 'Hard', 850)
danielRicciardo = Driver('Daniel Ricciardo', 100, 99, 'McLaren',20, 0, 'Soft', 830)
drivers = [maxVerstappen, danielRicciardo]
#print(drivers[0])