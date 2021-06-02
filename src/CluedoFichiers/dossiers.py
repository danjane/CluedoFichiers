import os


class Dossiers:

    def __init__(self, path, pistes, noms=None):
        if not noms:
            noms = ["Notes"] * len(pistes)
        filenames = self.construire_filenames(noms)
        self.pistes = list(zip(pistes, filenames))
        if path:
            self.path = path
        else:
            self.path = os.path.join(
                os.getcwd(), "Cobaye")
        if os.path.basename(self.path) == "Cobaye":
            self.nettoyage()
        else:
            raise RuntimeError
        os.mkdir(self.path)

    def plat(self):
        for piste in self.pistes:
            self.fichier(piste, self.path)

    def nettoyage(self):
        if os.path.isfile(self.path):
            raise RuntimeError
        if os.path.isdir(self.path) and (os.path.basename(self.path) == "Cobaye"):
            # Delete everything reachable from the directory named in 'self.path',
            # assuming there are no symbolic links.
            # CAUTION:  This is dangerous!  For example, if top == '/', it
            # could delete all your disk files.
            for root, dirs, files in os.walk(self.path, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(self.path)

    @staticmethod
    def fichier(piste, path):
        with open(os.path.join(path, piste[1]), 'w') as file:
            file.write(piste[0])

    def liste(self):
        self.liste_recursive(self.path, self.pistes)

    def liste_recursive(self, path, pistes):
        self.fichier(pistes[0], path)
        if len(pistes) > 1:
            path = os.path.join(path, "NewFolder")
            os.mkdir(path)
            self.liste_recursive(path, pistes[1:])

    @staticmethod
    def construire_filenames(noms):
        compteur = {}
        filenames = []
        for nom in noms:
            if not nom:
                nom = "Notes"
            if nom in compteur:
                compteur[nom] += 1
            else:
                compteur[nom] = 0
            filenames.append("{}_{:02d}.txt".format(nom, compteur[nom]))

        for (key, value) in compteur.items():
            if value == 0:
                filenames = [
                    x.replace(f"{key}_00.txt", f"{key}.txt") for x in filenames
                ]
        return filenames
