from car import Car
from textwrap import dedent

class Driver(Car):
    def __init__(self, name, skill, competetivness, constructor, power, age, compound):
        Car.__init__(self, constructor, power, age, compound)
        self.name = name
        self.skill = skill
        self.competetivness = competetivness

    def __repr__(self):
        return dedent(f"""
            Name: {self.getName()}
            Skill: {self.getSkill()}
            Competetivness: {self.getCompetetivness()}
            Constructor: {Car.getConstructorName(self)}
            Engine Power: {Car.getEnginePower(self)}
            Tyre Age: {Car.getTyreAge(self)}
            Tyre Compound: {Car.getTyreCompound(self)}""")

    def getName(self):
        return self.name
        
    def getSkill(self):
        return self.skill

    def getCompetetivness(self):
        return self.competetivness

testName = Driver('Test Name', 100, 77, 'Red Bull', 56, 2, 'Hard')

print(testName)