from typing import Protocol, Dict, Tuple


class IMutation(Protocol):

    def execute(self, population: Dict[Tuple[int, ...], float] ) -> None:
        """
        Оператор мутации -- замена некоторого числа генов какой-то конкретной
            особи
        """
        pass


class ICrossover(Protocol):

    def execute(self, population: Dict[Tuple[int, ...], float] ) -> None:
        """ 
        Оператор скрещивания -- 'шафл' генов у некоторого числа особй
        """
        pass


class ISelection(Protocol):

    def execute(self, population: Dict[Tuple[int, ...], float], 
                population_max_number: int) -> None:
        """
        Оператор селекции -- правило отбора особей внутри популяции
        """
        pass

    def _kill_unadapted_individuals(self, population: Dict[Tuple[int, ...], float], 
                                    population_max_number: int) -> None:
        """
        Устраняет менее приспособленные особи популяции
        """
        pass
