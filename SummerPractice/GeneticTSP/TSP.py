from Caretaker import Caretaker
from Strategy.OperatorContext import * 

from dataclasses import dataclass


@dataclass
class Node:
    """
    Класс вершины (aka город)
    """
    x: float
    y: float 


class TSP:

    def __init__(self, adjacency_matrix, generations_number, population_max_number):
        """
        @param: population -- выборка некоторых решений. Представляет собой словрь, где
            ключ - преспособленность, а значение - сам путь (список вершин)

        @param: population_max_number -- число итераций алгоритма
        """
        self.popualtion = {}
        self.generations_number = generations_number
        self.population_max_number = population_max_number
        
        self.caretaker = Caretaker()

        self.mutation_context = OperatorContext()
        self.crossover_context = OperatorContext()
        self.selection_context = OperatorContext()


    def solve(self):
        pass

    def choose_method(self, mutation, crossover, selection):
        """
        Выбораем конкретные операторы мутации, кроссовера и селекции
        """
        self.mutation_context.choose(mutation)
        self.crossover_context.choose(crossover)
        self.selection_context.choose(selection)

    def __generate_population(self):

        pass
