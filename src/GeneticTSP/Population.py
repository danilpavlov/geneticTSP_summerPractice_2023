from typing import Dict, Tuple, List
import random


class Population:
    def __init__(self, adjacency_matrix: List[List[float]], population_max_number: int):
        self.population = {}
        self.adjacency_matrix = adjacency_matrix
        self.population_max_number = population_max_number

    def get(self) -> Dict[Tuple[int, ...], float]:
        return self.population

    def add(self, individual: Tuple[int, ...], fitness: float) -> None:
        self.population.update({individual: fitness})

    def remove(self, individual: Tuple[int, ...], fitness: float) -> None:
        self.population.pop(individual, fitness)

    def get_max_number(self) -> int:
        return self.population_max_number 

    def calculate_fitness(self, individual: Tuple[int, ...]) -> float:
        fitness = 0
        for i in range( len(individual) - 1):
            gene1, gene2 = list(individual)[i], list(individual)[i + 1]
            fitness += self.adjacency_matrix[gene1][gene2]

        return fitness

    def generate_random_populatioh(self) -> None:

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
