from GeneticTSP.Strategy.Interfaces import *


class SinglePointCrossover(ICrossover):
    """
    До некоторого гена-маркера, родители обмениваются цепочками генов, 
        тем самым порождая двух потомков
    """
    def execute(self, parent_selection: IParentSelection, mutation: IMutation, population: Population, rates: Rates) -> None:
        parent1, parent2 = parent_selection.execute(population)
        
        marker = random.randint(1, len(parent1[:-1]) - 1)

        child1 = parent1[:marker] + parent2[marker:]
        child2 = parent2[:marker] + parent1[marker:]

        child1 = self.__individual_validation(child1)
        child2 = self.__individual_validation(child2)

        child1 = self._try_to_mutate(child1, mutation, rates)
        child2 = self._try_to_mutate(child2, mutation, rates)

        fitness1 = population.calculate_fitness(child1)
        fitness2 = population.calculate_fitness(child2)

        population.add(child1, fitness1)
        population.add(child2, fitness2)

    def __individual_validation(self, child: Tuple[int, ...]) -> Tuple[int, ...]:
        gene_set = [i for i in range(len(child) - 1)]
        better_child = [gene for gene in child if child.count(gene) == 1]
        while len(better_child) < len(gene_set):
            random_gene = random.choice( gene_set )
            if random_gene not in better_child:
                better_child.append(random_gene)
        better_child.append(better_child[0])
        return tuple(better_child)


class TwoPointCrossover(ICrossover):
    """
    Этот вид скрещивания аналогичен одноточечному скрещиванию, но 
        в данном случае может происходить обмен генами в нескольких 
        случайно выбранных точках особи (В данном случае точки 2).
    """
    def execute(self, parent_selection: IParentSelection, mutation: IMutation, population: Population, rates: Rates) -> None:
        parent1, parent2 = parent_selection.execute(population)

        crossover_markers = random.sample(range(1, len(parent1[:-1])), 2)
        crossover_markers.sort()
        
        child1 = (
                parent2[:crossover_markers[0]] + 
                parent1[crossover_markers[0]:crossover_markers[1]] +
                parent2[crossover_markers[1]:]
                )

        child1 = (
                parent1[:crossover_markers[0]] + 
                parent2[crossover_markers[0]:crossover_markers[1]] +
                parent1[crossover_markers[1]:]
                )

        child1 = self._try_to_mutate(tuple(child1), mutation, rates)
        child2 = self._try_to_mutate(tuple(child1), mutation, rates)
        
        fitness1 = population.calculate_fitness(child1)
        fitness2 = population.calculate_fitness(child2)
        
        population.add(child1, fitness1)
        population.add(child2, fitness2)


class UniformCrossover(ICrossover):
    """
    При равномерном скрещивании каждый ген в потомке выбирается 
        случайным образом от одного из родителей.
    """
    def execute(self, parent_selection: IParentSelection, mutation: IMutation, population: Population, rates: Rates) -> None:
        parent1, parent2 = parent_selection.execute(population)

        child1 = []
        child2 = []

        for i in range(len(parent1) - 1):
            random_number = random.randint(0, 1)
            if random_number == 0:
                child1.append(parent1[i])
                child2.append(parent2[i])
            else:
                child1.append(parent2[i])
                child2.append(parent1[i])

        child1.append(child1[0])
        child2.append(child2[0])

        child1 = self._try_to_mutate(tuple(child1), mutation, rates)
        child2 = self._try_to_mutate(tuple(child2), mutation, rates)

        fitness1 = population.calculate_fitness(child1)
        fitness2 = population.calculate_fitness(child2)

        population.add(child1, fitness1)
        population.add(child2, fitness2)

