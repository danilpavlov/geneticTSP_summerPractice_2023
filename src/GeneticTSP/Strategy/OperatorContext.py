from Interfaces import *

class OperatorContext():
    
    def __init__(self):
        self.mutation_strategy = None
        self.selection_strategy = None
        self.crossover_strategy = None

    def mutation(self, population: Population, mutation_rate: float) -> None:
        if self.mutation_strategy is not None:
            self.mutation_strategy.execute(population, mutation_rate)

    def selection(self, population: Population) -> None:
        if self.selection_strategy is not None:
            self.selection_strategy.execute(population)

    def crossover(self, population: Population, crossover_rate: float) -> None:
        if self.crossover_strategy is not None:
            self.crossover_strategy.execute(population, crossover_rate)

    def choose_mutation(self, mutation_strategy: IMutation) -> None:
        self.mutation_strategy = mutation_strategy

    def choose_selection(self, selection_strategy: ISelection) -> None:
        self.selection_strategy = selection_strategy

    def choose_crossover(self, crossover_strategy: ICrossover) -> None:
        self.crossover_strategy = crossover_strategy

