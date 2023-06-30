from abc import ABC, abstractmethod

class IMutation(ABC):
    def __init__(self):

        pass

    @abstractmethod
    def execute(self):

        pass


class ICrossover(ABC):

    def __init__(self):


        pass


    @abstractmethod
    def execute(self):

        pass


class ISelection(ABC):

    def __init(self):
        pass

    @abstractmethod
    def execute(self):

        pass
