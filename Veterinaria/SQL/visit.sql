-- Crear la tabla "Visit"

CREATE TABLE Visit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_veterinary INT,
    id_pet INT,
    date DATE NOT NULL,
    reason VARCHAR(100) NOT NULL,
    description TEXT,
    FOREIGN KEY (id_veterinary) REFERENCES veterinary(id),
    FOREIGN KEY (id_pet) REFERENCES pet(id)
);

-- Insertar datos de ejemplo en la tabla "Visit" haciendo referencia a registros existentes en "veterinary" y "pet"

INSERT INTO Visit (date, reason, description)
VALUES
    ('2023-10-25', 'Control de rutina', 'Sin observaciones.'),
    ('2023-10-26', 'Vacunación anual', 'Buena salud general.'),
    ('2023-10-27', 'Tratamiento dental', 'Sin complicaciones.');
