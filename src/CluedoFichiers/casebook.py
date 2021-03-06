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
        "le poignard",
        "le chandelier",
        "le revolver",
        "la corde",
        "la clef Anglaise",
        "le poison",
        "le fer à cheval"
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

    def nouveau_normalise(self, param):
        if isinstance(param, float):
            param = [param]*3
        self.personnages.nouveau_normalise(param[0])
        self.lieux.nouveau_normalise(param[1])
        self.armes.nouveau_normalise(param[2])

    def info_personnages(self):
        info = ["Les personnages suivants étaient présents:"] + self.personnages.all()
        return "\n".join(info)

    def info_lieux(self):
        info = ["Les lieux suivants étaient occupés:"] + self.lieux.all()
        return "\n".join(info)

    def info_armes(self):
        info = ["Les armes suivantes étaient présentes:"] + self.armes.all()
        return "\n".join(info)
