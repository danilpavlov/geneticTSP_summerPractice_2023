from GeneticTSP.Strategy.Strategies.Mutations import *
from GeneticTSP.Strategy.Strategies.Crossovers import *
from GeneticTSP.Strategy.Strategies.Selections import *
from GeneticTSP.Strategy.Strategies.ParentSelections import *
from GeneticTSP.TSP import *
from Adapter import *


class Testing():
    def __init__(self):
        tsp = None

    def execute(self, node_set: List[List[float]], population_size: int, generation_number: int, mutation_rate: float, crossover_rate: float):
        adapter = Adapter()
        adapter.make_adjacency_matrix(node_set)
        self.tsp = TSP(adapter.get_adjacency_matrix(), generation_number, population_size, mutation_rate, crossover_rate)

        # Можно менять операторов !!!
        self.__choose_operators(UniformMutation(), TwoPointCrossover(), EliteSelection(), RoulleteWheelParentSelection())

        population_history = self.tsp.run() # Список популяции на каждой итерации алгоритма
        return population_history
        
    def __choose_operators(self, mutation: IMutation, crossover: ICrossover, selection: ISelection, parent_selection: IParentSelection):
        self.tsp.choose_operators(mutation, crossover, selection, parent_selection)


test = Testing()

node_set = [[1.1, 1.1], [2.1, 2.3], [3.1, 3.0]]
population_size = 10
generations_number = 1000
mutation_rate = 0.15
crossover_rate = 0.8

population_history = test.execute(node_set, population_size, generations_number, mutation_rate, crossover_rate)
print(population_history)
