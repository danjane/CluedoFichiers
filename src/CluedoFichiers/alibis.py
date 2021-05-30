import itertools


class Alibis:

    def __init__(self, casebook):
        self.__casebook = casebook
        self.__size = self.__casebook.size-1
        self.elements = self.build_elements()
        self.__indices = list(
            itertools.product(range(4), repeat=self.__size)
            )
        self.clue_index = self.__indices[0]

    def build_elements(self):
        L = []
        for i in range(self.__size):
            L.append(list(self.__casebook[i].values()))
        return L

    def new_clue_index(self, pas):
        self.clue_index = self.__indices[int(pas) % len(self.__indices)]

    def new_clue_index_normalized(self, param):
        if 0 <= param < 1:
            pas = int(param * len(self.__indices))
            self.new_clue_index(pas)
        else:
            raise ValueError



