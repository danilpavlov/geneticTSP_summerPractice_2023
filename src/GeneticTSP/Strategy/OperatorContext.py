from Interfaces import *

class OperatorContext():
    
    def __init__(self):
        self.mutation_strategy = None
        self.selection_strategy = None
        self.crossover_strategy = None

    def mutation(self, population: Dict[Tuple[int, ...], float] ) -> None:
        self.mutation_strategy.execute(population)

    def selection(self, population: Dict[Tuple[int, ...], float], 
                  population_max_number: int) -> None:
        self.selection_strategy.execute(population, population_max_number)

    def crossover(self, population: Dict[Tuple[int, ...], float]) -> None:
        self.crossover_strategy.execute(population)

    def choose_mutation(self, mutation_strategy: IMutation) -> None:
        self.mutation_strategy = mutation_strategy

    def choose_selection(self, selection_strategy: ISelection) -> None:
        self.selection_strategy = selection_strategy

    def choose_crossover(self, crossover_strategy: ICrossover) -> None:
        self.crossover_strategy = crossover_strategy

