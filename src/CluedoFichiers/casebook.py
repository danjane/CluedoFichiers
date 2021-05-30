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
        self.__compteur = 0

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __getitem__(self, key):
        return {
            "personnage": self.personnages[self.__compteur]
        }

    def nouveau(self, pas):
        self.__compteur = int(pas) % len(self.personnages)

    def nouveau_normalise(self, param):
        if 0 <= param < 1:
            pas = int(param * len(self.personnages))
            self.nouveau(pas)
        else:
            raise ValueError

