from .connection import DatabaseConnection


class City:
    def __init__(self, city_id, name, is_branch, zip_code, population):
        self.city_id = city_id
        self.name = name
        self.is_branch = is_branch
        self.zip_code = zip_code
        self.population = population

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all(cls):
        query = """SELECT city_id, name, is_branch, zip_code, population FROM BeerDistribution.cities;"""
        result = DatabaseConnection.fetch_all(query)
        cities = []
        if result:
            for row in result:
                cities.append(cls(row[0], row[1], row[2], row[3], row[4]))
        return cities

    @classmethod
    def get_branches(cls):
        query = """SELECT city_id, name, is_branch, zip_code, population FROM BeerDistribution.cities WHERE is_branch = 1;"""
        result = DatabaseConnection.fetch_all(query)
        cities = []
        if result:
            for row in result:
                cities.append(cls(row[0], row[1], row[2], row[3], row[4]))
        return cities

    @classmethod
    def get_non_branches(cls):
        query = """SELECT city_id, name, is_branch, zip_code, population FROM BeerDistribution.cities WHERE is_branch = 0;"""
        result = DatabaseConnection.fetch_all(query)
        cities = []
        if result:
            for row in result:
                cities.append(cls(row[0], row[1], row[2], row[3], row[4]))
        return cities

    @classmethod
    def update_to_branch(cls, city):
        query = f"""UPDATE BeerDistribution.cities SET is_branch = 1 WHERE city_id = {city.city_id};"""
        DatabaseConnection.execute_query(query)
