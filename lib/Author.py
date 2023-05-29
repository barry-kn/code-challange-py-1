class Author:
    all_authors = []

    def __init__(self, name):
        self._name = name
        self.all_authors.append(self)

    def name(self):
        return self._name
