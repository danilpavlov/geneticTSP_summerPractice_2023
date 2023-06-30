from abc import ABC, abstractmethod



class IMutation(ABC):

    @abstractmethod
    def execute(self, population):
        """
        Оператор мутации -- замена некоторого числа генов какой-то конкретной
            особи
        """
        pass


class ICrossover(ABC):

    @abstractmethod
    def execute(self, population):
        """ 
        Оператор скрещивания -- 'шафл' генов у некоторого числа особй
        """
        pass


class ISelection(ABC):

    @abstractmethod
    def execute(self, population, population_max_number):
        """
        Оператор селекции -- правило отбора особей внутри популяции
        """
        pass

    def _kill_population_part(self, population, population_max_number):
        while len(population) >= population_max_number:
            population.pop()
