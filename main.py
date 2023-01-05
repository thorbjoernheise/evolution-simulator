import random
import matplotlib.pyplot as plt
from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from sklearn.cluster import KMeans

# fitness function with set of parameters
def evaluate_fitness(parameters):
    fitness = sum(parameters)
    return fitness,

# Function that returns True/False if two individuals can reproduce
def can_reproduce(ind1, ind2):
    size_threshold = 5
    strength_threshold = 5
    speed_threshold = 5
    size_diff = abs(ind1[0] - ind2[0])
    strength_diff = abs(ind1[1] - ind2[1])
    speed_diff = abs(ind1[2] - ind2[2])
    if size_diff > size_threshold or strength_diff > strength_threshold or speed_diff > speed_threshold:
        return False
    return True

class Individual(tuple):
    def __new__(cls, values):
        return tuple.__new__(cls, values)
    def __init__(self, values):
        self.fitness = creator.FitnessMax(values=evaluate_fitness(values))
    def __setitem__(self, index, value):
        lst = list(self)
        lst[index] = value
        self = self.__class__(lst)

creator.create("Individual", Individual)

# Defining genetic representation of individuals
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", Individual)

# Defining population
toolbox = base.Toolbox()
toolbox.register("attr_size", random.randint, 0, 10)
toolbox.register("attr_strength", random.randint, 0, 10)
toolbox.register("attr_speed", random.randint, 0, 10)
toolbox.register("individual", tools.initCycle, Individual,
                 (toolbox.attr_size, toolbox.attr_strength, toolbox.attr_speed), n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Defining evolutionary algorithm
toolbox.register("evaluate", evaluate_fitness)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Evolve the population
population = toolbox.population(n=200)
NGEN = 200
for generation in range(NGEN):
    # Check if the population has diverged enough to form new species
    species = []
    for individual in population:
        found_species = False
        for s in species:
            if can_reproduce(individual, s[0]):
                s.append(individual)
                found_species = True
                break
        if not found_species:
            species.append([individual])

    # Evolve each species separately
    for s in species:
        offspring = algorithms.varAnd(s, toolbox, cxpb=0.5, mutpb=0.1)
        fits = toolbox.map(toolbox.evaluate, offspring)
        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit
        s[:] = toolbox.select(offspring, k=len(s))

# Print the final population
print(population)

# Define a function that takes in an individual and returns the species it belongs to
def distance(ind1, ind2):
    size_diff = abs(ind1[0] - ind2[0])
    strength_diff = abs(ind1[1] - ind2[1])
    speed_diff = abs(ind1[2] - ind2[2])
    return size_diff + strength_diff + speed_diff

# Define a function that takes in an individual and returns the species it belongs to
def get_species(ind, population, k):
    # Use k-means clustering to divide the population into k clusters
    X = [[ind[0], ind[1], ind[2]] for ind in population]
    kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
    # Assign the individual to the cluster that it belongs to
    cluster_idx = kmeans.predict([[ind[0], ind[1], ind[2]]])[0]
    return chr(ord('A') + cluster_idx)

# Scatter plot of the individuals
k = 5
species = [get_species(ind, population, k) for ind in population]
colors = { chr(ord('A') + i): plt.cm.Set1(i / k) for i in range(k) }
plt.scatter([ind[0] for ind in population], [ind[1] for ind in population], c=[colors[s] for s in species])
plt.xlabel("Size")
plt.ylabel("Strength")
plt.show()
