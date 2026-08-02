import random

# -----------------------------
# Step 1 : Generate Population
# -----------------------------
def generate_population(size):
    population = []

    for _ in range(size):
        chromosome = list(range(8))
        random.shuffle(chromosome)
        population.append(chromosome)

    return population


# -----------------------------
# Step 2 : Fitness Function
# -----------------------------
def fitness(chromosome):

    conflicts = 0

    for i in range(8):
        for j in range(i + 1, 8):

            if abs(chromosome[i] - chromosome[j]) == abs(i - j):
                conflicts += 1

    return 28 - conflicts


# -----------------------------
# Step 3 : Tournament Selection
# -----------------------------
def tournament_selection(population):

    players = random.sample(population, 3)

    best = max(players, key=fitness)

    return best


# -----------------------------
# Step 4 : One Point Crossover
# -----------------------------
def crossover(parent1, parent2):

    point = random.randint(1, 7)

    child = parent1[:point] + parent2[point:]

    return child


# -----------------------------
# Step 5 : Mutation
# -----------------------------
def mutation(chromosome):

    a = random.randint(0, 7)
    b = random.randint(0, 7)

    chromosome[a], chromosome[b] = chromosome[b], chromosome[a]

    return chromosome


# -----------------------------
# Step 6 : Genetic Algorithm
# -----------------------------
def genetic_algorithm():

    population_size = 100

    generations = 1000

    population = generate_population(population_size)

    for generation in range(generations):

        population.sort(key=fitness, reverse=True)

        best = population[0]

        print("Generation:", generation,
              "Fitness:", fitness(best),
              best)

        if fitness(best) == 28:
            print("\nSolution Found!")
            print(best)
            print("Generation =", generation)
            return

        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)

        child = crossover(parent1, parent2)

        child = mutation(child)

        population[-1] = child

    print("No Solution Found")


genetic_algorithm()