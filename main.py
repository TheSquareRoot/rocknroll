from rocknroll.distribution import ParticleDistribution

def main():
    # Params
    number = int(1e6)
    radius = 5
    density = 1000

    distrib = ParticleDistribution(number=number, radius=radius, density=density, part_factory=None)

    print("Plotting...")
    distrib.plot()


if __name__ == '__main__':
    main()