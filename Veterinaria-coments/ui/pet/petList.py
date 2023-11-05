import flet as ft
from flet import *
from config.database import *
from flet_route import Routing, path, Params, Basket
from models.models import *

def petls(page:ft.Page,params:Params,basket:Basket):

    # Ejecuta la consulta SQL para obtener los datos de las mascotas
    query = "SELECT pet.id, pet.id_owner, pet.name, pet.species, pet.race, pet.sex, pet.age, owner.name FROM pet JOIN owner ON pet.id_owner = owner.id"
    cursor.execute(query)

    # Obtiene los datos de las mascotas de la base de datos
    pets_data = cursor.fetchall()

    # Crea instancias de la clase Pet para cada registro de mascota
    pets = [Pet(id, id_owner, name, species, race, sex, age, owner_name) for (id, id_owner, name, species, race, sex, age, owner_name) in pets_data]

    # Crea filas de tabla para cada mascota
    rows = []
    for pet in pets:
        rows.append(ft.DataRow(cells=[
            ft.DataCell(ft.Text(str(pet.id))),
            ft.DataCell(ft.Text(pet.name)),
            ft.DataCell(ft.Text(pet.species)),
            ft.DataCell(ft.Text(pet.race)),
            ft.DataCell(ft.Text(pet.sex)),
            ft.DataCell(ft.Text(str(pet.age))),
            ft.DataCell(ft.Text(str(pet.id_owner))),
            ft.DataCell(ft.Text(pet.owner_name))
        ]))

    # Crea la vista para la página de lista de mascotas
    return ft.View(
        "/ownerls/petls",
        controls=[
            # Agrega una barra de aplicaciones con un botón de retroceso, título y acciones
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls")),
                title= Text("Lista de mascotas"),
                automatically_imply_leading=False,
                actions=[
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda _: page.go("/ownerls/petls/deletePet")),
                    ft.ElevatedButton("Lista de visitas", on_click=lambda _: page.go("/ownerls/petls/visitls")),
                    ft.ElevatedButton("Crear mascota", on_click=lambda _: page.go("/ownerls/petls/createPet"))
                ]
            ),

            # Agrega una tabla de datos para mostrar la lista de mascotas
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("ID de mascota"), numeric=True),
                    ft.DataColumn(ft.Text("Nombre de la mascota")),
                    ft.DataColumn(ft.Text("Especie")),
                    ft.DataColumn(ft.Text("Raza")),
                    ft.DataColumn(ft.Text("Sexo")),
                    ft.DataColumn(ft.Text("Edad"), numeric=True),
                    ft.DataColumn(ft.Text("ID del propietario"), numeric=True),
                    ft.DataColumn(ft.Text("Nombre del propietario"))
                ],
                rows=rows
            )
        ]
    )
