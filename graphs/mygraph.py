from .positional_list import PositionalList
from .vertex import Vertex
from .edge import Edge

from .priority_queue import SortedPriorityQueue


class ADTGraph:
    def __init__(self, directed=False):
        self._directed = directed
        self._vertices = PositionalList()
        self.edges_count = 0

    def vertex_count(self):
        """Devuelve la cantidad de vértices del grafo"""
        return len(self._vertices)

    def vertices(self):
        """Devuelve un iterador de los vértices del grafo"""
        for node in self._vertices:
            yield node.element()

    def edge_count(self):
        """Devuelve la cantidad de aristas del grafo"""
        return self.edges_count

    def edges(self):
        """Devuelve un iterador de las aristas del grafo"""
        edges_set = set()
        for node in self._vertices:
            vertex = node.element()
            for node2 in vertex.incidence_collection:
                edge = node2.element()
                edges_set.add(edge)
        for edge in edges_set:
            yield edge

    def get_edge(self, u, v):
        """Devuelve la arista que conecta los vértices u y v"""
        for node in u.incidence_collection:
            edge = node.element()
            if self._directed and edge.v == v:
                return edge
            # Si el grafo es no dirigido, se debe verificar que la arista
            # conecte a u con v o a v con u
            elif not self._directed and (edge.u == v or edge.v == v):
                return edge
        return None

    def degree(self, v, out=True):
        """Devuelve el grado del vértice v
            - Si el grafo es dirigido, out indica si se calcula el grado de
        salida o de entrada
        """
        if not self._directed:
            return len(list(self.incident_edges(v)))
        else:
            if out:
                return len(list(self.incident_edges(v)))
            else:
                return len(list(self.incident_edges(v, out=False)))

    def incident_edges(self, v, out=True):
        """Devuelve un iterador de las aristas incidentes al vértice v
            - Si el grafo es dirigido, out indica si se devuelven las aristas
        salientes o entrantes
        """
        if not self._directed:
            for node in v.incidence_collection:
                yield node.element()
        else:
            for node in v.incidence_collection:
                edge = node.element()
                if out:
                    if edge.u == v:
                        yield edge
                else:
                    if edge.v == v:
                        yield edge

    def insert_vertex(self, x=None):
        """Inserta un vértice con elemento x"""
        vertex = Vertex(x)
        self._vertices.add_last(vertex)
        return vertex

    def insert_edge(self, u, v, x=None, weight=0):
        """Inserta una arista que conecta los vértices u y v
        - x es el elemento que se almacena en la arista
        """
        edge = Edge(u, v, x, self._directed, weight)
        u.incidence_collection.add_last(edge)
        v.incidence_collection.add_last(edge)
        if not self._directed:
            self.edges_count += 1

        self.edges_count += 1
        return edge

    def remove_vertex(self, v):
        """Remueve el vértice v del grafo"""
        edges = set()
        for node in v.incidence_collection:
            edges.add(node.element())
        for edge in edges:
            self.remove_edge(edge)
        self._vertices.delete(v)

    def remove_edge(self, e):
        """Remueve la arista e del grafo"""
        e.u.incidence_collection.delete(e)
        e.v.incidence_collection.delete(e)
        if not self._directed:
            self.edges_count -= 1
        self.edges_count -= 1

    def dfs(self, u):
        """Realiza un recorrido DFS desde el vértice v"""
        discovered = {}
        self._dfs(u, discovered)
        return discovered

    def _dfs(self, u, discovered):
        """Realiza un recorrido DFS desde el vértice v"""
        for e in self.incident_edges(u):  # Para cada arista incidente a u
            v = e.opposite(u)
            if v not in discovered:  # v es un vértice no visitado
                discovered[v] = e  # e es la arista que se ha visitado desde v
                self._dfs(v, discovered)

    def bfs(self, u):
        discovered = {u: None}
        self._bfs(u, discovered)
        return discovered

    def _bfs(self, u, discovered):
        level = [u]
        while len(level) > 0:
            next_level = []
            for u in level:
                for e in self.incident_edges(u):
                    v = e.opposite(u)
                    if v not in discovered:
                        discovered[v] = e
                        next_level.append(v)
            level = next_level

    def dijkstra(self, s):
        d = {}  # d[v] almacenará la distancia más corta desde s hasta v
        cloud = {s: []}  # Inicializa cloud con el vértice origen y una lista vacía
        pq = SortedPriorityQueue()  # Vértices con distancias como clave

        for v in self.vertices():
            if v is s:
                d[v] = 0
            else:
                d[v] = float("inf")
            pq.add(d[v], v)

        while not pq.is_empty():
            key, u = pq.remove_min()
            for e in self.incident_edges(u):  # Vértices adyacentes a u
                v = e.opposite(u)
                if v not in cloud:
                    wgt = e.weight
                    if (
                        d[u] + wgt < d[v]
                    ):  # ¿Existe un camino más corto a v pasando por u?
                        d[v] = d[u] + wgt  # Actualiza la distancia de v
                        pq.add(d[v], v)  # Actualiza la cola de prioridad
                        cloud[v] = cloud[u] + [
                            e
                        ]  # Actualiza el árbol de caminos más cortos
        return cloud, d
