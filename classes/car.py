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
    def __init__(self):
        pass

    def __repr__(self):
        pass

class Constructor(Engine):
    def __init__(self, constructor):
        Engine.__init__(self)
        self.constructor = constructor
    
    def __repr__(self):
        return "This is the " + str(self.constructor) + " constructor."

    def getConstructorName(self):
        return self.constructor
        
class Car(Constructor, Tyre):
    def __init__(self, constructor, speed, age, compound):
        Constructor.__init__(self, constructor)
        Tyre.__init__(self, age, compound)
        self.speed = speed

    def __repr__(self) -> str:
        return Constructor.__repr__(self) + '\n' + Tyre.__repr__(self)

    def getSpeed(self):
        return self.speed

