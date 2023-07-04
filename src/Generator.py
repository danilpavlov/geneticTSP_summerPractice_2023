import random
class Gen_data:
    def __init__(self, filename):
        self.n = 10
        self.x = 0
        self.y = 0
        self.node_set = []
        self.population_size = 0
        self.generations_number = 0
        self.mutation_rate = 0
        self.crossover_rate = 0
        self.generate_data()
        self.save_data(filename)

    def generate_data(self):
        for _ in range(self.n):
            self.x = round(random.uniform(1, 30), 1)
            self.y = round(random.uniform(1, 30), 1)
            self.node_set.append([self.x, self.y])
        self.population_size = random.randint(10, 1000)
        self.generations_number = random.randint(150, 100000)
        self.mutation_rate = round(random.uniform(0.05, 0.1), 2)
        self.crossover_rate = round(random.uniform(0.8, 0.95), 2)

#это можно не сохранять, а проcто дaнные читать
    def save_data(self, filename):
        with open(filename, 'w') as file:
            node_set_line = ', '.join([' '.join(str(coord) for coord in node) for node in self.node_set])
            file.write(node_set_line + '\n')
            file.write(str(self.population_size) + '\n')
            file.write(str(self.generations_number) + '\n')
            file.write(str(self.mutation_rate) + '\n')
            file.write(str(self.crossover_rate) + '\n')


filename = 'gen.txt'
data = Gen_data(filename)

