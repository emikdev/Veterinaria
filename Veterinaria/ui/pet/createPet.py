# Se importan las librerias y paquetes necesarios
import flet as ft
from flet import *
from config.database import *
from models.models import *
from flet_route import Params,Basket

# Se define la funcion contenedora de la View
def createPet(page:ft.Page,params:Params,basket:Basket):

    # Se recupera la id del usuario guardad en el "Sesion Storage"
    veterinaryid = page.session.get("veterinaryid")

    # Se definen la variables globales e inpust que se utilizara en la View y el Query
    global vetid_value
    ownerid = ft.TextField(hint_text="Owner ID")
    name = ft.TextField(hint_text="Name")
    species = ft.TextField(hint_text="Species")
    race = ft.TextField(hint_text="Race")
    sex = ft.TextField(hint_text="Sex")
    age = ft.TextField(hint_text="Age")

    # Se crea la funcion encargada de insertar los datos en la BD
    def create_pet(e):

        # Se obtienen los valores de los campos de texto
        vetid_value = veterinaryid
        ownerid_value = ownerid.value
        name_value = name.value
        species_value = species.value
        race_value = race.value
        sex_value = sex.value
        age_value = age.value

        # Se insertan los valores en la tabla "owner"
        query = f"INSERT INTO pet (id_veterinary, id_owner, name, species, race, sex, age) VALUES ('{vetid_value}', '{ownerid_value}', '{name_value}', '{species_value}', '{race_value}', '{sex_value}', '{age_value}')"
        cursor.execute(query)
        conn.commit()

        # Se redirige al usuario a la interface "Pet-list"
        page.go("/ownerls/petls")

    # Se retorna el contenido de la View
    return ft.View(
        "/ownerls/petls/createPet",
        controls=[
            # Se define el contenido de la View
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, tooltip='Back to "Pet List"', on_click=lambda _: page.go("/ownerls/petls")),
                title= Text("Create Pet"),
                automatically_imply_leading=False,
                ),
            ft.Text("Please make sure that the pet owner is already registered on the Owners list before registering a pet", size=10, color='#FFA500'),
            ownerid,
            name,
            species,
            race,
            sex,
            age,
            ft.ElevatedButton("Create Pet", on_click=create_pet)
        ]
    )