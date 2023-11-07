import flet as ft
from flet import *
from config.database import *
from flet_route import Routing, path, Params, Basket
from models.models import *

def petls(page:ft.Page,params:Params,basket:Basket):
    query = "SELECT pet.id, pet.id_owner, pet.name, pet.species, pet.race, pet.sex, pet.age, owner.name FROM pet JOIN owner ON pet.id_owner = owner.id"
    cursor.execute(query)
    pets_data = cursor.fetchall()
    pets = [Pet(id, id_owner, name, species, race, sex, age, owner_name) for (id, id_owner, name, species, race, sex, age, owner_name) in pets_data]

    rows = []
    for pet in pets:
        rows.append(ft.DataRow(cells=[
            ft.DataCell(ft.Text(str(pet.id))),
            ft.DataCell(ft.Text(pet.name)),
            ft.DataCell(ft.Text((pet.species))),
            ft.DataCell(ft.Text((pet.race))),
            ft.DataCell(ft.Text(pet.sex)),
            ft.DataCell(ft.Text(str(pet.age))),
            ft.DataCell(ft.Text(str(pet.id_owner))),
            ft.DataCell(ft.Text(pet.owner_name))
        ]))

    return ft.View(
        "/ownerls/petls",
        controls=[
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
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Pet ID"), numeric=True),
                    ft.DataColumn(ft.Text("Pet Name")),
                    ft.DataColumn(ft.Text("Species")),
                    ft.DataColumn(ft.Text("Race")),
                    ft.DataColumn(ft.Text("Sex")),
                    ft.DataColumn(ft.Text("age"), numeric=True),
                    ft.DataColumn(ft.Text("Owner ID"), numeric=True),
                    ft.DataColumn(ft.Text("Owner Name"))
                ],
                rows=rows,
            )

        ]
    )
