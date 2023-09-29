from .positional_list import PositionalList
from .vertex import Vertex
from .edge import Edge
from .mygraph import ADTGraph


class TSP(ADTGraph):
    def nearest_neighbor_tsp(self, start_vertex):
        """Resuelve TSP con el método del vecino más cercano"""
        if start_vertex is None:
            raise ValueError(
                f"Vértice inicial con elemento {start_vertex} no fue encontrado en el grafo"
            )

        # Creamos un conjunto de vértices visitados y una lista de vértices que representará el camino
        visited = set()
        path = [start_vertex]
        visited.add(start_vertex)
        current_vertex = start_vertex

        # Mientras no hayamos visitado todos los vértices
        while len(visited) < self.vertex_count():
            nearest_vertex = None
            # Suponemos que el peso de las aristas es positivo
            min_distance = float("inf")

            # Suponemos que incident_edges devuelve objetos Edge con atributos u, v y weight.
            for edge in self.incident_edges(current_vertex):
                neighbor = edge.v if edge.u == current_vertex else edge.u
                if neighbor not in visited and edge.weight < min_distance:
                    nearest_vertex = neighbor
                    min_distance = edge.weight

            # Si encontramos un vecino no visitado, lo agregamos al camino
            if nearest_vertex is not None:
                path.append(nearest_vertex)
                visited.add(nearest_vertex)
                current_vertex = nearest_vertex
            else:
                raise ValueError("No hay vecinos cercanos. El grafo no es conexo")
        # Volvemos al vértice inicial para completar el ciclo
        path.append(start_vertex)

        # Devolvemos una lista de vértices para facilitar su interpretación
        element_path = []
        for vertex in path:
            element_path.append(vertex.element)
        return element_path
