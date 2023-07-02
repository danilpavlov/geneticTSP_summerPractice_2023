from ..Interfaces import *


class SinglePointCrossover(ICrossover):
    """
    До некоторого гена-маркера, родители обмениваются цепочками генов, 
        тем самым порождая двух потомков
    """
    def execute(self, parent_selection: IParentSelection, population: Population, rates: Rates) -> None:
        parent1, parent2 = parent_selection.execute(population)

        marker = random.randint(1, len(parent1) - 1)




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

