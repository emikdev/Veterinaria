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

INSERT INTO owner (id_veterinary, name, dni, phone, mail)
VALUES
    ('1', 'Theo Molina', '45779189', '+54 911 6692-2713', 'TheoMolina12@gmail.com');