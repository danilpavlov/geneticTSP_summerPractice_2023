from ..Interfaces import *


class SinglePointCrossover(ICrossover):
    """
    До некоторого гена-маркера, родители обмениваются цепочками генов, 
        тем самым порождая двух потомков
    """
    def execute(self, parent_selection: IParentSelection, mutation: IMutation, population: Population, rates: Rates) -> None:
        parent1, parent2 = parent_selection.execute(population)
        
        marker = random.randint(1, len(parent1) - 1)

        child1 = parent1[:marker] + parent2[marker:]
        child2 = parent2[:marker] + parent1[marker:]

        child1 = self.__individual_validation(child1)
        child2 = self.__individual_validation(child2)

        child1 = self.__try_to_mutate(child1, mutation, rates)
        child2 = self.__try_to_mutate(child2, mutation, rates)

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


    def __try_to_mutate(self, individual: Tuple[int, ...], mutation: IMutation, rates: Rates) -> Tuple[int, ...]:
        mutate_chance = random.uniform(0, 1)
        if mutate_chance < rates.mutation:
            return mutation.execute(individual)
        return individual


class TwoPointCrossover(ICrossover):
    """
    Этот вид скрещивания аналогичен одноточечному скрещиванию, но 
        в данном случае может происходить обмен генами в нескольких 
        случайно выбранных точках особи (В данном случае точки 2).
    """
    def execute(self, parent_selection: IParentSelection, population: Population, rates: Rates) -> None:
        parent1, parent2 = parent_selection.execute(population)


class UniformCrossover(ICrossover):
    """
    При равномерном скрещивании каждый ген в потомке выбирается 
        случайным образом от одного из родителей.
    """
    def execute(self, parent_selection: IParentSelection, population: Population, rates: Rates) -> None:
        parent1, parent2 = parent_selection.execute(population)

