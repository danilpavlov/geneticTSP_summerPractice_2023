

class OperatorContext():
    
    def __init__(self):
        self.strategy = None

    def execute(self, population):
        """
        Выполнение некоторого оператора (мутации or скрещивания or селекции)

        @param : популяция 
        """
        self.strategy.execute(population)

    def choose(self, strategy):
        """
        Выбор некоторой конкретной стратегии оператора

        @param : конкретная стратегия оператора
        """
        
        self.startegy = strategy
