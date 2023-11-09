# Se importan las librerias y paquetes necesarios
import flet as ft
from flet import *
from config.database import *
from flet_route import Routing, path, Params, Basket
from models.models import *

# Se define la funcion contenedora de la View
def petls(page:ft.Page,params:Params,basket:Basket):

    # Se recupera la id del usuario que se encuentra en el "Session Storage"
    veterinaryid = page.session.get("veterinaryid")

    # Se realiza la consulta en la base de datos para cargar la informacion de la mascota
    query = "SELECT pet.id, pet.id_owner, pet.name, pet.species, pet.race, pet.sex, pet.age, owner.name FROM pet JOIN owner ON pet.id_owner = owner.id WHERE pet.id_veterinary = %s"
    cursor.execute(query, (veterinaryid,))
    pets_data = cursor.fetchall()
    pets = [Pet(id, id_owner, name, species, race, sex, age, owner_name) for (id, id_owner, name, species, race, sex, age, owner_name) in pets_data]

    # Se crean las filas que se asignaran a la tabla
    rows = []
    for pet in pets:
        rows.append(ft.DataRow(cells=[
            # Se carga el contenido de la instancia de la clase Pet en las celdas correspondientes
            ft.DataCell(ft.Text(str(pet.id))),
            ft.DataCell(ft.Text(pet.name)),
            ft.DataCell(ft.Text((pet.species))),
            ft.DataCell(ft.Text((pet.race))),
            ft.DataCell(ft.Text(pet.sex)),
            ft.DataCell(ft.Text(str(pet.age))),
            ft.DataCell(ft.Text(str(pet.id_owner))),
            ft.DataCell(ft.Text(pet.owner_name))
        ]))

    # Se retorna el contenido de la View
    return ft.View(
        "/ownerls/petls",
        controls=[
            # Se define el contenido de la View
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, tooltip='Back to "Owner List"', on_click=lambda _: page.go("/ownerls")),
                title= Text("Pet List"),
                automatically_imply_leading=False,
                actions=[
                    ft.IconButton(icon=ft.icons.LIST_ALT, tooltip='Visit List', on_click=lambda _: page.go("/ownerls/petls/visitls")),
                    ft.IconButton(icon=ft.icons.APP_REGISTRATION, tooltip='Create Pet', on_click=lambda _: page.go("/ownerls/petls/createPet")),
                    ft.IconButton(icon=ft.icons.DELETE, tooltip='Delete Pet', on_click=lambda _: page.go("/ownerls/petls/deletePet"))
                ]
                ),
            # Se define la tabla
            ft.DataTable(
                columns=[
                    # Se definen las columnas de la tabla
                    ft.DataColumn(ft.Text("Pet ID"), numeric=True),
                    ft.DataColumn(ft.Text("Pet Name")),
                    ft.DataColumn(ft.Text("Species")),
                    ft.DataColumn(ft.Text("Race")),
                    ft.DataColumn(ft.Text("Sex")),
                    ft.DataColumn(ft.Text("age"), numeric=True),
                    ft.DataColumn(ft.Text("Owner ID"), numeric=True),
                    ft.DataColumn(ft.Text("Owner Name"))
                ],
                # Se cargan las filas que fueron creadas con anterioridad
                rows=rows,
            )

        ]
    )
