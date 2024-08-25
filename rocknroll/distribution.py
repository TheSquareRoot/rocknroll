import matplotlib.pyplot as plt
import numpy as np

from typing import Callable, Dict, List, Optional

from .config import setup_logging
from .particle import Particle


class ParticleDistribution:
    _logger = setup_logging(__name__, "logs/output.log")

    def __init__(self,
                 number: int = 1,
                 part_factory: Optional[Callable] = None,
                 factory_args: Optional[Dict] = None,
                 ) -> None:
        """
        Contructs a ParticuleDistribution object.

        If the user does not provide a particle factory, the default one is used.
        """
        self.part_factory = part_factory or self._default_particle_factory
        self.factory_args = factory_args or {}

        # Generate the list of particles
        self.particles = self._generate_particles(number)

    @staticmethod
    def _default_particle_factory(**kwargs) -> Particle:
        """By default, particles are generated with a fixed radius and density."""
        # Unpack arguments
        radius = kwargs['radius']
        density = kwargs['density']

        # Set mean and standard deviation according to Biasi
        mean = np.log(0.016 - 0.0023 * (radius ** 0.545))
        stdv = np.log(1.8 + 0.136 * (radius ** 1.4))

        # Sample a lognormal distribution to get an adhesion force
        adhesion = np.random.lognormal(mean, stdv, 1).item()

        return Particle(radius, density, adhesion)

    def _generate_particles(self, number: int) -> List[Particle]:
        """Generate a list of particles using the provided factory."""

        if not callable(self.part_factory):
            self._logger.critical("part_factory is not callable!")
            raise TypeError("part_factory must be callable")

        # If part_factory is callable, use it to generate the particle distribution
        particles = []
        for _ in range(number):
            try:
                particles.append(self.part_factory(**self.factory_args))
            except KeyError as e:
                self._logger.critical(f"Error generating particle: Missing argument {e}")
                raise
            except Exception as e:
                self._logger.critical(f"Unexpected error during particle generation: {e}")
                raise

        return particles

    # Some properties
    @property
    def length(self) -> int:
        return len(self.particles)

    def get_property_distributions(self) -> Dict[str, List[float]]:
        """Returns a dictionary containing the size, density, and adhesion distributions."""
        size_distribution = []
        density_distribution = []
        adhesion_distribution = []

        for particle in self.particles:
            size_distribution.append(particle.radius)
            density_distribution.append(particle.density)
            adhesion_distribution.append(particle.adhesion)

        return {
            'size': size_distribution,
            'density': density_distribution,
            'adhesion': adhesion_distribution
        }

    def plot(self, plot_type: str = 'box') -> None:
        distrib_stats = self.get_property_distributions()

        fig, axs = plt.subplots(1, 3)

        # Plot the distributions
        if plot_type == 'box':
            for (ax, distrib) in zip(axs, distrib_stats.values()):
                ax.boxplot(distrib)
        elif plot_type == 'violin':
            for (ax, distrib) in zip(axs, distrib_stats.values()):
                ax.violinplot(distrib)
        else:
            self._logger.critical("plot_type must be either 'box' or 'violin'")
