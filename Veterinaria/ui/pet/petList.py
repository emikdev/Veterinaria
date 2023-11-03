import flet as ft
from flet import *
from flet_route import Params,Basket

def petls(page:ft.Page,params:Params,basket:Basket):

    return ft.View(
        "/ownerls/petls",
        controls=[
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls")),
                title= Text("Pet List"),
                automatically_imply_leading=False,
                actions=[
                    ft.ElevatedButton("Create Pet", on_click=lambda _: page.go("/ownerls/petls/createPet")),
                ]
                ),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("ID"), numeric=True),
                    ft.DataColumn(ft.Text("Name")),
                    ft.DataColumn(ft.Text("Species")),
                    ft.DataColumn(ft.Text("Race")),
                    ft.DataColumn(ft.Text("Sex")),
                    ft.DataColumn(ft.Text("age"), numeric=True),
                    ft.DataColumn(ft.Text("View Visit List"))
                ],
                rows=[
                    ft.DataRow(cells=[ft.DataCell(ft.Text("1")),
                    ft.DataCell(ft.Text("Obvi")),
                    ft.DataCell(ft.Text("Dog")),
                    ft.DataCell(ft.Text("Bull Terrier")),
                    ft.DataCell(ft.Text("Male")),
                    ft.DataCell(ft.Text("1")),
                    ft.DataCell(ft.ElevatedButton("Visit List", on_click=lambda _: page.go("/ownerls/petls/visitls")))
                    ]),

                    ft.DataRow(cells=[ft.DataCell(ft.Text("2")),
                    ft.DataCell(ft.Text("Blanca")),
                    ft.DataCell(ft.Text("Dog")),
                    ft.DataCell(ft.Text("Mongrel")),
                    ft.DataCell(ft.Text("Female")),
                    ft.DataCell(ft.Text("4")),
                    ft.DataCell(ft.ElevatedButton("Visit List", on_click=lambda _: page.go("/ownerls/petls/visitls")))
                    ]),

                ]
            )

        ]
    )