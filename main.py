import random
import matplotlib.pyplot as plt
from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from sklearn.cluster import KMeans
import csv

# fitness function with set of parameters
def evaluate_fitness(parameters):
    fitness = sum(parameters)
    return fitness,

# Function that returns True/False if two individuals can reproduce
def can_reproduce(ind1, ind2):
    size_threshold = 20
    strength_threshold = 20
    speed_threshold = 20
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
toolbox.register("attr_size", random.randint, 0, 100)
toolbox.register("attr_strength", random.randint, 0, 100)
toolbox.register("attr_speed", random.randint, 0, 100)
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
NGEN = 500
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

def get_species(ind, population):
    # Initialize a list of species
    species = []
    # Iterate over the population and assign individuals to species based on their ability to reproduce
    for individual in population:
        found_species = False
        for s in species:
            if can_reproduce(individual, s[0]):
                s.append(individual)
                found_species = True
                break
        if not found_species:
            species.append([individual])
    # Return the name of the species that the input individual belongs to
    for i, s in enumerate(species):
        if ind in s:
            return 'Species {}'.format(i+1)
    return 'Unclassified'

# Get the species names for each individual in the population
species_names = [get_species(ind, population) for ind in population]

# Initialize the colors dictionary
colors = { s: plt.cm.Set1(i / len(set(species_names))) for i, s in enumerate(set(species_names)) }

# Create the 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter([ind[0] for ind in population], [ind[1] for ind in population], [ind[2] for ind in population], c=[colors[s] for s in species_names])
ax.set_xlabel("Size")
ax.set_ylabel("Strength")
ax.set_zlabel("Speed")
plt.show()

#Writing the data to population.csv
# Open a file in write mode
with open('population.csv', 'w', newline='') as csvfile:
  # Create a CSV writer object
  writer = csv.writer(csvfile)
  
  # Write the header row
  writer.writerow(['size', 'strength', 'speed', 'species'])
  
  # Iterate over the population
  for ind in population:
    # Get the species name for the individual
    species = get_species(ind, population)
    # Write the individual's data to the CSV file
    writer.writerow(list(ind) + [species])

