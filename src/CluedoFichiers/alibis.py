class Alibis:

    def __init__(self, casebook):
        self.__casebook = casebook
        self.__size = self.__casebook.size
        self.elements = self.build_elements()

    def build_elements(self):
        L = []
        for i in range(1, self.__size):
            L.append(list(self.__casebook[i].values()))
        return L

