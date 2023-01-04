import random
import numpy as np
from .ColorIndividual import ColorIndividual


class BitInversionMutation:
    @staticmethod
    def do_mutation(individual, mutation_probability):
        individual = individual.chromosome
        size = individual.size
        new_ind = []
        for i in range(0, size):
            rnd = random.random()
            if rnd <= mutation_probability:
                if individual[i] == 1:
                    new_ind.append(0)
                else:
                    new_ind.append(1)
            else:
                new_ind.append(individual[i])
        return ColorIndividual(np.array(new_ind))
