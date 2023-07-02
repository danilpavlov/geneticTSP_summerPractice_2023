from dataclasses import dataclass
from math import sqrt
from typing import List, Tuple


class Adapter:
    """
    Данный класс нужен для связи между GUI и самим алгоритмом. Он работает со
    всеми вершинами в графе, выбранными пользователем. Способен составить матрицу
    смежности для получившегося полного графа.
    """
    def __init__(self):
        self.adjacency_matrix = []

    def get_adjacency_matrix(self) -> List[List[float]]:
        return self.adjacency_matrix

    def make_adjacency_matrix(self, node_set: List[List[float]]) -> None:
        
        self.adjacency_matrix = [[] for _ in range(len(node_set))]

        for i in range(len(node_set)):

            for j in range(len(node_set)):
                distance = self.__euclidean_distance(tuple(node_set[i]), tuple(node_set[j]))
                self.adjacency_matrix[i].append(distance)

    def __euclidean_distance(self, node1: Tuple[float, float], node2: Tuple[float, float]) -> float:
        """
        Находит евклидово расстояние между двумя точками в двумерном пространстве.
        """
        x1, y1 = node1
        x2, y2 = node2
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)

