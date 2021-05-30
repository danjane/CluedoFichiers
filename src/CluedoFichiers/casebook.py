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

    lieux_possibles = [
        "la salle de billard",
        "la salle de bal",
        "la salle de bain",
        "la chambre à coucher",
        "le pavillon des invités",
        "le jardin d'hiver",
        "le bureau"
    ]

    armes_possibles = [
        "poignard",
        "chandelier",
        "revolver",
        "corde",
        "matraque",
        "clef Anglaise",
        "poison",
        "fer à cheval"
    ]

    def __init__(self, size):
        self.size = size
        self.personnages = Cartes(self.size, self.personnages_possibles)
        self.lieux = Cartes(self.size, self.lieux_possibles)
        self.armes = Cartes(self.size, self.armes_possibles)

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __getitem__(self, key):
        return {
            "personnage": self.personnages[key],
            "lieu": self.lieux[key],
            "arme": self.armes[key]
        }

    def nouveau(self, pas):
        self.personnages.nouveau(pas)
        self.lieux.nouveau(pas)
        self.armes.nouveau(pas)

    def nouveau_normalise(self, param):
        self.personnages.nouveau_normalise(param)
        self.lieux.nouveau_normalise(param)
        self.armes.nouveau_normalise(param)
