from ..Interfaces import ISelection


class LowestFitnessSelection(ISelection):
    """
    Производим отбор популяции по наименьшему значению всех ослобей популяции, 
        после чего удаляем особи 
    """

    def execute(self, population, population_max_number):
        population = dict(
                sorted(population.items(), key=lambda item : item[1])
                ) 

        self._kill_population_part(population, population_max_number)
