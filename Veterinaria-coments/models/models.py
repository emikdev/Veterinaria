class Pet:

    def __init__(self, id, id_owner, name, species, race, sex, age, owner_name):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.id = id
        self.name = name
        self.species = species
        self.race = race
        self.sex = sex
        self.age = age
        self.id_owner = id_owner
        self.owner_name = owner_name

class Owner:

    def __init__(self, id, name, dni, phone, mail):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.id = id
        self.name = name
        self.dni = dni
        self.phone = phone
        self.mail = mail

class Visit:

    def __init__(self, id, id_pet, date, reason, description, pet_name):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.id = id
        self.id_pet = id_pet
        self.date = date
        self.reason = reason
        self.description = description
        self.pet_name = pet_name

class veterinary:

    def __init__(self, id, username, password):
        # Inicializa una instancia de Mascota con los atributos proporcionados
        self.id = id
        self.username = username
        self.password = password