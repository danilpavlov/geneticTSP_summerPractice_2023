from GUI.gui import *


class Mediator:

    def __init__(self, window):
        self.window = window
        self.window.set_mediator(self)
        self.tsp = None

    def run(self):
        cities = self.window.sc.get_cities()
        print(cities)
        population_size = self.window.horizontalSlider.value()
        generation_number = self.window.horizontalSlider_2.value()
        mutation_chance = self.window.horizontalSlider_3.value() / 100
        crossing_chance = self.window.horizontalSlider.value() / 100

        crossover = self.window.comboBox.currentText()
        mutation = self.window.comboBox_2.currentText()
        selection = self.window.comboBox_3.currentText()
        parent_selection = self.window.comboBox_4.currentText()
        print(population_size, generation_number, mutation_chance, crossing_chance)
        print(crossover, mutation, selection, parent_selection)


        """
        Здесь происходит инициализация алгоритма с полученными с GUI параметрами,
        включение алгоритма, возвращение результата, что-то вроде:
        self.tsp = TSP(..., ..., ...)
        self.window.population_history =  self.tsp.run()
        """

        #Это тест!!! Удалить после добавления инициализации алгоритма
        self.window.population_history = [{(0, 1, 2, 3, 0): 20, (1, 0, 2, 3, 1): 30, (3, 1, 2, 0, 3): 18,},
                                          {(0, 1, 2, 3, 0): 21, (1, 0, 2, 3, 1): 12, (3, 1, 2, 0, 3): 15,},
                                          {(0, 1, 2, 3, 0): 13, (1, 0, 2, 3, 1): 9, (3, 1, 2, 0, 3): 7,}]

