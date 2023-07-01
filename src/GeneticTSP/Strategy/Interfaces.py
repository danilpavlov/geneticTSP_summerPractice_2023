from ..Population import Population

from typing import Protocol


class IMutation(Protocol):

    def execute(self, population: Population, mutation_rate: float) -> None:
        """
        Оператор мутации -- замена некоторого числа генов какой-то особи
        """
        pass


class IParentSelection(Protocol):

    def execute(self, population: Population): 
        """
        Оператор выбора родителей для дальнейшего скрещивания
        """
        pass


class ICrossover(Protocol):

    def execute(self, parent_selection: IParentSelection, population: Population, crossover_rate: float) -> None:
        """ 
        Оператор скрещивания -- 'шафл' генов у некоторого числа особей
        """
        pass


class ISelection(Protocol):

    def execute(self, population: Population) -> None:
        """
        Оператор селекции -- правило отбора особей внутри популяции
        """
        pass

