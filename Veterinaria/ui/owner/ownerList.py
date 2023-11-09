# Se importan la librerias y paquetes necesarios
import flet as ft
import flet_route
from flet import *
from flet_route import Routing, path, Params, Basket
from config.database import *
from models.models import *

# Se define la funcion contenedora de la View
def ownerls(page:ft.Page,params:Params,basket:Basket):

    # Se recupera la id del usuario almacenada en el "Sesion Storage"
    veterinaryid = page.session.get("veterinaryid")

    # Se realiza la consulta de la base de datos para cargar la informacion de los Dueños
    query = "SELECT owner.id, owner.name, owner.dni, owner.phone, owner.mail FROM owner WHERE owner.id_veterinary = %s"
    cursor.execute(query, (veterinaryid,))
    owners_data = cursor.fetchall()
    owners = [Owner(id, name, dni, phone, mail) for (id, name, dni, phone, mail) in owners_data]

    # Se crean las filas que se asignaran a la tabla
    rows = []
    for owner in owners:
        rows.append(ft.DataRow(cells=[
            # Se carga el contenido de la instancia de la clase Owner en las celdas correspondientes
            ft.DataCell(ft.Text(str(owner.id))),
            ft.DataCell(ft.Text(owner.name)),
            ft.DataCell(ft.Text(str(owner.dni))),
            ft.DataCell(ft.Text(str(owner.phone))),
            ft.DataCell(ft.Text(owner.mail))
        ]))

    # Se retorna el contenido de la view
    return ft.View(
        "/ownerls",
        controls=[
            # Se define el contenido de la View
            ft.AppBar(
                leading=IconButton(icon=ft.icons.LOGOUT, tooltip='Logout', on_click=lambda _: page.go("/")),
                title= ft.Text("Owner List"),
                actions=[
                    ft.IconButton(icon=ft.icons.PETS, tooltip='Pet List', on_click=lambda _: page.go("/ownerls/petls")),
                    ft.IconButton(icon=ft.icons.APP_REGISTRATION, tooltip='Create Owner', on_click=lambda _: page.go("/ownerls/createOwner")),
                    ft.IconButton(icon=ft.icons.DELETE, tooltip='Delete Owner', on_click=lambda _: page.go("/ownerls/deleteOwner"))
                ]
                ),
            # Se define la tabla
            ft.DataTable(
                columns=[
                    # Se definen las columnas de la tabla
                    ft.DataColumn(ft.Text("ID"), numeric=True),
                    ft.DataColumn(ft.Text("Full Name")),
                    ft.DataColumn(ft.Text("DNI"), numeric=True),
                    ft.DataColumn(ft.Text("Phone"), numeric=True),
                    ft.DataColumn(ft.Text("Email"))
                ],
                # Se cargan las filas que fueron creadas con anterioridad
                rows=rows,
            ),
        ],
    )