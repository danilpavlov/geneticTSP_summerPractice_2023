from ..Interfaces import *


class SwapMutation(IMutation):
    """!
    Выбираем в популяции случайную особь и меняем у нее два случайных гена местами. 
    """
    def execute(self, individual: Tuple[int, ...]) -> Tuple[int, ...]:
        mutant = list(individual[:-1])
        idx1 = random.randint(0, len(mutant) - 1)
        idx2 = random.randint(0, len(mutant) - 1)
        mutant[idx1], mutant[idx2] = mutant[idx2], mutant[idx1]
        mutant.append(mutant[0])
        return tuple(mutant)


class UniformMutation(IMutation):
    """!
    При равномерной мутации каждая позиция в особи имеет небольшую 
        вероятность быть измененной.
    """
    def execute(self, individual: Tuple[int, ...]) -> Tuple[int, ...]:
        not_seen = list(individual[:-1])
        mutant = []
        gene_mutation_chance = 0.1
        for gene in individual[:-1]:
            random_chance = random.uniform(0, 1)
            if random_chance < gene_mutation_chance or gene not in not_seen:
                random_gene = random.choice( not_seen )
                mutant.append(random_gene)
                not_seen.remove(random_gene)
            else:
                mutant.append(gene)
                not_seen.remove(gene)
        mutant.append(mutant[0])
        return tuple(mutant)


class ScrambleMutation(IMutation):
    """!
    Выбираются две случайные позиции в особи, и гены между этими 
        позициями перемешиваются случайным образом.
    """
    def execute(self, individual: Tuple[int, ...]) -> Tuple[int, ...]:
        mutant = list(individual[:-1])
        idx1 = random.randint(0, len(mutant) - 1)
        idx2 = random.randint(0, len(mutant) - 1)

        start_idx = min(idx1, idx2)
        end_idx = max(idx1, idx2)
        if start_idx == end_idx:
            return individual

        subsequence = mutant[start_idx + 1:end_idx]

        random.shuffle(subsequence)

        mutant = mutant[:start_idx + 1] + subsequence + mutant[end_idx:]
        mutant = list(set(mutant))
        mutant.append(mutant[0])
        return tuple(mutant)

