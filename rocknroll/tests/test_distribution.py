import unittest

from ..distribution import ParticleDistribution


class TestDistribution(unittest.TestCase):
    def test_default_generation(self) -> None:
        radius = 5.1
        density = 1000.1
        distrib = ParticleDistribution(number=2, factory_args={'radius': radius, 'density': density})

        self.assertEqual(distrib.length, 2)
        self.assertEqual(distrib.particles[0].radius, radius)
        self.assertEqual(distrib.particles[0].density, density)

    def test_custom_generation(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
