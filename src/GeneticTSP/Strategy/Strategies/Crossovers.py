from ..Interfaces import ICrossover
from typing import Dict, Tuple


class RandomCrossover(ICrossover):
    """
    Выбираем две случайные особи из популяции и меняем местами некоторые гены
        одной особи на второй

    """
    def execute(self, population: Dict[Tuple[int, ...], float] ) -> None:
        pass

