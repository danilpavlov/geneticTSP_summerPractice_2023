from ..Interfaces import *

from typing import Tuple


class Panmixia(IParentSelection):
    """
    Панмиксия — оба родителя выбираются случайно, 
        каждая особь популяции имеет равные шансы быть выбранной
    """
    def execute(self, population: Population) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
        return tuple(population.get_random_individuals(2))
