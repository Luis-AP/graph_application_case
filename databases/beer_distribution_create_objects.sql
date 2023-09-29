-- Crear la base de datos
CREATE DATABASE BeerDistribution;

-- Usar la base de datos creada
USE BeerDistribution;

-- Crear la tabla de ciudades
CREATE TABLE cities (
    city_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    is_branch BOOLEAN,
    zip_code INT,
    population INT
);

-- Crear la tabla de caminos
CREATE TABLE paths (
    path_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    distance INT,
    origin_city INT,
    destination_city INT,
    FOREIGN KEY (origin_city) REFERENCES cities(city_id),
    FOREIGN KEY (destination_city) REFERENCES cities(city_id)
);
