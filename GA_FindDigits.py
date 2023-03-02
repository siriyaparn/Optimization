# genetic algorithm search of 20 digits secret code problem
from numpy.random import randint
from numpy.random import rand


def code_crack(individual):
    target =[0,1,2,3,4,5,6,7,8,9, 0,1,0,1,0,1,0,1,0,1]
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == target[i]:
             fitness += 1
    return fitness
 

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
		pt = randint(1, len(p1)-2)
		# perform crossover
		c1 = p1[:pt] + p2[pt:]
		c2 = p2[:pt] + p1[pt:]
	return [c1, c2]

# mutation operator
def mutation(bitstring, r_mut):
	for i in range(len(bitstring)):
		# check for a mutation
		if rand() < r_mut:
			# flip the bit
			bitstring[i] = randint(0,10)

# genetic algorithm
def genetic_algorithm(find_fitness, n_genes, n_generation, n_population, r_crossover, r_mutation):
	# initial population of random bitstring
	population = [randint(0, 10, n_genes).tolist() for _ in range(n_population)]
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
			# crossover and mutation
			for c in crossover(p1, p2, r_crossover):
				# mutation
				mutation(c, r_mutation)
				# store for next generation
				children.append(c)
		# replace population
		population = children
	return [best, best_eval]


#------------------ MAIN ------------------------
# define the total number of generations
n_generation = 500
# bits
n_genes = 20
# define the population size
n_population = 100
# crossover rate
r_crossover = 0.9
# mutation rate
r_mutation = 1.0 / float(n_genes)
# perform the genetic algorithm search
best, fitness = genetic_algorithm(code_crack, n_genes, n_generation, n_population, r_crossover, r_mutation)
print('Done!')
print('f(%s) = %f' % (best, fitness))