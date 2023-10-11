class Pet:

    def __init__(self, nombre, dni, especie, raza, sexo, edad, enferma=False):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.nombre = nombre
        self.dni = dni
        self.especie = especie
        self.raza = raza
        self.sexo = sexo
        self.edad = edad
        self.enferma = enferma

class Owner:

    def __init__(self, nombre, dni, numero, correo):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.nombre = nombre
        self.dni = dni
        self.numero = numero
        self.correo = correo

class Visit:

    def __init__(self, fecha, hora, motivo, descripcion, numero):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.descripcion = descripcion
        self.numero = numero

class User:

    def __init__(self, username, password):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.username = username
        self.password = password