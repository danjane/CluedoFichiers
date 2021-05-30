import os


class Dossiers:

    def __init__(self, path, pistes):
        self.pistes = pistes
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
        pass

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
