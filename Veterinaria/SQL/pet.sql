-- Crear la tabla "pet"

CREATE TABLE pet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_veterinary INT,
    id_owner INT,
    name VARCHAR(16) NOT NULL,
    species VARCHAR(12) NOT NULL,
    race VARCHAR(32),
    sex CHAR(1) NOT NULL,
    FOREIGN KEY (id_veterinary) REFERENCES veterinary(id),
    FOREIGN KEY (id_owner) REFERENCES owner(id)
);

-- Insertar datos de ejemplo en la tabla "pet" haciendo referencia a registros existentes en "veterinary" y "owner"

INSERT INTO pet (name, species, race, sexo)
VALUES
    ('Mascota 1', 'Perro', 'Golden Retriever', 'M'),
    ('Mascota 2', 'Gato', 'Siamés', 'F'),
    ('Mascota 3', 'Perro', 'Labrador', 'M');
