from CluedoFichiers.cartes import Cartes

class CaseBook:
    """ Ensemble de personnages, lieux et armes """

    personnages_possibles = [
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
        self.personnages = Cartes(self.size, self.personnages_possibles)

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __getitem__(self, key):
        return {
            "personnage": self.personnages[key]
        }

    def nouveau(self, pas):
        self.personnages.nouveau(pas)

    def nouveau_normalise(self, param):
        self.personnages.nouveau_normalise(param)
