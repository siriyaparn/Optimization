from numpy.random import randint
from numpy.random import rand

def code_crack(individual):
    fitness = 0
    if individual[0]*0.5 + individual[1]*0.2 <= 10 and individual[0] + individual[1] <= 30:
        return individual[0]*3.0 + individual[1]*2.0
    elif individual[0]*0.5 + individual[1]*0.2 > 10 :
        return fitness - (individual[0]*0.5 + individual[1]*0.2 - 10)
    elif individual[0] + individual[1] > 30 :
        return fitness - (individual[0] + individual[1] - 30)
    else :
        return fitness - (individual[0]*0.5 + individual[1]*0.2 - 10) - (individual[0] + individual[1] - 30)

# k-tournament selection
def selection(pop, fitness, k=3):
    # first random selection
    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k-1):
        # check if better (e.g. perform a tournament)
        if fitness[ix] > fitness[selection_ix]:
            selection_ix = ix
    return pop[selection_ix]

# crossover two parents to create two children
def crossover(p1, p2, r_cross):
    # children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()
    # check for recombination
    if rand() < r_cross:
        # select crossover point that is not on the end of the string
        for i in range(0,len(p1)):
            pt = randint(1, len(p1[i])-2)
            # perform crossover
            c1[i] = p1[i][:pt] + p2[i][pt:]
            c2[i] = p2[i][:pt] + p1[i][pt:]
    return [c1, c2]

# mutation operator
def mutation(bitstring, r_mut):
    for i in range(len(bitstring)):
        # check for a mutation
        if rand() < r_mut:
            pt = randint(0, len(bitstring[i])-1)
            # flip the bit
            if bitstring[i][pt] == '0':                 
                bitstring[i] = bitstring[i][:pt] + '1' + bitstring[i][pt+1:]
            else :
                bitstring[i] = bitstring[i][:pt] + '0' + bitstring[i][pt+1:]
                
                
# decimal to binary
def decimalToBinary(n):
    bi = bin(n).replace("0b", "")
    while len(bi) < n_bits:
        bi = '0' + bi
    return bi

# genetic algorithm
def genetic_algorithm(find_fitness, n_genes, n_generation, n_population, r_crossover, r_mutation):
    # initial population of random bitstring
    population = [randint(0, 100, n_genes).tolist() for _ in range(n_population)]
    # keep track of best solution
    best, best_eval = 0, find_fitness(population[0])
    # enumerate generations
    for gen in range(n_generation):
        # evaluate all candidates in the population
        fitness = [find_fitness(c) for c in population]
        # check for new best solution
        for i in range(n_population):
            if fitness[i] > best_eval:
                best, best_eval = population[i], fitness[i]
                print(">%d, new best f(%s) = %.3f" % (gen,  population[i], fitness[i]))
        # select parents
        selected = [selection(population, fitness) for _ in range(n_population)]
        # create the next generation
        children = list()
        for i in range(0, n_population, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i+1]
            # decimal to binary
            p1 = [decimalToBinary(j) for j in p1]
            p2 = [decimalToBinary(j) for j in p2]
            # crossover and mutation
            for c in crossover(p1, p2, r_crossover):
                # mutation
                mutation(c, r_mutation)
                # binary to decimal
                c = [int(i,2) for i in c]
                # store for next generation
                children.append(c)
        # replace population
        population = children
    return [best, best_eval]                
                
                
#------------------ MAIN ------------------------
# define the total number of generations
n_generation = 100
# inputs
n_genes = 2
# bits
n_bits = 10
# define the population size
n_population = 100
# crossover rate
r_crossover = 0.9
# mutation rate
r_mutation = 1.0 / float(n_bits)
# perform the genetic algorithm search
best, fitness = genetic_algorithm(code_crack, n_genes, n_generation, n_population, r_crossover, r_mutation)
print('Done!')
print('f(%s) = %f' % (best, fitness))                
                
                
                
                
                
                
                
                
                
                