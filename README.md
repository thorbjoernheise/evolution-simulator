# Evolution Simulator

This Python program simulates the evolution of a population of individuals, where each individual has a size, strength, and speed, and belongs to a species. The program uses a combination of genetic algorithms and k-means clustering to evolve the population and assign individuals to species, respectively. It then visualizes the individuals and their species in a scatter plot.

## Dependencies

The program requires the following libraries:

- DEAP
- Matplotlib
- Scikit-learn

## Usage

To run the program, execute the following command:

```
python main.py
```

The program will generate a random population of individuals, evolve the population using genetic algorithms, assign each individual to a species using k-means clustering, and create a scatter plot of the individuals, where the x-axis represents size, the y-axis represents strength, and the color of each point represents the species that the individual belongs to.

## Configuration

The number of species can be controlled by adjusting the `k` parameter in the `get_species` function. The number of individuals in the population can be controlled by adjusting the `pop_size` parameter in the `main` function. The evolution of the population can be controlled by adjusting the various genetic algorithm parameters in the `main` function, such as the crossover and mutation probabilities, the selection function, etc.

## License

