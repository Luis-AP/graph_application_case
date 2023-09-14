from dotenv import dotenv_values


class Config:
    config = dotenv_values(".env")

    DATABASE_USERNAME = config["DATABASE_USERNAME"]
    DATABASE_PASSWORD = config["DATABASE_PASSWORD"]
    DATABASE_HOST = config["DATABASE_HOST"]
    DATABASE_PORT = config["DATABASE_PORT"]
