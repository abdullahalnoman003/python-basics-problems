import random

# ============================================================
# STEP 1 : CREATE INITIAL POPULATION
# ============================================================


def create_population(size, n):

    population = []
    for i in range(size):
        chromosome = list(range(n))
        random.shuffle(chromosome)
        population.append(chromosome)

    return population


# ============================================================
# STEP 2 : FITNESS FUNCTION
# ============================================================


def fitness(chromosome):

    n = len(chromosome)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(chromosome[i] - chromosome[j]) == abs(i - j):
                conflicts += 1
    max_pairs = n * (n - 1) // 2
    return max_pairs - conflicts


# ============================================================
# STEP 3 : TOURNAMENT SELECTION
# ============================================================


def selection(population):

    players = random.sample(population, 3)
    return max(players, key=fitness)


# ============================================================
# STEP 4 : ONE POINT CROSSOVER
# ============================================================


def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n - 1)
    child = parent1[:point] + parent2[point:]
    return child


# ============================================================
# STEP 5 : SWAP MUTATION
# ============================================================


def mutation(child):

    n = len(child)
    a = random.randint(0, n - 1)
    b = random.randint(0, n - 1)
    child[a], child[b] = child[b], child[a]
    return child


# ============================================================
# STEP 6 : GENETIC ALGORITHM
# ============================================================


def genetic_algorithm(n):
    POPULATION_SIZE = 100
    population = create_population(POPULATION_SIZE, n)
    generation = 0
    max_fitness = n * (n - 1) // 2
    while True:
        population.sort(key=fitness, reverse=True)
        best = population[0]
        print("Generation:", generation, "Fitness:", fitness(best))
        if fitness(best) == max_fitness:
            print("\n========== SOLUTION FOUND ==========")
            print("Queens       :", n)
            print("Chromosome   :", best)
            print("Fitness      :", fitness(best))
            print("Generations  :", generation)

            break

        parent1 = selection(population)
        parent2 = selection(population)

        child = crossover(parent1, parent2)

        child = mutation(child)

        population[-1] = child

        generation += 1


# ============================================================
# MAIN PROGRAM
# ============================================================

n = int(input("Enter number of queens: "))

genetic_algorithm(n)
