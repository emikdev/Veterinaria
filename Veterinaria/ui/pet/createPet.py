import flet as ft
from flet import *
from config.database import *
from models.models import *
from flet_route import Params,Basket

def createPet(page:ft.Page,params:Params,basket:Basket):
    ownerid = ft.TextField(hint_text="Owner ID")
    name = ft.TextField(hint_text="Name")
    species = ft.TextField(hint_text="Species")
    race = ft.TextField(hint_text="Race")
    sex = ft.TextField(hint_text="Sex")
    age = ft.TextField(hint_text="Age")

    def create_pet(e):
        # Obtener los valores de los campos de texto
        ownerid_value = ownerid.value
        name_value = name.value
        species_value = species.value
        race_value = race.value
        sex_value = sex.value
        age_value = age.value

        # Insertar los valores en la tabla "owner"
        query = f"INSERT INTO pet (id_owner, name, species, race, sex, age) VALUES ('{ownerid_value}', '{name_value}', '{species_value}', '{race_value}', '{sex_value}', '{age_value}')"
        cursor.execute(query)
        conn.commit()

        # Redirigir a la página de lista de propietarios
        page.go("/ownerls/petls")

    return ft.View(
        "/ownerls/petls/createPet",
        controls=[
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls/petls")),
                title= Text("Create Pet"),
                automatically_imply_leading=False,
                ),
            ownerid,
            name,
            species,
            race,
            sex,
            age,
            ft.ElevatedButton("Create Pet", on_click=create_pet)
        ]
    )