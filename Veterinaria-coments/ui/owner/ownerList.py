import flet as ft
from flet import *
from config.database import *
from flet_route import Routing, path, Params, Basket
from models.models import *

def ownerls(page:ft.Page,params:Params,basket:Basket):
    # Ejecuta la consulta SQL para obtener los datos de los propietarios
    query = "SELECT id, name, dni, phone, mail FROM owner"
    cursor.execute(query)

    # Obtiene los datos de los propietarios de la base de datos
    owners_data = cursor.fetchall()

    # Crea instancias de la clase Owner para cada propietario
    owners = [Owner(id, name, dni, phone, mail) for (id, name, dni, phone, mail) in owners_data]

    # Crea filas de tabla para cada propietario
    rows = []
    for owner in owners:
        rows.append(ft.DataRow(cells=[
            ft.DataCell(ft.Text(str(owner.id))),
            ft.DataCell(ft.Text(owner.name)),
            ft.DataCell(ft.Text(str(owner.dni))),
            ft.DataCell(ft.Text(str(owner.phone))),
            ft.DataCell(ft.Text(owner.mail))
        ]))

    # Crea la vista de la página de lista de propietarios
    return ft.View(
        "/ownerls",
        controls=[
            # Agrega una barra de aplicaciones con un botón de refrescar, título y acciones
            ft.AppBar(
                leading=IconButton(icon=ft.icons.REFRESH),
                title= Text("Lista de propietarios"),
                automatically_imply_leading=False,
                actions=[
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda _: page.go("/ownerls/deleteOwner")),
                    ft.ElevatedButton("Lista de mascotas", on_click=lambda _: page.go("/ownerls/petls")),
                    ft.ElevatedButton("Crear propietario", on_click=lambda _: page.go("/ownerls/createOwner")),
                    ft.ElevatedButton("Cerrar sesión", on_click=lambda _: page.go("/")),
                ]
                ),

            # Agrega una tabla de datos para mostrar la lista de propietarios
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("ID"), numeric=True),
                    ft.DataColumn(ft.Text("Nombre completo")),
                    ft.DataColumn(ft.Text("DNI"), numeric=True),
                    ft.DataColumn(ft.Text("Teléfono"), numeric=True),
                    ft.DataColumn(ft.Text("Correo electrónico"))
                ],
                rows=rows,
            ),
        ],
    )
