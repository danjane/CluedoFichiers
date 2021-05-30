from CluedoFichiers.dossiers import Dossiers


def test_construction():
    assert Dossiers(None, [])


def test_plat():
    dossiers = Dossiers(None, ["test1", "test2"])
    dossiers.plat()
