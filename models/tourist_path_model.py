from .connection import DatabaseConnection


class TouristPath:
    def __init__(self, path_id, name, distance, origin_site, destination_site):
        self.path_id = path_id
        self.name = name
        self.distance = distance
        self.origin_site = origin_site
        self.destination_site = destination_site

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all(cls):
        query = """SELECT path_id, name, distance, origin_site, destination_site 
            FROM TouristCity.paths;"""
        result = DatabaseConnection.fetch_all(query)
        paths = []
        if result:
            for row in result:
                paths.append(cls(row[0], row[1], row[2], row[3], row[4]))
        return paths
