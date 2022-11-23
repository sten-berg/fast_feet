class Track():
    def __init__(self, downfall, wind, trackTemperature):
        self.downfall = downfall
        self.wind = wind
        self.trackTemperature = trackTemperature

class Street(Track):
    def __init__(self, downfall, wind, width):
        super().__init__(downfall, wind, )
        self.width = width


class NonStreet(Track):
    def __init__(self, downfall, wind):
        super().__init__(downfall, wind)