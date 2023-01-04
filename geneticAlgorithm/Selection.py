import random
from .ColorPopulation import ColorPopulation


class Selection:
    @staticmethod
    def wheel_selection(population: ColorPopulation):
        rnd = random.random()
        for i in range(0, population.number_individuals):
            # considering cumulative probabilities
            if rnd < population.probabilities[i]:
                return i

    @staticmethod
    def random_selection(population: ColorPopulation):
        return random.randint(0, len(population.individuals) - 1)
