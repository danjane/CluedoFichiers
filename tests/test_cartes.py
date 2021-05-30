import pytest
from CluedoFichiers.cartes import Cartes

personnages = [
    "Mademoiselle Josephine Rose",
    "Colonel Michael Moutarde",
    "Madame Blanche Leblanc"
]


def test_cartes():
    assert Cartes(1, ["a"])


def test_premiere_carte():
    cartes = Cartes(1, personnages)
    assert cartes[0] == "Mademoiselle Josephine Rose"


def test_set_error():
    cartes = Cartes(1, personnages)
    with pytest.raises(NotImplementedError):
        cartes[0] = ""


def test_prochaine_carte():
    cartes = Cartes(1, personnages)
    cartes.nouveau(1)
    assert cartes[0] == "Colonel Michael Moutarde"


def test_normaliser_prochain():
    cartes = Cartes(1, personnages)
    cartes.nouveau_normalise(0.9999)
    assert cartes[0] == personnages[-1]


def test_deux_personnages():
    cartes = Cartes(2, personnages)
    assert cartes[0] == "Mademoiselle Josephine Rose"
    assert cartes[1] == "Colonel Michael Moutarde"


def test_all_des_deux_personnages():
    cartes = Cartes(2, personnages)
    assert cartes.all() == [
        "Mademoiselle Josephine Rose",
        "Colonel Michael Moutarde"
        ]
