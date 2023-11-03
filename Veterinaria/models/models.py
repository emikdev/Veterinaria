class Pet:

    def __init__(self, id, name, species, race, sex, age):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.id = id
        self.name = name
        self.species = species
        self.race = race
        self.sex = sex
        self.age = age

class Owner:

    def __init__(self, id, name, dni, phone, mail):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.id = id
        self.name = name
        self.dni = dni
        self.phone = phone
        self.mail = mail

class Visit:

    def __init__(self, id, date, motive, description):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.id = id
        self.date = date
        self.motive = motive
        self.description = description

class User:

    def __init__(self, id, username, password):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.id = id
        self.username = username
        self.password = password