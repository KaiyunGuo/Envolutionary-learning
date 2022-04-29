"""
My collection of recombination methods

Student number:20090444
Student name:Kaiyun Guo
"""

import random


def one_point_crossover(parent1, parent2):
    """one point crossover for permutation representations"""

    p = random.randint(1, len(parent1)-1)
    off1 = parent1[0:p] + parent2[p:]
    off2 = parent2[0:p] + parent1[p:]
    off3 = parent2[p:] + parent1[0:p]
    off4 = parent1[p:] + parent2[0:p]
    return [off1, off2, off3, off4]

def two_point_crossover(parent1, parent2):
    """two point crossover for permutation representations"""
    p = random.randint(1, len(parent1) - 1)
    q = random.randint(p, len(parent1))
    off1 = parent1[:p] + parent2[p:q] + parent1[q:]
    off2 = parent2[:p] + parent1[p:q] + parent2[q:]
    return [off1, off2]

if __name__ == '__main__':
    print(one_point_crossover([1, 3, 5, 2, 6, 4, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]))
