from ..Interfaces import * 


class TournamentSelection(ISelection):
    """
    Турнирная селекция — сначала случайно выбирается установленное количество 
        особей (в данном случае 2), а затем из них выбирается особь с лучшим значением 
        функции приспособленности
    """
    def execute(self, population: Population) -> None:

        while len(population.get()) > population.get_max_number():
            challenger1, challenger2 = population.get_random_individuals(2)
            fitness1, fitness2 = population.get()[challenger1], population.get()[challenger2]

            if fitness1 < fitness2:
                population.remove(challenger1, fitness1)
            else:
                population.remove(challenger2, fitness2)
