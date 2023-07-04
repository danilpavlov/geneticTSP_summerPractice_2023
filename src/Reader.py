class Data_file:
    def __init__(self, filename):
        self.node_set = []
        self.population_size = 0
        self.generations_number = 0
        self.mutation_rate = 0
        self.crossover_rate = 0
        self.read_data(filename)

    def read_data(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

            node_set_line = lines[0].strip()
            nodes = node_set_line.split(',')
            for node in nodes:
                coords = node.split()
                self.node_set.append([float(coords[0]), float(coords[1])])

            self.population_size = int(lines[1].strip())
            self.generations_number = int(lines[2].strip())
            self.mutation_rate = float(lines[3].strip())
            self.crossover_rate = float(lines[4].strip())


filename = 'file.txt'
read_f = Data_file(filename)
