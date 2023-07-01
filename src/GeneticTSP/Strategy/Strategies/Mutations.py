from ..Interfaces import IMutation
from typing import Dict, Tuple


class RandomMutation(IMutation):
    """
    Выбираем в популяции случайную особь и меняем два случайных гена местами. 
    """
    def execute(self, population: Dict[Tuple[int, ...], float], 
                population_max_number: int) -> None:
        pass

