import pytest
from CluedoFichiers.casebook import CaseBook


def test_construction():
    assert CaseBook(1)


def test_premier_personnage():
    casebook = CaseBook(1)
    assert casebook[0]["personnage"] == "Mademoiselle Josephine Rose"


def test_set_error():
    casebook = CaseBook(1)
    with pytest.raises(NotImplementedError):
        casebook[0] = ""


def test_size():
    casebook = CaseBook(1)
    assert casebook.size == 1


def test_prochain_personnage():
    casebook = CaseBook(1)
    casebook.nouveau(1)
    assert casebook[0]["personnage"] == "Colonel Michael Moutarde"


def test_normaliser_prochain():
    casebook = CaseBook(1)
    casebook.nouveau_normalise(0.9999)
    assert casebook[0]["personnage"] == casebook.personnages_possibles[-1]


def test_deux_personnages():
    casebook = CaseBook(2)
    assert casebook[0]["personnage"] == "Mademoiselle Josephine Rose"
    assert casebook[1]["personnage"] == "Colonel Michael Moutarde"


def test_deux_lieux():
    casebook = CaseBook(2)
    assert casebook[0]["lieu"] == "la salle de billard"
    assert casebook[1]["lieu"] == "la salle de bal"
