from CluedoFichiers.dossiers import Dossiers
import os


def test_construction():
    assert Dossiers(None, [])


def test_plat():
    dossiers = Dossiers(None, ["test1", "test2"])
    dossiers.plat()
    assert os.path.isfile(
        os.path.join(dossiers.path, "Notes_00.txt"))
    assert os.path.isfile(
        os.path.join(dossiers.path, "Notes_01.txt"))
