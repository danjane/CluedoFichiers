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
        "Mademoiselle Josephine Rose",
        "la salle de billard",
        "le poignard"
    ]


def test_clues_selection():
    casebook = CaseBook(2)
    alibis = Alibis(casebook)
    assert alibis.clue_index == (0, )


def test_new_clues_selection():
    casebook = CaseBook(3)
    alibis = Alibis(casebook)
    assert alibis.clue_index == (0, 0)
    alibis.new_clue_index(1)
    assert alibis.clue_index == (0, 1)


def test_new_clues_normalised():
    casebook = CaseBook(7)
    alibis = Alibis(casebook)
    alibis.new_clue_index_normalized(0.9999)
    assert alibis.clue_index == (3, 3, 3, 3, 3, 3)


def test_permute_clue_index():
    casebook = CaseBook(3)
    alibis = Alibis(casebook)
    alibis.new_clue_index(1)
    alibis.new_clue_index_permute(0.7)
    assert alibis.clue_index == (1, 0)


def test_one_piste():
    casebook = CaseBook(2)
    alibis = Alibis(casebook)
    assert alibis[0] == ["Alibi. Mademoiselle Josephine Rose était dans la salle de billard avec le poignard."]


def test_second_piste():
    casebook = CaseBook(3)
    alibis = Alibis(casebook)
    assert alibis[1] == ["Alibi. Colonel Michael Moutarde était dans la salle de bal avec le chandelier."]