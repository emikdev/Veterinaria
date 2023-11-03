import flet as ft
from flet import *
from flet_route import Params,Basket

def ownerls(page:ft.Page,params:Params,basket:Basket):

    return ft.View(
        "/ownerls",
        controls=[
            ft.AppBar(
                title= Text("Owner List"),
                automatically_imply_leading=False,
                actions=[
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
                    ft.DataColumn(ft.Text("Email")),
                    ft.DataColumn(ft.Text("Pet Name")),
                    ft.DataColumn(ft.Text("Pet-Info"))
                ],
                rows=[
                    ft.DataRow(cells=[ft.DataCell(ft.Text("1")),
                    ft.DataCell(ft.Text("Damian Muñoz")),
                    ft.DataCell(ft.Text("46266463")),
                    ft.DataCell(ft.Text("+54 911 3372-6899")),
                    ft.DataCell(ft.Text("damzerotec@gmail.com")),
                    ft.DataCell(ft.Text("Obvi")),
                    ft.DataCell(ft.ElevatedButton("View Pet", on_click=lambda _: page.go("/ownerls/petls")))
                    ]),

                    ft.DataRow(cells=[ft.DataCell(ft.Text("2")),
                    ft.DataCell(ft.Text("Ludmila Achucarro")),
                    ft.DataCell(ft.Text("46628300")),
                    ft.DataCell(ft.Text("+54 911 2488-6670")),
                    ft.DataCell(ft.Text("ludmila07achucarro@gmail.com")),
                    ft.DataCell(ft.Text("Blanca")),
                    ft.DataCell(ft.ElevatedButton("View Pet", on_click=lambda _: page.go("/ownerls/petls")))
                    ]),

                ]
            )

        ]
    )
