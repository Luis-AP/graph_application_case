from models.city_model import City

from graphs.mygraph import ADTGraph

from models.connection import DatabaseConnection
from config import Config

from utils import charge_vertices, charge_edges, search_vertex, total_weight, Route


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
        (cloud, distances) = graph.dijkstra(search_vertex(graph, branch.city_id))
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

    # Seleccionar las ciudades que no son sucursales
    non_branches = City.get_non_branches()
    # Creamos una copia de las mejores rutas para no modificarlas
    perfect_routes = best_routes.copy()
    # Para cada ciudad que no es sucursal
    for city in non_branches:
        # Creamos una copia de las mejores rutas
        routes = best_routes.copy()
        # Empleamos Dijkstra nuevamente
        # Suponemos que la ciudad seleccionada es una sucursal
        (cloud, distances) = graph.dijkstra(search_vertex(graph, city.city_id))
        # Actualizamos las rutas con la nueva información
        for vertex, distance in distances.items():
            route = Route(city, distance, cloud[vertex])
            if vertex not in routes.keys():
                routes[vertex] = route
            else:
                if route < routes[vertex]:
                    routes[vertex] = route
        # Si el peso total de las rutas es menor que el peso total que teníamos
        # antes de suponer que la ciudad seleccionada es una sucursal, entonces
        # actualizamos las rutas perfectas
        if total_weight(routes) < total_weight(perfect_routes):
            perfect_routes = routes.copy()
        # Guardamos las rutas tentativas en un archivo csv
        Route.to_csv(
            routes,
            file_name=f"paths/exercise02/{city.name}(weight={total_weight(routes)}).csv",
        )

    # Guardamos las rutas perfectas en un archivo csv
    Route.to_csv(
        perfect_routes,
        file_name=f"paths/exercise02/solution(weight={total_weight(perfect_routes)}).csv",
    )
