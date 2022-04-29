"""
My collection of parent selection methods

Student number:20090444
Student name:Kaiyun Guo
"""
# Complete three functions for the MPS, tournament, and random-uniform parent selection methods
import random
import numpy as np


def MPS(fitness, mating_pool_size):
    """Multi-pointer selection (MPS)"""

    selected_to_mate = []

    mu = len(fitness)
    # rank
    # fitness larger better, best rank mu-1
    fit = np.array(fitness)
    rank = list(np.argsort(-fit))
    fit = list(fit[rank])

    # linear ranking
    s = 1.5
    a = []
    for i in range(mu):
        a.append((2-s) / mu + 2*i*(s-1) / (mu*(mu-1)))
    a.reverse()
    # cumulative probability distribution
    i = 0
    while i < mu:
        duplicate = fit.count(fit[i])
        if duplicate > 1:
            # if same fitness, share same probability
            prob = sum(a[i: i+duplicate]) / duplicate
            if i == 0:
                for j in range(duplicate):
                    a[i+j] = (j+1)*prob
            else:
                for j in range(duplicate):
                    a[i+j] = a[i-1] + (j+1)*prob
            i += duplicate
        else:
            if i != 0:
                a[i] = a[i-1] + a[i]
            i += 1

    # MPS
    pointer = 0             # number of chosen parents
    i = 0                   # current place on scale
    arm_length = 1 / mating_pool_size
    r = random.uniform(0, arm_length)       # initial position
    while pointer < mating_pool_size:
        #print(r, i, a)
        while r <= a[i]:
            selected_to_mate.append(rank[i])
            r += arm_length
            pointer += 1
        i += 1

    return selected_to_mate


def tournament(fitness, mating_pool_size, tournament_size):
    """Tournament selection without replacement"""
    selected_to_mate = []
    tour_idx = []
    # select λ members of a pool of μ individuals
    current_number = 0
    while current_number < mating_pool_size:
        # pick k individuals randomly
        tournament = np.random.choice(len(fitness)-1, tournament_size)
        best = 0
        idx = 0

        for i in tournament:
            if fitness[i] > best:
                best = fitness[i]
                idx = i
        # without replacement
        if idx in selected_to_mate:
            continue
        # append the best's index
        selected_to_mate.append(idx)
        tour_idx += list(tournament)
        current_number += 1
    return selected_to_mate


if __name__ == '__main__':
    print(MPS([7, 11, 11, 23, 23, 23, 3, 4], 3))
    #tournament([7, 11, 23, 3, 4, 9, 8], 3, 3)
