import numpy as np


class ColorIndividual:

    # Chromosome is a binary representation, each block of 8 gens represents a part of HSL
    chromosome: np.ndarray
    hsl_representation: np.ndarray
    fitness: float

    @staticmethod
    def generate_random_individual():
        return ColorIndividual(np.random.randint(0, 2, size=24))

    @staticmethod
    def chromosome_to_hsl(chromosome: np.ndarray):
        chromosome_str = ""
        for i in range(chromosome.size):
            chromosome_str += f"{int(chromosome[i])}"
        hue = int(str(chromosome_str[0:8]), 2)
        # Standarize to percentage
        saturation = int(int(str(chromosome_str[8:16]), 2) * 100 / 255)
        light = int(int(str(chromosome_str[16:24]), 2) * 100 / 255)
        return np.array([hue, saturation, light])

    @staticmethod
    def decimal_to_byte(decimal):
        binary = bin(decimal).replace("0b", "")
        while len(binary) < 8:
            binary = "0" + binary
        return binary

    @staticmethod
    def standarize(percentage):
        return int((percentage * 255) / 100)

    @staticmethod
    def hsl_to_chromosome(hsl_representation: np.ndarray):
        hue, saturation, light = hsl_representation
        saturation = ColorIndividual.standarize(saturation)
        light = ColorIndividual.standarize(light)
        bin_hue = ColorIndividual.decimal_to_byte(hue)
        bin_saturation = ColorIndividual.decimal_to_byte(saturation)
        bin_light = ColorIndividual.decimal_to_byte(light)
        chromosome_str = bin_hue + bin_saturation + bin_light
        chromosome = np.zeros(len(chromosome_str))
        for i, gen in enumerate(chromosome_str):
            chromosome[i] = 0 if gen == "0" else 1
        return chromosome

    @staticmethod
    def dictionary_to_individual(dictionary_representation: dict):
        hsl = np.array(
            [
                dictionary_representation["h"],
                dictionary_representation["s"],
                dictionary_representation["l"],
            ]
        )
        chromosome = ColorIndividual.hsl_to_chromosome(hsl)
        fitness = dictionary_representation["f"]
        return ColorIndividual(chromosome, fitness)

    def __init__(self, chromosome: np.ndarray, fitness: float = 0):
        self.chromosome = chromosome
        self.fitness = fitness
        self.hsl_representation = ColorIndividual.chromosome_to_hsl(chromosome)
