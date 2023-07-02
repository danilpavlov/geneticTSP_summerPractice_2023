from typing import Dict, Tuple, List
import random


class Population:
    def __init__(self, adjacency_matrix: List[List[float]], population_max_number: int):
        self.population = {} # Ключ - гамильтонов цикл, Значение - его приспособленность (длина цикла)
        self.adjacency_matrix = adjacency_matrix
        self.population_max_number = population_max_number

    def get(self) -> Dict[Tuple[int, ...], float]:
        """
        Возвращает популяцию
        """
        return self.population

    def get_random_individuals(self, amount: int) -> List[Tuple[int, ...]]:
        """
        Возвращает заданное число случайных особей популяции
        """
        individuals = []
        for _ in range(amount):
            random_individual = random.choice( list(self.population.keys()) )
            individuals.append(random_individual)

        return individuals

    def add(self, individual: Tuple[int, ...], fitness: float) -> None:
        """
        Добавление особи и значение ее приспособленности в Популяцию
        """
        self.population.update({individual: fitness})

    def remove(self, individual: Tuple[int, ...], fitness: float) -> None:
        """
        Удаление индивида из популяции
        """
        self.population.pop(individual, fitness)

    def get_max_number(self) -> int:
        """
        Получение максимального числа особей в Популяции
        """
        return self.population_max_number 

    def calculate_fitness(self, individual: Tuple[int, ...]) -> float:
        """
        Считает значение приспособленности особи исходя из таблицы смежности
        """
        fitness = 0
        for i in range( len(individual) - 1):
            gene1, gene2 = list(individual)[i], list(individual)[i + 1]
            fitness += self.adjacency_matrix[gene1][gene2]

        return fitness

    def generate_random_population(self) -> None:
        """
        Генерируте случайную популяцию
        """
        for _ in range(self.population_max_number):

            seen_nodes = []
            while len(seen_nodes) != len(self.adjacency_matrix):

                # Выбираем случайный номер вершины, относительно размера
                # матрицы смжености. Если он еще не был просмотрен - 
                # заносим Его в Просмотренные Вершины 
                node_index = random.randint(0, len(self.adjacency_matrix) - 1)
                if node_index not in seen_nodes:

                    seen_nodes.append(node_index)

            fitness = self.calculate_fitness(tuple(seen_nodes))
            self.population.update({tuple(seen_nodes): fitness}) 