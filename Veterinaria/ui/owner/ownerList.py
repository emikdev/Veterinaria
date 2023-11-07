import flet as ft
from flet import *
from config.database import *
from flet_route import Routing, path, Params, Basket
from models.models import *

def ownerls(page:ft.Page,params:Params,basket:Basket):
    query = "SELECT owner.id, owner.name, owner.dni, owner.phone, owner.mail, pet.id AS pet_id, pet.name AS pet_name FROM owner JOIN pet ON owner.id = pet.id_owner"
    cursor.execute(query)
    owners_data = cursor.fetchall()
    owners = [Owner(id, name, dni, phone, mail, pet_id, pet_name) for (id, name, dni, phone, mail, pet_id, pet_name) in owners_data]

    rows = []
    for owner in owners:
        rows.append(ft.DataRow(cells=[
            ft.DataCell(ft.Text(str(owner.id))),
            ft.DataCell(ft.Text(owner.name)),
            ft.DataCell(ft.Text(str(owner.dni))),
            ft.DataCell(ft.Text(str(owner.phone))),
            ft.DataCell(ft.Text(owner.mail)),
            ft.DataCell(ft.Text(str(owner.pet_id))),
            ft.DataCell(ft.Text(owner.pet_name))
        ]))

    return ft.View(
        "/ownerls",
        controls=[
            ft.AppBar(
                leading=IconButton(icon=ft.icons.LOGOUT, tooltip='Logout', on_click=lambda _: page.go("/")),
                title= ft.Text("Owner List"),
                actions=[
                    ft.IconButton(icon=ft.icons.PETS, tooltip='Pet List', on_click=lambda _: page.go("/ownerls/petls")),
                    ft.IconButton(icon=ft.icons.APP_REGISTRATION, tooltip='Create Owner', on_click=lambda _: page.go("/ownerls/createOwner")),
                    ft.IconButton(icon=ft.icons.DELETE, tooltip='Delete Owner', on_click=lambda _: page.go("/ownerls/deleteOwner"))
                ]
                ),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("ID"), numeric=True),
                    ft.DataColumn(ft.Text("Full Name")),
                    ft.DataColumn(ft.Text("DNI"), numeric=True),
                    ft.DataColumn(ft.Text("Phone"), numeric=True),
                    ft.DataColumn(ft.Text("Email")),
                    ft.DataColumn(ft.Text("Pet ID"), numeric=True),
                    ft.DataColumn(ft.Text("Pet Name"))
                ],
                rows=rows,
            ),
        ],
    )