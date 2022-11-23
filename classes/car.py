class Tyre():

    def __init__(self, age, compound):
        self.age = age
        self.compound = compound

    def __repr__(self) -> str:
        return "Tyres are " + str(self.age) + " laps old and the compound is " + str(self.compound)

    def getTyreAge(self):
        return self.age

    def setTyreAge(self, age):
        if (type(age) == int):
                self.age = age
        else:
            raise TypeError("Input parameter is not Int. It was " + type(age))
        return 

    def getTyreCompound(self):
        return self.compound

    def setTyreCompound(self, compound):
        if compound in ["Soft", "Medium", "Hard", "Intermediate", "Rain"]:
            self.compound = compound
        elif type(compound) != str:
            raise TypeError("Expected string, got " + type(compound))
        else:
            raise ValueError("Entered value is not one of: \"Soft\", \"Medium\", \"Hard\", \"Intermediate\", \"Rain\"")

class Engine():
    def __init__(self, power):
        self.power = power

    def __repr__(self):
        return "This is the engine's power: " + str(self.power)

    def getEnginePower(self):
        return self.power

class Constructor(Engine):
    def __init__(self, constructor, power):
        Engine.__init__(self, power)
        self.constructor = constructor
    
    def __repr__(self):
        return "This is the " + str(self.constructor) + " constructor."

    def getConstructorName(self):
        return self.constructor
        
class Car(Constructor, Tyre):
    def __init__(self, constructor, power, age, compound):
        Constructor.__init__(self, constructor, power)
        Tyre.__init__(self, age, compound)

    def __repr__(self) -> str:
        return Constructor.__repr__(self) + '\n' + Engine.__repr__(self) + '\n' + Tyre.__repr__(self)

#redBull = Car("Red Bull", 5, 10, "Soft")
#print(redBull)