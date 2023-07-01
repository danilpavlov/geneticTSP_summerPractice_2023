from dataclasses import dataclass
from math import sqrt


@dataclass
class Node:
    x: int
    y: int 


class Adapter:
    """
    Данный класс нужен для связи между GUI и самим алгоритмом. Он работает со
    всеми вершинами в графе, выбранными пользователем. Способен составить матрицу
    смежности для получившегося полного графа.
    """
    def __init__(self):
        self.adjacency_matrix = []


    def get_adjacency_matrix(self):
        return self.adjacency_matrix

    def make_adjacency_matrix(self, node_set):
        """
        Создание матрицы смежности
        
        @param: node_set -- множество всех вершин
        """      

        pass


    def __euclidean_distance(self, node1, node2):
        """
        Находит евклидово расстояние между двумя точками в двумерном пространстве.
        """
        x1, y1 = node1.x, node1.y
        x2, y2 = node2.x, node2.y

        distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance

