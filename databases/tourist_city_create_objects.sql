-- Create the database
CREATE DATABASE TouristCity;

-- Use the created database
USE TouristCity;

-- Create the table for tourist sites
CREATE TABLE tourist_sites (
    site_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    is_popular BOOLEAN,
    zip_code INT,
    visitors_per_year INT
);

-- Create the table for paths
CREATE TABLE paths (
    path_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    distance INT,
    origin_site INT,
    destination_site INT,
    FOREIGN KEY (origin_site) REFERENCES tourist_sites(site_id),
    FOREIGN KEY (destination_site) REFERENCES tourist_sites(site_id)
);
