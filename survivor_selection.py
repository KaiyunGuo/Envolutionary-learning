"""
My collection of survivor selection methods

Student number:20090444
Student name:Kaiyun Guo
"""
# Complete three functions for the mu+lambda, replacement, and random uniform survivor selection methods
import numpy as np
import random



def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):
    """mu+lambda selection"""
    # rank all and take top mu
    mu = len(current_pop)

    total = np.array(current_pop + offspring)
    fit = np.array(current_fitness + offspring_fitness)
    # the ranked index of all fitness
    rank = np.argsort(-fit)
    # get top mu population according to ranked fitness
    population = [list(i) for i in total[rank]][:mu]
    fitness = list(fit[rank])[:mu]

    return population, fitness


def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    """replacement selection"""

    # replace worst lambda parents
    org_pop = np.array(current_pop)
    org_fit = np.array(current_fitness)
    rank = np.argsort(org_fit)
    # cut off the worst parents
    cut = len(offspring)
    fitness = list(org_fit[rank][cut:]) + offspring_fitness
    population = [list(i) for i in org_pop[rank]][cut:] + offspring
    
    return population, fitness

