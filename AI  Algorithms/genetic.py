import random

# ------ Creating Population ------
def create_population(size):
    population = []
    for i in range(size):
        chromosome = list(range(8))
        random.shuffle(chromosome)
        population.append(chromosome)
    return population

# ------ Fitness Function ------
def fitness(chromosome):
    conflict = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if abs(chromosome[i] - chromosome[j]) == abs(i - j):
                conflict += 1
    return 28 - conflict

# ------ Selection Function ------
def selection(population):
    three = random.sample(population, 3)
    return max(three, key=fitness)

# ------ Crossover Function ------
def crossover(parent1, parent2):
    point = random.randint(1, 7)
    return parent1[:point] + parent2[point:]

# ------ Mutation Function ------
def mutation(child):
    a = random.randint(0, 7)
    b = random.randint(0, 7)
    child[a], child[b] = child[b], child[a]
    return child

# ------ Genetic Algorithm ------
def genetic_algorithm():
    population = create_population(100)
    generation = 0

    while True:
        population.sort(key=fitness, reverse=True)
        best = population[0]

        print("Generation:", generation, "Fitness:", fitness(best))

        if fitness(best) == 28:
            print("\nSolution Found!")
            print("Best Chromosome:", best)
            print("Generations Needed:", generation)
            break

        parent1 = selection(population)  
        parent2 = selection(population)  
        child = crossover(parent1, parent2)  
        child = mutation(child)  
        population[-1] = child 

        generation += 1

genetic_algorithm()