from ..Interfaces import *


class SwapMutation(IMutation):
    """
    Выбираем в популяции случайную особь и меняем у нее два случайных гена местами. 
    """
    def execute(self, population: Population, mutation_rate: float) -> None:

        if mutation_rate < 0 or mutation_rate > 1:
            raise ValueError("Вероятность мутации < 0 или > 1")

        for _ in range( round(mutation_rate * 100) ):
            random_individual = random.choice( list(population.get().keys()) )

            mutant = self.__switch_genes(random_individual)
            mutant_fitness = population.calculate_fitness(mutant) 

            population.remove(random_individual, population.get()[random_individual])
            population.add(mutant, mutant_fitness)

    def __switch_genes(self, individual: Tuple[int, ...]) -> Tuple[int, ...]:
        idx1 = random.randint(0, len(individual) - 1)
        idx2 = random.randint(0, len(individual) - 1)
        
        if idx1 == idx2:
            idx2 -= 1

        mutant = list(individual)

        mutant[idx1], mutant[idx2] = mutant[idx2], mutant[idx1]

        # Исключаем случай, когда выбранный случайный индекс является началом или концом
        if idx1 == 0 or idx1 == len(mutant) - 1 or idx2 == 0 or idx2 == len(mutant) - 1:
            mutant[0] = mutant[-1]

        return tuple(mutant)


class UniformMutation(IMutation):
    """
    При равномерной мутации каждая позиция в особи имеет небольшую 
        вероятность быть измененной.
    """
    def execute(self, population: Population, mutation_rate: float) -> None:

        if mutation_rate < 0 or mutation_rate > 1:
            raise ValueError("Вероятность мутации < 0 или > 1")

        pass


class InversionMutation(IMutation):
    """
    В инверсии происходит обратное перестроение части особи.
    """
    def execute(self, population: Population, mutation_rate: float) -> None:

        if mutation_rate < 0 or mutation_rate > 1:
            raise ValueError("Вероятность мутации < 0 или > 1")

        pass
