from CluedoFichiers.alibis import Alibis
from CluedoFichiers.casebook import CaseBook


def test_alibis():
    assert True


def test_construction():
    casebook = CaseBook(1)
    assert Alibis(casebook)


def test_first_set_of_alibis():
    casebook = CaseBook(2)
    alibis = Alibis(casebook)
    assert alibis.elements[0] == [
        "Colonel Michael Moutarde",
        "la salle de bal",
        "chandelier"
    ]


def test_clue_selection():
    casebook = CaseBook(2)
    alibis = Alibis(casebook)
    assert alibis.clue_index == [0]
