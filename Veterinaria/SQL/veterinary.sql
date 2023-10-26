-- Crear la tabla "veterinary"

CREATE TABLE veterinary (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(12) NOT NULL,
    password VARCHAR(12) NOT NULL
);

-- Insertar datos de ejemplo en la tabla "veterinary"

INSERT INTO veterinary (username, password)
VALUES
    ('usuario1', 'clave1'),
    ('usuario2', 'clave2'),
    ('usuario3', 'clave3');
