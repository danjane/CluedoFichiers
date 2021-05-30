import itertools


class Cartes:

    def __init__(self, size, possibles):
        self.size = size
        self.possibles = possibles
        self.__indices = list(
            itertools.permutations(self.possibles, self.size)
            )
        self.__compteur = 0

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __getitem__(self, key):
        selected = self.__indices[self.__compteur]
        return selected[key]
