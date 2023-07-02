from Caretaker import Caretaker
from Population import Population
from Strategy.OperatorContext import * 

from typing import List


class TSP:
    def __init__(self, adjacency_matrix: List[List[float]], 
                 generations_number: int, population_max_number: int,
                 mutation_rate: float, crossover_rate: float):
                    
        """
        @param: adjacency_matrix -- матрица смежности графа

        @param: generations_number -- число итераций алгоритма

        @param: population_max_number -- максимальный размер популяции
        """
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.__rate_validation()

        self.population = Population(adjacency_matrix, population_max_number)

        self.generations_number = generations_number
        
        self.caretaker = Caretaker()

        self.operator_context = OperatorContext()


    def run(self):
        pass

    def choose_operators(self, mutation: IMutation, 
                         crossover: ICrossover, 
                         selection: ISelection,
                         parent_selection: IParentSelection,
                        ) -> None:
        """
        Выбораем конкретные операторы мутации, кроссовера и селекции
        """
        self.operator_context.choose_mutation(mutation)
        self.operator_context.choose_crossover(crossover)
        self.operator_context.choose_selection(selection)
        self.operator_context.choose_parent_selection(parent_selection)

    def __rate_validation(self) -> None:
        if self.mutation_rate < 0 or self.mutation_rate > 1:
            raise ValueError("Mutation rate is < 0 or > 1")
        if self.crossover_rate < 0 or self.crossover_rate > 1:
            raise ValueError("Crossover rate is < 0 or > 1")
                
