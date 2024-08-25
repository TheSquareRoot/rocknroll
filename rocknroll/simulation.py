from .distribution import ParticleDistribution
from .flow import Flow
from .model import ResuspensionModel


class Simulation:
    def __init__(self,
                 model: ResuspensionModel,
                 particle_distribution: ParticleDistribution,
                 flow: Flow,
                 ):

        self.model = model
        self.particle_distribution = particle_distribution
        self.flow = flow
