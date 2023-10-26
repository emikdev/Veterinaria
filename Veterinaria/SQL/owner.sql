-- Crear la tabla "owner"

CREATE TABLE owner (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_veterinary INT,
    name VARCHAR(32) NOT NULL,
    dni VARCHAR(8) NOT NULL,
    phone VARCHAR(21) NOT NULL,
    mail VARCHAR(64) NOT NULL,
    FOREIGN KEY (id_veterinary) REFERENCES veterinary(id)
);

-- Insertar datos de ejemplo en la tabla "owner" sin proporcionar un valor para "id_veterinary"

INSERT INTO owner (name, dni, phone, mail)
VALUES
    ('Dueño 1', '123456789', '555-123-4567', 'dueno1@example.com'),
    ('Dueño 2', '987654321', '555-987-6543', 'dueno2@example.com'),
    ('Dueño 3', '111222333', '555-111-2223', 'dueno3@example.com');
