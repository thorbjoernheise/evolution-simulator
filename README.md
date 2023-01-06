# Evolution Simulator

This is a Python implementation of a genetic algorithm for optimizing a set of parameters. The algorithm evolves a population of individuals with three attributes (size, strength, and speed) through the processes of selection, crossover, and mutation. The fittest individuals are selected to form the next generation of the population, and the evolution process continues for a specified number of generations.

This project was created as a hobby project to explore the basics of genetic algorithms and how they can be used to solve optimization problems. It is a simple example of how a genetic algorithm can be implemented in Python, and it can serve as a starting point for more complex or sophisticated projects.

## Dependencies

The program requires the following libraries:

- DEAP [(LGPL 2.1 license)](https://github.com/thorbjoernheise/evolution-simulator/blob/main/LICENSES/deap.txt)
- Matplotlib [(Python Software Foundation License)](https://github.com/thorbjoernheise/evolution-simulator/blob/main/LICENSES/matplotlib.txt)
- Scikit-learn [(BSD 3-clause license)](https://github.com/thorbjoernheise/evolution-simulator/blob/main/LICENSES/scikit-learn.txt)
- Numpy [(BSD 3-clause license)](https://github.com/thorbjoernheise/evolution-simulator/blob/main/LICENSES/numpy.txt)

This project uses the Python standard library, which is licensed under the Python Software Foundation License.

## Usage

To run the program, execute the following command:

```
python main.py
```

## Customization

The behavior of the genetic algorithm can be customized by modifying the following variables in the code:

__NGEN:__ *The number of generations to evolve the population*
 
__size_threshold, strength_threshold, speed_threshold:__ *The threshold values for determining whether two individuals can reproduce with each other (as defined in the* can_reproduce() *function)* 
 
__cxpb, mutpb:__ *The probability of applying crossover and mutation, respectively, to the individuals within each species (as used in the* algorithms.varAnd() *function)*


## Further Resources

- [DEAP documentation](https://deap.readthedocs.io/en/stable/)
- [Matplotlib documentation](https://matplotlib.org/stable/documentation/index.html)
- [Scikit-learn documentation](https://scikit-learn.org/stable/documentation.html)
- [NumPy documentation](https://numpy.org/doc/stable/)

