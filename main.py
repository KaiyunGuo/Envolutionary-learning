"""
CISC455 Final Project
Student number:20090444
Student name:Kaiyun Guo
"""

# imports
import random
import numpy as np
import pandas as pd

# import your own modules
import readData
import initialization
import evaluation
import parent_selection
import recombination
import mutation
import survivor_selection

   
def main():
   
    random.seed()
    np.random.seed()

    # TODO: switch for different dataset
    # infection
    data, num_entities = readData.readFile()
    # severity
    # data, num_entities = readData.readFile1()

    # you may test on different parameter settings
    popsize = 10
    mating_pool_size = 2                    # has to be even
    tournament_size = 6                     # selected parent size
    xover_rate = 0.8                        # crossover rate
    mut_rate = 0.3                          # mutation rate
    gen_limit = 50                          # generation limit

    # initialize population
    gen = 0     # initialize the generation counter
    population = initialization.permutation(popsize, num_entities)
    fitness = []
    for i in range(0, popsize):
        # TODO: switch for different dataset
        # infection
        fitness.append(evaluation.fitness(population[i], data.copy(deep=True)))
        # severity
        # fitness.append(evaluation.fitness1(population[i], data.copy(deep=True)))
    print("generation", gen, ": best fitness", max(fitness), "average fitness", sum(fitness)/len(fitness))

    # evolution begins
    while gen <= gen_limit:

        # pick parents 
        parents_index = parent_selection.MPS(fitness, mating_pool_size)
        # parents_index = parent_selection.tournament(fitness, mating_pool_size, tournament_size)

        # in order to randomly pair up parents
        random.shuffle(parents_index)
    
        # reproduction
        offspring = []
        offspring_fitness = []
        i = 0    # initialize the counter for parents in the mating pool
        
        # offspring are generated using selected parents in the mating pool
        while len(offspring) < mating_pool_size:
            # recombination
            if random.random() < xover_rate:        # [0, 1) float
                if random.random() < 0.5:
                    offs = recombination.one_point_crossover(population[parents_index[i]], population[parents_index[i + 1]])
                else:
                    offs = recombination.two_point_crossover(population[parents_index[i]], population[parents_index[i + 1]])
            else:
                offs = [population[parents_index[i]], population[parents_index[i+1]]]
            # mutation
            for i in range(len(offs)):
                if random.random() < mut_rate:
                    if random.random() < 0.5:
                        offs[i] = mutation.bit_flip(offs[i])
                    else:
                        offs[i] = mutation.swap(offs[i])
                offspring.append(offs[i])
                # TODO: switch for different dataset
                # infection
                offspring_fitness.append(evaluation.fitness(offs[i], data.copy(deep=True)))
                # severity
                # offspring_fitness.append(evaluation.fitness1(offs[i], data.copy(deep=True)))

            i = i+2  # update the counter

        # organize the population of next generation
        #print(population, fitness, offspring, offspring_fitness)
        population, fitness = survivor_selection.mu_plus_lambda(population, fitness, offspring, offspring_fitness)
#        population, fitness = survivor_selection.replacement(population, fitness, offspring, offspring_fitness)
        gen += 1  # update the generation counter
        print("generation", gen, ": best fitness", max(fitness), "average fitness", sum(fitness)/len(fitness))
        # break
    # evolution ends
    
    # print the final best solution(s)
    k = 0
    picked = []
    best = max(fitness)
    for i in range(popsize):
        if fitness[i] == best:
            ind = population[i]
            if ind not in picked:
                temp = [i for i in range(len(ind)) if ind[i] == 1]
                imp = data.columns[temp]
                # print("best solution", k, population[i], fitness[i], "\n", imp)
                print(ind)
                k = k+1
                picked.append(ind)

    # TODO:switch for different dataset
    # compare with other models
    # infection
    evaluation.comparision(data)
    # severity
    # evaluation.comparision1(data)
# end of main


main()



