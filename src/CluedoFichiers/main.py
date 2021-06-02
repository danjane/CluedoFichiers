from CluedoFichiers.casebook import CaseBook
from CluedoFichiers.alibis import Alibis
from CluedoFichiers.dossiers import Dossiers
import random


def aleatoire_casebook(_n=3, seed=1):
    random.seed(seed)
    _casebook = CaseBook(_n)
    _casebook.nouveau_normalise(random.random())
    alibis = Alibis(_casebook)
    alibis.new_clue_index_normalized(random.random())
    alibis.new_clue_index_permute(random.random())
    _pistes = alibis.all()
    random.shuffle(_pistes)
    return _casebook, _pistes


if __name__ == "__main__":
    casebook, pistes = aleatoire_casebook(3)
    print(casebook.personnages.all())
    print(casebook.lieux.all())
    print(casebook.armes.all())
    for n, p in enumerate(pistes):
        print(f"{n}. {p}")
    pistes += [
        casebook.info_personnages(),
        casebook.info_lieux(),
        casebook.info_armes()
    ]
    dossier = Dossiers(None, pistes)
    dossier.plat()
