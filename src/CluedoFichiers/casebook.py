import itertools


class CaseBook:
    """ Ensemble de personnages, lieux et armes """

    personnages = [
        "Mademoiselle Josephine Rose",
        "Colonel Michael Moutarde",
        "Madame Blanche Leblanc",
        "Révérend John Olive",
        "Docteure Orchidée",
        "Madame Patricia Pervenche",
        "Professeur Peter Violet"
    ]

    def __init__(self, size):
        self.size = size
        self.__indices = list(
            itertools.permutations(self.personnages, self.size)
            )
        self.__compteur = 0

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __getitem__(self, key):
        personnages = self.__indices[self.__compteur]
        return {
            "personnage": personnages[key]
        }

    def nouveau(self, pas):
        self.__compteur = int(pas) % len(self.__indices)

    def nouveau_normalise(self, param):
        if 0 <= param < 1:
            pas = int(param * len(self.__indices))
            self.nouveau(pas)
        else:
            raise ValueError
