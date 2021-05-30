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
        es = []
        for i in range(self.__size):
            es.append(list(self.__casebook[i].values()))
        return es

    def new_clue_index(self, pas):
        self.clue_index = self.__indices[int(pas) % len(self.__indices)]

    def new_clue_index_normalized(self, param):
        if 0 <= param < 1:
            pas = int(param * len(self.__indices))
            self.new_clue_index(pas)
        else:
            raise ValueError

    def new_clue_index_permute(self, param):
        if 0 <= param < 1:
            pas = int(param * self.__size)
            perms = list(itertools.permutations(self.clue_index))
            self.clue_index = perms[pas]
        else:
            raise ValueError

    def __getitem__(self, key):
        pers, lieu, arme = self.__casebook[key].values()
        return [f"Alibi. {pers} était dans {lieu} avec {arme}."]
