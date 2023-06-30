

class Caretaker:
    def __init__(self):
        self.population_history = []

    def save(self, population):
        self.population_history.append(population)
        
    def get_history(self):
        return self.population_history
