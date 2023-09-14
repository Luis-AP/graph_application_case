class Edge:
    def __init__(self, u, v, element, directed=True, weight=0):
        self.u = u  # Starting vertex
        self.v = v  # Ending vertex
        self.element = element
        self.weight = weight
        self.directed = directed

    def endpoints(self):
        """Retorna una tupla (u, v) donde u y v son los vértices que forman la arista"""
        return (self.u, self.v)

    def opposite(self, v):
        """ "Retorna el vértice opuesto a v en la arista"""
        if v is self.u:
            return self.v
        else:
            return self.u

    def element(self):
        """Retorna el elemento asociado a la arista"""
        return self.element

    def __str__(self):
        if self.directed:
            return f"{self.u} -({self.weight})-> {self.v}"
        else:
            return f"{self.u} -({self.weight})- {self.v}"
