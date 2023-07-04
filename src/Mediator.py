
from GUI.gui import *


class Mediator:

    def __init__(self, window):
        self.window = window
        self.window.set_mediator(self)
        self.tsp = None

    def run(self):
        cities = self.window.sc.get_cities()
        #print(cities)
        population_size = int(self.window.lineEdit_X.text())
        generation_number = int(self.window.lineEdit_X_2.text())
        mutation_chance = float(self.window.lineEdit_X_3.text())
        crossing_chance = float(self.window.lineEdit_X_4.text())
        #print(population_size, generation_number, mutation_chance, crossing_chance)

        """
        Здесь происходит инициализация алгоритма с полученными с GUI параметрами,
        включение алгоритма, возвращение результата, что-то вроде:
        self.tsp = TSP(..., ..., ...)
        return self.tsp.run()
        """

        return self.window.sc.get_cities #здесь будем возвращать результат работы алгоритма

