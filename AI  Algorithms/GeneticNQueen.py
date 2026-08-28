import random
# STEP 1 : CREATE INITIAL POPULATION

def create_population(size, n):
    population = []
    for i in range(size):
        chromosome = list(range(n))
        random.shuffle(chromosome)
        population.append(chromosome)
        print("Generation Population", population)
    return population

# STEP 2 : FITNESS FUNCTION

def fitness(chromosome):
    print("Fitness Called")
    n = len(chromosome)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(chromosome[i] - chromosome[j]) == abs(i - j):
                conflicts += 1
    max_pairs = n * (n - 1) // 2
    return max_pairs - conflicts

# STEP 3 : TOURNAMENT SELECTION

def selection(population):

    players = random.sample(population, 2)
    print("Players for selection", players)
    return max(players, key=fitness)

# STEP 4 : ONE POINT CROSSOVER


def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n - 1)
    child = parent1[:point] + parent2[point:]
    return child

# STEP 5 : SWAP MUTATION

def mutation(child):
    n = len(child)
    a = random.randint(0, n - 1)
    b = random.randint(0, n - 1)
    child[a], child[b] = child[b], child[a]
    return child

# STEP 6 : GENETIC ALGORITHM

def genetic_algorithm(n):
    POPULATION_SIZE = 10
    population = create_population(POPULATION_SIZE, n)
    generation = 0
    max_fitness = n * (n - 1) // 2
    while True:
        population.sort(key=fitness, reverse=True)
        print("population after sorting", population)
        best = population[0]
        print("Generation:", generation, "Fitness:", fitness(best))
        if fitness(best) == max_fitness:
            print("\n========== SOLUTION FOUND ==========")
            print("Queens      :", n)
            print("Best Chromosome :", best)
            print("Fitness     :", fitness(best))
            print("Generation  :", generation)

            # Print Chessboard
            print("\nChessboard:")
            for row in range(n):
                for col in range(n):
                    if best[col] == row:
                        print("Q", end=" ")
                    else:
                        print("X", end=" ")
                print()

            break

        parent1 = selection(population)
        parent2 = selection(population)
        child = crossover(parent1, parent2)
        print("Child after crossover", child)
        child = mutation(child)
        population[-1] = child
        print("Generation Population after crossover", population)
        generation += 1


n = int(input("Enter number of queens: "))

genetic_algorithm(n)
