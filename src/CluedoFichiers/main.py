from CluedoFichiers.casebook import CaseBook
from CluedoFichiers.alibis import Alibis
import random


def aleatoire_casebook(n=3, seed=1):
    random.seed(seed)
    _casebook = CaseBook(n)
    _casebook.nouveau_normalise(random.random())
    alibis = Alibis(_casebook)
    alibis.new_clue_index_normalized(random.random())
    alibis.new_clue_index_permute(random.random())
    _pistes = alibis.all()
    random.shuffle(_pistes)
    return _casebook, _pistes


if __name__ == "__main__":
    casebook, pistes = aleatoire_casebook(7)
    print(casebook.personnages.all())
    print(casebook.lieux.all())
    print(casebook.armes.all())
    for n, p in enumerate(pistes):
        print(f"{n}. {p}")
