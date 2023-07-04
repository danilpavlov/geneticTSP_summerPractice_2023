from GeneticTSP.Strategy.Strategies.Mutations import *
from GeneticTSP.Strategy.Strategies.Crossovers import *
from GeneticTSP.Strategy.Strategies.Selections import *
from GeneticTSP.Strategy.Strategies.ParentSelections import *
from GeneticTSP.TSP import *
from Adapter import *
from Reader import *
from Generator import *

from GeneticTSP.Logger import *

class Testing():
    def __init__(self):
        tsp = None
        logger = None

    def execute(self, node_set: List[List[float]], population_size: int, generation_number: int, mutation_rate: float, crossover_rate: float):
        adapter = Adapter()
        adapter.make_adjacency_matrix(node_set)
        self.logger = Logger(generation_number)
        self.tsp = TSP(adapter.get_adjacency_matrix(), generation_number, population_size, mutation_rate, crossover_rate, self.logger)

        self.__choose_operators(ScrambleMutation(self.logger), UniformCrossover(self.logger), ExclusionSelection(), RoulleteWheelParentSelection())

        population_history = self.tsp.run() 
    
        self.__open_logs()
        return population_history
        
    def __choose_operators(self, mutation: IMutation, crossover: ICrossover, selection: ISelection, parent_selection: IParentSelection):
        self.tsp.choose_operators(mutation, crossover, selection, parent_selection)

    def __open_logs(self):
        for generation_logs in self.logger.get_loggs():
            for log in generation_logs:
                print(log)

test = Testing()

node_set = [[1.1, 1.1], [2.1, 2.3], [3.1, 3.0], [100.1, 124.4]]
population_size = 20
generations_number = 1000
mutation_rate = 0.15
crossover_rate = 0.8

#population_history = test.execute(read_f.node_set, read_f.population_size, read_f.generations_number, read_f.mutation_rate, read_f.crossover_rate)
#population_history = test.execute(data.node_set, data.population_size, data.generations_number, data.mutation_rate, data.crossover_rate)
#print(population_history)
population_history = test.execute(node_set, population_size, generations_number, mutation_rate, crossover_rate)
print(population_history[0])
print(population_history[-1])

