from models.city_model import City
from models.path_model import Path

import csv

import os


def charge_vertices(graph):
    """Carga los vértices en un grafo desde la base de datos"""
    cities = City.get_all()
    for city in cities:
        graph.insert_vertex(city)


def charge_edges(graph, vertex):
    """Carga las aritas en un grafo desde la base de datos"""
    paths = Path.get_paths(vertex.element)
    for path in paths:
        destination_vertex = seach_vertex(graph, path.destination_city)
        if destination_vertex:
            graph.insert_edge(vertex, destination_vertex, path.name, path.distance)


def seach_vertex(graph, city_id):
    """Busca un vértice en un grafo por su id"""
    for vertex in graph.vertices():
        if vertex.element.city_id == city_id:
            return vertex
    return None


def total_weight(routes):
    """Calcula el peso total de una lista de rutas"""
    total_weight = 0
    for route in routes.values():
        total_weight += route.distance
    return total_weight


class Route:
    """Representa una ruta desde una sucursal hasta un vértice del grafo"""

    def __init__(self, branch, distance, path):
        """Constructor de la clase
        Atributos:
            branch (City): Sucursal de partida
            distance (float): Distancia desde la sucursal hasta el vértice
            path (list): Camino desde la sucursal hasta el vértice
        """

        self.branch = branch
        self.distance = distance
        self.path = path

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __eq__(self, other):
        return self.distance == other.distance

    @classmethod
    def to_csv(cls, routes, file_name="paths/paths.csv"):
        """Guarda una lista de rutas en un archivo csv"""
        if os.path.exists("paths"):
            with open(file_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["Destino", "Sucursal de Partida", "Distancia (km)", "Recorrido"]
                )
                for vertex, route in routes.items():
                    row = []
                    row.append(vertex.element.name)
                    row.append(route.branch.name)
                    row.append(route.distance)
                    path = []
                    if len(route.path) > 0:
                        for edge in route.path:
                            path.append(str(edge))
                    else:
                        path.append("No hay recorrido")
                    row.append(" -> ".join(path))
                    writer.writerow(row)
        else:
            os.mkdir("paths")
            os.mkdir("paths/exercise01")
            os.mkdir("paths/exercise02")
            cls.to_csv(routes, file_name)
