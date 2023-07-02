from ..Population import Population
from ..Structures import Rates

from typing import Protocol, Tuple
import random


class IMutation(Protocol):

    def execute(self, individual: Tuple[int, ...]):
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

    def execute(self, parent_selection: IParentSelection, mutation: IMutation, population: Population, rates: Rates) -> None:
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

