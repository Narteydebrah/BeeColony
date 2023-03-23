## AUTHOR : GEORGE NARTEY DEBRAH 
## BEE COLONY ALGORITHM + BENCHMARKING 
import perfplot
import random

def generate_random_solution(n):
    return [random.uniform(-5.12, 5.12) for _ in range(n)]

def objective_function(solution):
    return sum([x ** 2 for x in solution])

def initialize_population(n, population_size):
    return [generate_random_solution(n) for _ in range(population_size)]

def evaluate_fitness(population):
    return [objective_function(solution) for solution in population]

def select_best_solution(population, fitness):
    index = fitness.index(min(fitness))
    return population[index], fitness[index]

def select_random_solution(population):
    return random.choice(population)

def bee_colony_algorithm(n, population_size, limit):
    # Initialize the population of bees with random solutions
    population = initialize_population(n, population_size)

    # Evaluate the fitness of each bee
    fitness = evaluate_fitness(population)

    # Select the best solution from the population
    best_solution, best_fitness = select_best_solution(population, fitness)

    # Main loop
    for i in range(limit):
        # Generate a new solution using the best solution and a random solution
        new_solution = [best_solution[j] + random.uniform(-1, 1) * (best_solution[j] - select_random_solution(population)[j])
                        for j in range(n)]

        # Evaluate the fitness of the new solution
        new_fitness = objective_function(new_solution)

        # Replace the worst solution in the population with the new solution
        worst_index = fitness.index(max(fitness))
        population[worst_index] = new_solution
        fitness[worst_index] = new_fitness

        # Select the new best solution from the population
        current_best_solution, current_best_fitness = select_best_solution(population, fitness)

        # Update the best solution if a new one is found
        if current_best_fitness < best_fitness:
            best_solution, best_fitness = current_best_solution, current_best_fitness

    return best_fitness

perfplot.show(
    setup=lambda n: (n, 20, 100),
    kernels=[bee_colony_algorithm],
    labels=["bee_colony_algorithm"],
    n_range=[2 ** k for k in range(1, 14)],
    xlabel="Input size",
    logx=True,
    logy=True,
)
