from ..Interfaces import * 


class LowestFitnessSelection(ISelection):
    """
    Производим отбор популяции по наименьшему значению всех ослобей популяции, 
        после чего удаляем особи 
    """

    def execute(self, population: Population) -> None:
        population_set = population.get()

        population_set= dict(
                sorted(population_set.items(), key=lambda item : item[1])
                ) 

        self._kill_unadapted_individuals(population)
