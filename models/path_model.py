from .connection import DatabaseConnection


class Path:
    def __init__(self, path_id, name, distance, origin_city, destination_city):
        self.path_id = path_id
        self.name = name
        self.distance = distance
        self.origin_city = origin_city
        self.destination_city = destination_city

    @classmethod
    def get_paths(cls, city):
        query = """SELECT path_id, name, distance, origin_city, destination_city 
            FROM BeerDistribution.paths WHERE origin_city = %s;"""
        result = DatabaseConnection.fetch_all(query, (city.city_id,))
        paths = []
        if result:
            for row in result:
                paths.append(cls(row[0], row[1], row[2], row[3], row[4]))
        return paths
