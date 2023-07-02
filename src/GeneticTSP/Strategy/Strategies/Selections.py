from ..Interfaces import * 


class TournamentSelection(ISelection):
    """
    Турнирная селекция — сначала случайно выбирается установленное количество 
        особей (в данном случае 2), а затем из них выбирается особь с лучшим 
        значением функции приспособленности
    """
    def execute(self, population: Population) -> None:

        while len(population.get()) > population.get_max_number():
            challenger1, challenger2 = population.get_random_individuals(2)
            fitness1, fitness2 = population.get()[challenger1], population.get()[challenger2]

            if fitness1 < fitness2:
                population.remove(challenger1, fitness1)
            else:
                population.remove(challenger2, fitness2)


class RandomSelection(ISelection):
    """
    Особи выбираются случайным образом без учета их приспособленности 
    """
    def execute(self, population: Population) -> None:

        while len(population.get()) > population.get_max_number():
            random_individual = random.choice( list(population.get()) ) 
            fitness = population.get()[random_individual]
            population.remove(random_individual, fitness)


class RoulleteWheelSelection(ISelection):
    """
    Особи выбираются пропорционально их приспособленности. 
        Более приспособленные особи имеют больший шанс быть выбранными, 
        поскольку их приспособленность увеличивает их долю на колесе рулетки
    """
    def execute(self, population: Population) -> None:
        pass
