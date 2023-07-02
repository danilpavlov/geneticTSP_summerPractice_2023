from ..Interfaces import *


class Panmixia(IParentSelection):
    """
    Панмиксия — оба родителя выбираются случайно, 
        каждая особь популяции имеет равные шансы быть выбранной
    """
    def execute(self, population: Population) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
        return tuple(population.get_random_individuals(2))


class Inbreeding(IParentSelection):
    """
    Первый родитель выбирается случайным образом, а вторым родителем 
        является член популяции ближайший к первому (по расстоянию Хемминга)
    """
    def execute(self, population: Population) -> Tuple[Tuple[int, ...], Tuple[int, ...]]: 
        pass


class Outbreeding(IParentSelection):
    """
    Первый родитель выбирается случайным образом, а вторым родителем 
        является член популяции наиболее отличный от первого (по расстоянию Хемминга)
    """
    def execute(self, population: Population) -> Tuple[Tuple[int, ...], Tuple[int, ...]]: 
        pass
