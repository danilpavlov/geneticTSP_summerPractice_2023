from ..Interfaces import ICrossover


class RandomCrossover(ICrossover):
    """
    Выбираем две случайные особи из популяции и меняем местами некоторые гены
        одной особи на второй

    """
    def execute(self, population: Population, crossover_rate: float) -> None:
        pass

