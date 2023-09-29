from models.city_model import City

from graphs.tsp import TSP

from models.connection import DatabaseConnection
from config import Config

from utils import charge_sites_as_vertices, charge_site_edges, TouristRoute

if __name__ == "__main__":
    DatabaseConnection.set_config(Config)
    graph = TSP(directed=True)

    charge_sites_as_vertices(graph)
    for vertex in graph.vertices():
        charge_site_edges(graph, vertex)

    start_vertex = list(graph.vertices())[0]
    solution = graph.nearest_neighbor_tsp(start_vertex)

    routes = []
    for site in solution:
        routes.append(site)

    TouristRoute.to_csv(routes, "paths/exercise03/nearest_neighbor_tsp.csv")
