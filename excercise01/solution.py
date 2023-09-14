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
    # Creamos un diccionario donde cada clave es un vértice del grafo y cada
    # valor es una ruta desde la sucursal más cercana a ese vértice
    best_routes = {}
    for branch in branches:
        # Dijkstra retorna una tupla con dos diccionarios, el primero contiene
        # el camino más corto desde el vértice de partida hasta cada uno de los
        # vértices del grafo, el segundo contiene la distancia desde el vértice
        (cloud, distances) = graph.dijkstra(seach_vertex(graph, branch.city_id))
        for vertex, distance in distances.items():
            # Creamos una ruta con la sucursal seleccionada como partida, la
            # distancia desde la sucursal hasta el vértice y el camino desde la
            # sucursal hasta el vértice
            route = Route(branch, distance, cloud[vertex])
            if vertex not in best_routes.keys():
                best_routes[vertex] = route
            else:
                # Actualizamos la ruta si la distancia desde otra sucursal es menor
                # que la distancia desde la sucursal seleccionada
                if route < best_routes[vertex]:
                    best_routes[vertex] = route

    Route.to_csv(best_routes, file_name=f"paths/excercise01/solution.csv")
