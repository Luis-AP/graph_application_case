from models.city_model import City

from graphs.mygraph import ADTGraph

from models.connection import DatabaseConnection
from config import Config

from utils import charge_vertices, charge_edges, seach_vertex, Route

if __name__ == "__main__":
    DatabaseConnection.set_config(Config)
    graph = ADTGraph(directed=True)
    charge_vertices(graph)
    for vertex in graph.vertices():
        charge_edges(graph, vertex)

    # Seleccionar las sucursales de la base de datos
    branches = City.get_branches()
    # Creamos una lista de diccionarios, donde cada diccionario contiene
    # una ruta desde la sucursal seleccionada hasta cada una de las ciudades
    all_routes = []
    for city in branches:
        route = {}

        # Dijkstra retorna una tupla con dos diccionarios, el primero contiene
        # el camino más corto desde el vértice de partida hasta cada uno de los
        # vértices del grafo, el segundo contiene la distancia desde el vértice
        (cloud, distances) = graph.dijkstra(seach_vertex(graph, city.city_id))
        for vertex, distance in distances.items():
            # Creamos una ruta con la sucursal seleccionada como partida, la
            # distancia desde la sucursal hasta el vértice y el camino desde la
            # sucursal hasta el vértice
            route[vertex] = Route(city, distance, cloud[vertex])
        # Agregamos la ruta a la lista de rutas
        all_routes.append(route)

    # Guardamos las rutas en archivos csv
    for index, routes in enumerate(all_routes):
        Route.to_csv(
            routes,
            file_name=f"paths/exercise01/path_branch_{branches[index].name}.csv",
        )
