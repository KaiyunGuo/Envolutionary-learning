"""
My collection of initialization methods for different representations

Student number:20090444
Student name:Kaiyun Guo
"""

import random


def permutation (pop_size, num_entities):
    """initialize a population of permutation"""

    population = []
    # generates a population of individuals represented as permutations
    while len(population) < pop_size:
        a = [random.randint(0,1) for i in range(num_entities)]
        if a not in population:
            population.append(a)

    return population

if __name__ == '__main__':
    print(permutation(20, 8))