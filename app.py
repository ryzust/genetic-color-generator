from flask import Flask, jsonify, request
from geneticAlgorithm.ColorPopulation import ColorPopulation
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)


@cross_origin
@app.route("/getPopulation", methods=["GET"])
def get_initial_population():
    population = ColorPopulation.generate_random_population(20)
    response = ColorPopulation.population_to_dictionary(population)
    return jsonify(response)


@cross_origin
@app.route("/trainPopulation", methods=["POST"])
def train_population():
    current_population = request.json
    # Current population must be transformed to a Population object
    current_population = ColorPopulation.dictionary_to_population(current_population)
    # selected inviduals have a fitness of 1
    filtered_population = ColorPopulation.filter_by_fitness(current_population, 1)
    # The crossover is performed with the selected individuals
    next_population = ColorPopulation.crossover_population(filtered_population)
    next_population = ColorPopulation.mutate_population(next_population, 0.05)
    # repeat with population randomized
    filtered_population.randomize_population_order()
    next_population_2 = ColorPopulation.crossover_population(filtered_population)
    next_population_2 = ColorPopulation.mutate_population(next_population_2, 0.05)
    final_population = ColorPopulation.merge_population(
        next_population, next_population_2
    )
    response = ColorPopulation.population_to_dictionary(final_population)
    return jsonify(response)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
