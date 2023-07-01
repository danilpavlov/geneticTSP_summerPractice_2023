from ..Interfaces import ICrossover


class SinglePointCrossover(ICrossover):
    """
    До некоторого гена-маркера, родители обмениваются цепочками генов, 
        тем самым порождая двух потомков
    """
    def execute(self, parent_selection: IParentSelection, population: Population, crossover_rate: float) -> None:

        if crossover_rate < 0 or crossover_rate > 1:
            raise ValueError("Вероятность скрещивания < 0 или > 1")

        pass
