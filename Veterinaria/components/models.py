class Pet:

    def __init__(self, id, nombre, especie, raza, sexo, edad):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.sexo = sexo
        self.edad = edad

class Owner:

    def __init__(self, id, nombre, dni, numero, correo):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.id = id
        self.nombre = nombre
        self.dni = dni
        self.numero = numero
        self.correo = correo

class Visit:

    def __init__(self, id, fecha, hora, motivo, descripcion, numero):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.id = id
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.descripcion = descripcion
        self.numero = numero

class User:

    def __init__(self, id, username, password):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.id = id
        self.username = username
        self.password = password
