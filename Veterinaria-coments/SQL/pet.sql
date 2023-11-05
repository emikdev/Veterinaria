-- Crear la tabla "pet"

CREATE TABLE pet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_veterinary INT,
    id_owner INT,
    name VARCHAR(16) NOT NULL,
    species VARCHAR(12) NOT NULL,
    race VARCHAR(32),
    sex CHAR(1) NOT NULL,
    age INT,
    FOREIGN KEY (id_veterinary) REFERENCES veterinary(id),
    FOREIGN KEY (id_owner) REFERENCES owner(id)
);

-- Insertar datos de ejemplo en la tabla "pet" haciendo referencia a registros existentes en "veterinary" y "owner"

INSERT INTO pet (id_owner, id_veterinary, name, species, race, sex, age)
VALUES
    ('1', '1', 'Obvi', 'Perro', 'Bull Terrier', 'M', '1');