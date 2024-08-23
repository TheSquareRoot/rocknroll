from math import pi

class Particle:
    def __init__(self, radius, density, fadh):
        self.radius = radius
        self.density = density
        self.fadh = fadh

    @property
    def volume(self):
        return (4/3) * pi * self.radius **3

    @property
    def mass(self):
        return self.density * self.volume
