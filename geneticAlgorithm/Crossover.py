import random
import numpy as np


class UniformRecombination:
    def do_crossover(self, individual_1, individual_2):
        size = individual_1.size
        new_ind = []
        for i in range(0, size):
            rnd = random.random()
            if rnd <= 0.5:
                new_ind.append(individual_1[i])
            else:
                new_ind.append(individual_2[i])
        return np.array(new_ind)


class NPointCrossover:
    def do_crossover(self, chromosome_1, chromosome_2, cross_points: list):
        """
        N point crossover
        Receives:
            chromosome_1, chromosome_2: chromosomes
            cross_points: array of points where the cut will be performed, these must be in ascending order
        """
        n_points = len(cross_points)
        ind_1_cuts = []
        ind_2_cuts = []
        cross_points = [0] + cross_points
        # Cuts the chromosomes in the different cross points
        for i in range(n_points):
            start = cross_points[i]
            if (i + 1) < n_points:
                end = cross_points[i + 1]
                ind_1_cuts.append([chromosome_1[start:end]])
                ind_2_cuts.append([chromosome_2[start:end]])
            else:
                ind_1_cuts.append([chromosome_1[start:]])
                ind_2_cuts.append([chromosome_2[start:]])

        # Connect the cuts in the new chromosome
        new_ind1 = np.zeros(chromosome_1.size)
        new_ind2 = np.zeros(chromosome_1.size)
        cuts = random.sample(range(n_points), n_points)
        # Assigns a side of the cuts to each chromosome
        lim = int(len(cuts) / 2)
        ind_1_selected_cuts = cuts[0:lim]
        ind_2_selected_cuts = cuts[lim:]

        for i in ind_1_selected_cuts:
            start = cross_points[i]
            if (i + 1) < n_points:
                end = cross_points[i + 1]
                new_ind1[start:end] = chromosome_1[start:end]
                new_ind2[start:end] = chromosome_2[start:end]
            else:
                new_ind1[start:] = chromosome_1[start:]
                new_ind2[start:] = chromosome_2[start:]

        for i in ind_2_selected_cuts:
            start = cross_points[i]
            if (i + 1) < n_points:
                end = cross_points[i + 1]
                new_ind1[start:end] = chromosome_2[start:end]
                new_ind2[start:end] = chromosome_1[start:end]
            else:
                new_ind1[start:] = chromosome_2[start:]
                new_ind2[start:] = chromosome_1[start:]

        return [new_ind1, new_ind2]
