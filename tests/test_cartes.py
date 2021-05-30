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
