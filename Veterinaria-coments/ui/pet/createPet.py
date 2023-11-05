import flet as ft
from flet import *
from config.database import *
from models.models import *
from flet_route import Params, Basket

# Define una función para crear una nueva mascota
def createPet(page:ft.Page,params:Params,basket:Basket):
    # Crea campos de texto para recopilar información de la mascota
    ownerid = ft.TextField(hint_text="ID del propietario")
    name = ft.TextField(hint_text="Nombre")
    species = ft.TextField(hint_text="Especie")
    race = ft.TextField(hint_text="Raza")
    sex = ft.TextField(hint_text="Sexo")
    age = ft.TextField(hint_text="Edad")

    # Define una función de devolución de llamada para manejar el clic del botón "Crear mascota"
    def create_pet(e):
        # Obtén los valores de los campos de texto
        ownerid_value = ownerid.value
        name_value = name.value
        species_value = species.value
        race_value = race.value
        sex_value = sex.value
        age_value = age.value

        # Construye la consulta SQL para insertar los datos de la mascota en la tabla "pet"
        query = f"INSERT INTO pet (id_owner, name, species, race, sex, age) VALUES ('{ownerid_value}', '{name_value}', '{species_value}', '{race_value}', '{sex_value}', '{age_value}')"

        # Ejecuta la consulta para insertar los datos de la mascota en la base de datos
        cursor.execute(query)
        conn.commit()

        # Redirige al usuario a la página de lista de mascotas
        page.go("/ownerls/petls")

    # Crea la vista para la página "Crear mascota"
    return ft.View(
        "/ownerls/petls/createPet",
        controls=[
            # Agrega una barra de aplicaciones con un botón de retroceso y título
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls/petls")),
                title= Text("Crear mascota"),
                automatically_imply_leading=False,
            ),

            # Agrega los campos de texto para nombre, especie, raza, sexo y edad de la mascota
            ownerid,
            name,
            species,
            race,
            sex,
            age,

            # Agrega un botón elevado con la etiqueta "Crear mascota" y la función de devolución de llamada adjunta
            ft.ElevatedButton("Crear mascota", on_click=create_pet)
        ]
    )
