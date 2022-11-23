class Car():

    def __init__(self, constructor, engine, tyres, frontwing, rearwing, floor, brakes, hydralics):
        self.constructor = constructor
        self.engine = engine
        self.tyres = tyres
        self.frontwing = frontwing
        self.rearwing = rearwing
        self.floor = floor
        self.brakes = brakes
        self.hydralics = hydralics

    def getAverageStats(self):
        averageStats = 0

        for attribute in self:
            averageStats += attribute

        return averageStats


test = Car(10, 10, 10, 10, 10, 10, 10, 10)

print(test.getAverageStats())