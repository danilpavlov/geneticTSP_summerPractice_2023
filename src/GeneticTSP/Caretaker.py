from typing import Dict, Tuple

class Caretaker:
    def __init__(self):
        self.population_history = []

    def save(self, population: Dict[Tuple[int, ...], float] ) -> None:
        self.population_history.append(population)
        
    def get_history(self):
        return self.population_history
