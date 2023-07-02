from Caretaker import Caretaker
from Population import Population
from Strategy.OperatorContext import * 

from typing import List


class TSP:
    def __init__(self, adjacency_matrix: List[List[float]], 
                 generations_number: int, population_max_number: int):
        """
        @param: adjacency_matrix -- матрица смежности графа

        @param: generations_number -- число итераций алгоритма

        @param: population_max_number -- максимальный размер популяции
        """
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

                
