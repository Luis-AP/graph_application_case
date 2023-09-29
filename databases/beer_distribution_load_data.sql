-- Insertar ciudades en la tabla de ciudades
INSERT INTO cities (name, is_branch, zip_code, population) VALUES
('Bogotá', TRUE, 110111, 7000000),-- 1
('Cali', TRUE, 760001, 2200000),-- 2
('Medellín', TRUE, 500001, 2500000),-- 3
('Barranquilla', FALSE, 800001, 1200000),-- 4
('Cartagena', FALSE, 130001, 900000),-- 5
('Cúcuta', FALSE, 540001, 600000),-- 6
('Bucaramanga', FALSE, 680001, 1000000),-- 7
('Pereira', FALSE, 660001, 450000),-- 8
('Santa Marta', FALSE, 470001, 400000),-- 9
('Ibagué', FALSE, 730001, 500000),-- 10
('Pasto', FALSE, 520001, 300000),-- 11
('Manizales', FALSE, 170001, 350000),-- 12
('Neiva', FALSE, 410001, 320000),-- 13
('Villavicencio', FALSE, 500001, 380000),-- 14
('Armenia', FALSE, 630001, 280000);-- 15
-- Original paths
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Bogotá-Medellín', 419, 1, 3);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Bogotá-Barranquilla', 1005, 1, 4);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Bogotá-Bucaramanga', 409, 1, 7);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Bogotá-Ibagué', 193, 1, 10);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Bogotá-Villavicencio', 110, 1, 14);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Bogotá-Neiva', 301, 1, 13);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Bogotá-Manizales', 318, 1, 12);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Bogotá-Santa Marta', 968, 1, 9);

INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Medellín-Barranquilla', 704, 3, 4);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Medellín-Cartagena', 659, 3, 5);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Medellín-Bucaramanga', 392, 3, 7);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Medellín-Pereira', 224, 3, 8);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Medellín-Manizales', 209, 3, 12);

INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Cali-Pereira', 215, 2, 8); 
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Cali-Pasto', 393, 2, 11);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Cali-Neiva', 382, 2, 13);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Cali-Armenia', 187, 2, 15);

INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Barranquilla-Cartagena', 122, 4, 5);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Barranquilla-Santa Marta', 102, 4, 9);

INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Cúcuta-Bucaramanga', 200, 6, 7);

INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Bucaramanga-Santa Marta', 602, 7, 9);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Bucaramanga-Barranquilla', 643, 7, 4);

INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Pereira-Manizales', 54, 8, 12);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Pereira-Armenia', 53, 8, 15);

INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Santa Marta-Manizales', 964, 9, 12);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Santa Marta-Ibagué', 951, 9, 10);

INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Ibagué-Armenia', 86, 10, 15);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Ibagué-Neiva', 206, 10, 13);

INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Pasto-Neiva', 464, 11, 13);

-- Returning paths
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Medellín-Bogotá',  419,  3,  1);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Barranquilla-Bogotá',  1005,  4,  1);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Bucaramanga-Bogotá',  409,  7,  1);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Ibagué-Bogotá',  193,  10,  1);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Villavicencio-Bogotá',  110,  14,  1);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Neiva-Bogotá',  301,  13,  1);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Manizales-Bogotá',  318,  12,  1);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Santa Marta-Bogotá',  968,  9,  1);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Barranquilla-Medellín',  704,  4,  3);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Cartagena-Medellín',  659,  5,  3);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Bucaramanga-Medellín',  392,  7,  3);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Pereira-Medellín',  224,  8,  3);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Manizales-Medellín',  209,  12,  3);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Pereira-Cali',  215,  8,  2);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Pasto-Cali',  393,  11,  2);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Neiva-Cali',  382,  13,  2);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Armenia-Cali',  187,  15,  2);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Cartagena-Barranquilla',  122,  5,  4);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Santa Marta-Barranquilla',  102,  9,  4);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Bucaramanga-Cúcuta',  200,  7,  6);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Santa Marta-Bucaramanga',  602,  9,  7);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Barranquilla-Bucaramanga',  643,  4,  7);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Manizales-Pereira',  54,  12,  8);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Armenia-Pereira',  53,  15,  8);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Manizales-Santa Marta',  964,  12,  9);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Ibagué-Santa Marta',  951,  10,  9);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Armenia-Ibagué',  86,  15,  10);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Neiva-Ibagué',  206,  13,  10);
INSERT INTO paths (name, distance, origin_city, destination_city) VALUES ('Neiva-Pasto',  464,  13,  11);