from typing import Protocol
from ..Population import Population


class IMutation(Protocol):

    def execute(self, population: Population, mutation_rate: float) -> None:
        """
        Оператор мутации -- замена некоторого числа генов какой-то конкретной
            особи
        """
        pass


class ICrossover(Protocol):

    def execute(self, population: Population, crossover_rate: float) -> None:
        """ 
        Оператор скрещивания -- 'шафл' генов у некоторого числа особй
        """
        pass


class ISelection(Protocol):

    def execute(self, population: Population) -> None:
        """
        Оператор селекции -- правило отбора особей внутри популяции
        """
        pass

    def _kill_unadapted_individuals(self, population: Population) -> None:
        """
        Устраняет менее приспособленные особи популяции
        """
        pass
