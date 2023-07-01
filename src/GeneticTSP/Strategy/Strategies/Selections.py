from ..Interfaces import ISelection
from typing import Dict, Tuple


class LowestFitnessSelection(ISelection):
    """
    Производим отбор популяции по наименьшему значению всех ослобей популяции, 
        после чего удаляем особи 
    """

    def execute(self, population: Dict[Tuple[int, ...], float], 
                population_max_number: int) -> None:
        population = dict(
                sorted(population.items(), key=lambda item : item[1])
                ) 

        self._kill_unadapted_individuals(population, population_max_number)
