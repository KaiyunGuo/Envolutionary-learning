"""
My colleciton of mutation methods

Student number:20090444
Student name:20090444
"""

import random


def bit_flip (individual):
    """flip a random entity"""
    choice = random.randint(0, len(individual)-1)
    if individual[choice] == 1:
        individual[choice] = 0
    else:
        individual[choice] = 1
    return individual


def swap(individual):
    # implements the swap mutation for a permutation
    i1, i2 = random.sample(range(len(individual)), 2)
    individual[i1], individual[i2] = individual[i2], individual[i1]
    return individual


if __name__ == '__main__':
    print(swap([1, 0, 1, 0, 0, 1]))
