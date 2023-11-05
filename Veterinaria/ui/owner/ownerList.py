import flet as ft
from flet import *
from config.database import *
from flet_route import Routing, path, Params, Basket
from models.models import *

def ownerls(page:ft.Page,params:Params,basket:Basket):
    query = "SELECT id, name, dni, phone, mail FROM owner"
    cursor.execute(query)
    owners_data = cursor.fetchall()
    owners = [Owner(id, name, dni, phone, mail) for (id, name, dni, phone, mail) in owners_data]

    rows = []
    for owner in owners:
        rows.append(ft.DataRow(cells=[
            ft.DataCell(ft.Text(str(owner.id))),
            ft.DataCell(ft.Text(owner.name)),
            ft.DataCell(ft.Text(str(owner.dni))),
            ft.DataCell(ft.Text(str(owner.phone))),
            ft.DataCell(ft.Text(owner.mail))
        ]))

    return ft.View(
        "/ownerls",
        controls=[
            ft.AppBar(
                leading=IconButton(icon=ft.icons.REFRESH),
                title= Text("Owner List"),
                automatically_imply_leading=False,
                actions=[
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda _: page.go("/ownerls/deleteOwner")),
                    ft.ElevatedButton("Pet List", on_click=lambda _: page.go("/ownerls/petls")),
                    ft.ElevatedButton("Create Owner", on_click=lambda _: page.go("/ownerls/createOwner")),
                    ft.ElevatedButton("Logout", on_click=lambda _: page.go("/")),
                ]
                ),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("ID"), numeric=True),
                    ft.DataColumn(ft.Text("Full Name")),
                    ft.DataColumn(ft.Text("DNI"), numeric=True),
                    ft.DataColumn(ft.Text("Phone"), numeric=True),
                    ft.DataColumn(ft.Text("Email"))
                ],
                rows=rows,
            ),
        ],
    )