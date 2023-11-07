import flet as ft
from flet import *
from config.database import *
from flet_route import Routing, path, Params, Basket
from models.models import *

def visitls(page:ft.Page,params:Params,basket:Basket):
    query = "SELECT visit.id, visit.id_pet, visit.date, visit.reason, visit.description, pet.name FROM visit JOIN pet ON visit.id_pet = pet.id"
    cursor.execute(query)
    visits_data = cursor.fetchall()
    visits = [Visit(id, id_pet, date, reason, description, pet_name) for (id, id_pet, date, reason, description, pet_name) in visits_data]

    rows = []
    for visit in visits:
        rows.append(ft.DataRow(cells=[
            ft.DataCell(ft.Text(str(visit.id))),
            ft.DataCell(ft.Text(visit.date)),
            ft.DataCell(ft.Text(visit.reason)),
            ft.DataCell(ft.Text(visit.description)),
            ft.DataCell(ft.Text(str(visit.id_pet))),
            ft.DataCell(ft.Text(visit.pet_name))
        ]))

    return ft.View(
        "/ownerls/petls/visitls",
        controls=[
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, tooltip='Back to "Pet List"', on_click=lambda _: page.go("/ownerls/petls")),
                title= Text("Visit List"),
                automatically_imply_leading=False,
                actions=[
                    ft.IconButton(icon=ft.icons.APP_REGISTRATION, tooltip='Create Visit', on_click=lambda _: page.go("/ownerls/petls/visitls/createVisit")),
                    ft.IconButton(icon=ft.icons.DELETE, tooltip='Delete Visit', on_click=lambda _: page.go("/ownerls/petls/visitls/deleteVisit"))
                ]
                ),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Visit ID"), numeric=True),
                    ft.DataColumn(ft.Text("Date")),
                    ft.DataColumn(ft.Text("Motive")),
                    ft.DataColumn(ft.Text("Description")),
                    ft.DataColumn(ft.Text("Pet ID")),
                    ft.DataColumn(ft.Text("Pet Name"))
                ],
                rows=rows,
            )
        ]
    )
