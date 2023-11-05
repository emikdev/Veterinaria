import flet as ft
from flet import *
from config.database import *
from flet_route import Routing, path, Params, Basket
from models.models import *

# Función para obtener la lista de visitas
def visitls(page:ft.Page,params:Params,basket:Basket):

    # Consulta SQL para recuperar los datos de las visitas
    query = """
        SELECT visit.id, visit.id_pet, visit.date, visit.reason, visit.description, pet.name
        FROM visit
        JOIN pet ON visit.id_pet = pet.id
    """

    # Ejecuta la consulta SQL
    cursor.execute(query)

    # Obtiene los datos de las visitas
    visits_data = cursor.fetchall()

    # Crea una lista de objetos Visit con los datos de las visitas
    visits = [Visit(id, id_pet, date, reason, description, pet_name) for (id, id_pet, date, reason, description, pet_name) in visits_data]

    # Crea una lista de filas para la tabla de datos
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

    # Devuelve la vista con la tabla de datos
    return ft.View(
        "/ownerls/petls/visitls",
        controls=[
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls/petls")),
                title= Text("Visit List"),
                automatically_imply_leading=False,
                actions=[
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda _: page.go("/ownerls/petls/visitls/deleteVisit")),
                    ft.ElevatedButton("Create Visit", on_click=lambda _: page.go("/ownerls/petls/visitls/createVisit")),
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

