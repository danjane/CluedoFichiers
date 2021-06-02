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


def test_liste():
    dossiers = Dossiers(None, ["test1", "test2"])
    dossiers.liste()
    assert os.path.isfile(
        os.path.join(dossiers.path, "Notes_00.txt"))
    assert os.path.isfile(
        os.path.join(dossiers.path, "NewFolder", "Notes_01.txt"))


def test_noms_AA():
    dossiers = Dossiers(None, ["test1", "test2"], ["A", "A"])
    dossiers.plat()
    assert os.path.isfile(
        os.path.join(dossiers.path, "A_00.txt"))
    assert os.path.isfile(
        os.path.join(dossiers.path, "A_01.txt"))


def test_noms_AB():
    dossiers = Dossiers(None, ["test1", "test2"], ["A", "B"])
    dossiers.plat()
    assert os.path.isfile(
        os.path.join(dossiers.path, "A.txt"))
    assert os.path.isfile(
        os.path.join(dossiers.path, "B.txt"))
