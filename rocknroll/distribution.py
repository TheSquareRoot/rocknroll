import matplotlib.pyplot as plt
import numpy as np

from .config import setup_logging
from .particle import Particle


class ParticleDistribution:

    _logger = setup_logging(__name__, "./logs/output.log")

    def __init__(self, number=None,
                 radius=None,
                 density=None,
                 part_factory=None,
                 particles=None
                 ):

        if particles:
            self.particles = particles
        else:
            if part_factory:
                if callable(part_factory):
                    self._logger.debug('Particle factory must be callable')
                    self.particles = [part_factory() for _ in range(number)]
                else:
                    self._logger.error('Particle factory must be callable')
            else:
                self._logger.info(f"Creating {number} particle(s) with default factory.")
                self.particles = self._get_particles(number, radius, density)


    def __add__(self, other):
        return ParticleDistribution(particles=(self.particles + other.particles))

    @property
    def number(self):
        return len(self.particles)

    @staticmethod
    def _default_particle_factory(radius, density, fadh):
        # Sample a log-normal distribution
        fadh = np.random.lognormal(mean, stdv, 1)[0]

        return Particle(radius=radius, density=density, fadh=fadh)
    
    @staticmethod
    def _get_particles(number, radius, density):
        # Compute mean and stdv from Biasi experiments
        mean = np.log(0.016 - 0.0023 * (radius ** 0.545))
        stdv = np.log(1.8 + 0.136 * (radius ** 1.4))

        adhesion = np.random.lognormal(mean, stdv, number)
        
        return [Particle(radius=radius, density=density, fadh=fadh) for fadh in adhesion]
            

    def get_adhesion(self):
        return [ particle.fadh for particle in self.particles]

    def plot(self):
        plt.clf()
        fadh_array = self.get_adhesion()

        # plt.violinplot(fadh_array)
        plt.boxplot(fadh_array)

        plt.yscale('log')

        plt.show()

