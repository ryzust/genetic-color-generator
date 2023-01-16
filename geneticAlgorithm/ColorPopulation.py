from .ColorIndividual import ColorIndividual
import numpy as np
from .Crossover import NPointCrossover
from .Mutation import BitInversionMutation
import random


class ColorPopulation:
    individuals: list[ColorIndividual]

    def __init__(self, individuals: list[ColorIndividual]):
        self.individuals = individuals

    def randomize_population_order(self):
        self.individuals = random.sample(self.individuals, k=len(self.individuals))

    @staticmethod
    def merge_population(population1, population2) -> "ColorPopulation":
        individuals_1 = population1.individuals
        individuals_2 = population2.individuals
        merged = individuals_1 + individuals_2
        return ColorPopulation(merged)

    @staticmethod
    def generate_random_population(number_individuals) -> "ColorPopulation":
        pop = []
        for _ in range(0, number_individuals):
            tmp = ColorIndividual.generate_random_individual()
            pop.append(tmp)
        return ColorPopulation(pop)

    @staticmethod
    def dictionary_to_population(individuals_dictionary) -> "ColorPopulation":
        individuals_arr = []
        for individual in individuals_dictionary.values():
            individuals_arr.append(ColorIndividual.dictionary_to_individual(individual))
        return ColorPopulation(individuals_arr)

    @staticmethod
    def population_to_dictionary(population) -> dict:
        individuals = population.individuals
        individuals_hsl_representation = [
            individual.hsl_representation for individual in individuals
        ]
        response = {}
        for i in range(len(individuals_hsl_representation)):
            individual_hsl_representation = individuals_hsl_representation[i]
            response[i] = {
                "h": int(individual_hsl_representation[0]),
                "s": int(individual_hsl_representation[1]),
                "l": int(individual_hsl_representation[2]),
                "f": int(individuals[i].fitness),
            }
        return response

    @staticmethod
    def crossover_population(population) -> "ColorPopulation":
        crossover_method = NPointCrossover()
        next_population = []
        individuals = population.individuals
        for i in range(0, len(individuals), 2):
            parent_1 = individuals[i].chromosome
            parent_2 = individuals[i + 1].chromosome
            cross_points = [8, 16]
            son_1, son_2 = crossover_method.do_crossover(
                parent_1, parent_2, cross_points
            )
            next_population.append(ColorIndividual(son_1))
            next_population.append(ColorIndividual(son_2))
        return ColorPopulation(next_population)

    @staticmethod
    def mutate_population(population, mutation_probability) -> "ColorPopulation":
        mutation_method = BitInversionMutation()
        mutated_population = []

        for individual in population.individuals:
            mutated_population.append(
                mutation_method.do_mutation(individual, mutation_probability)
            )
        return ColorPopulation(mutated_population)

    @staticmethod
    def filter_by_fitness(population, min_threshold):
        filtered_population = []
        for individual in population.individuals:
            if individual.fitness >= min_threshold:
                filtered_population.append(individual)
        return ColorPopulation(filtered_population)
