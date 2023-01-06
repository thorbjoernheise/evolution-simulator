# Evolution Simulator

This is a Python implementation of a genetic algorithm for optimizing a set of parameters. The algorithm evolves a population of individuals with three attributes (size, strength, and speed) through the processes of selection, crossover, and mutation. The fittest individuals are selected to form the next generation of the population, and the evolution process continues for a specified number of generations.

This project was created as a hobby project to explore the basics of genetic algorithms and how they can be used to solve optimization problems. It is a simple example of how a genetic algorithm can be implemented in Python, and it can serve as a starting point for more complex or sophisticated projects.

## Dependencies

The program requires the following libraries:

- DEAP
- Matplotlib
- Scikit-learn
- CSV

## Usage

To run the program, execute the following command:

```
python main.py
```

##Customization

The behavior of the genetic algorithm can be customized by modifying the following variables in the code:

NGEN: *The number of generations to evolve the population*
size_threshold, strength_threshold, speed_threshold: *The threshold values for determining whether two individuals can reproduce with each other (as defined in the* can_reproduce() *function)*
cxpb, mutpb: *The probability of applying crossover and mutation, respectively, to the individuals within each species (as used in the* algorithms.varAnd() *function)*

