from math import pi


class Particle:
    def __init__(self,
                 radius: float,
                 density: float,
                 adhesion: float,
                 ) -> None:
        """
        Contructs a ParticuleDistribution object.

        Arguments:
            radius {float} -- Radius of the particle [µm]
            density {float} -- Density of the particle [kg/m3]
            adhesion {float} -- Normalized adhesion force of the particle to the surface [/]
        """

        self.radius = radius
        self.density = density
        self.adhesion = adhesion

    def __repr__(self) -> str:
        return f"Particle(radius={self.radius}, density={self.density}, adhesion={self.adhesion})"

    @property
    def volume(self) -> float:
        return (4 / 3) * pi * self.radius ** 3

    @property
    def mass(self) -> float:
        return self.density * self.volume
