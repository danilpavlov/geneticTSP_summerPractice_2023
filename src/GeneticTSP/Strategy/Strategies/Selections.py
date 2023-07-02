from ..Interfaces import * 




class RandomSelection(ISelection):
    """
    Особи выбираются случайным образом без учета их приспособленности 
    """
    def execute(self, population: Population) -> None:

        while len(population.get()) > population.get_max_number():
            random_individual = random.choice( list(population.get()) ) 
            fitness = population.get()[random_individual]
            population.remove(random_individual, fitness)


class EliteSelection(ISelection):
    """
    Лучшие особи из текущей популяции непосредственно передаются 
    в следующее поколение 
    """
    def execute(self, population: Population) -> None:
        pass
    
