from .positional_list import PositionalList


class Vertex:
    def __init__(self, element):
        self.element = element
        self.incidence_collection = PositionalList()

    def element(self):
        return self.element

    def __str__(self):
        return str(self.element)
