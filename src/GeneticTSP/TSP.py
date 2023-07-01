from Caretaker import Caretaker
from Strategy.OperatorContext import * 

import random
from typing import List


class TSP:
    def __init__(self, adjacency_matrix: List[List[float]], 
                 generations_number: int, population_max_number: int):
        """
        @param: adjacency_matrix -- матрица смежности графа

        @param: generations_number -- число итераций алгоритма

        @param: population_max_number -- максимальный размер популяции
        """

        self.population = {} # ключ - картеж пути; значение - приспособленность

        self.adjacency_matrix = adjacency_matrix
        self.generations_number = generations_number
        self.population_max_number = population_max_number
        
        self.caretaker = Caretaker()

        self.operator_context = OperatorContext()


    def solve(self):
        pass

    def choose_operators(self, mutation: IMutation, 
                      crossover: ICrossover, selection: ISelection) -> None:
        """
        Выбораем конкретные операторы мутации, кроссовера и селекции
        """
        self.operator_context.choose_mutation(mutation)
        self.operator_context.choose_crossover(crossover)
        self.operator_context.choose_selection(selection)

    def __generate_population(self) -> None:
        """
        Создание начальной популяции
        """

        for _ in range(self.population_max_number):

            seen_nodes = []
            fitness = 0
            while len(seen_nodes) != len(self.adjacency_matrix):

                # Выбираем случайный номер вершины, относительно размера
                # матрицы смжености. Если он еще не был просмотрен - 
                # заносим Его в Просмотренные Вершины и прибавляем 
                # к Значению Приспособленности значение пути в матрице смежности. 
                node_index = random.randint(0, len(self.adjacency_matrix) - 1)
                if node_index not in seen_nodes:

                    seen_nodes.append(node_index)
                    fitness += self.adjacency_matrix[len(seen_nodes)][node_index]
            self.population.update({tuple(seen_nodes): fitness}) 
                
