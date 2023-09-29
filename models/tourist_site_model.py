from .connection import DatabaseConnection


class TouristSite:
    def __init__(self, site_id, name, is_popular, zip_code, visitors_per_year):
        self.site_id = site_id
        self.name = name
        self.is_popular = is_popular
        self.zip_code = zip_code
        self.visitors_per_year = visitors_per_year

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all(cls):
        query = """SELECT site_id, name, is_popular, zip_code, visitors_per_year FROM TouristCity.tourist_sites;"""
        result = DatabaseConnection.fetch_all(query)
        sites = []
        if result:
            for row in result:
                sites.append(cls(row[0], row[1], row[2], row[3], row[4]))
        return sites
