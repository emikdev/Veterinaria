import flet as ft
from flet import *
from flet_route import Params,Basket

def visitls(page:ft.Page,params:Params,basket:Basket):

    return ft.View(
        "/ownerls/petls/visitls",
        controls=[
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls/petls")),
                title= Text("Visit List"),
                automatically_imply_leading=False,
                actions=[
                    ft.ElevatedButton("Create Visit", on_click=lambda _: page.go("/ownerls/petls/visitls/createVisit")),
                ]
                ),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("ID"), numeric=True),
                    ft.DataColumn(ft.Text("Date")),
                    ft.DataColumn(ft.Text("Motive")),
                    ft.DataColumn(ft.Text("Description"))
                ],
                rows=[
                    ft.DataRow(cells=[ft.DataCell(ft.Text("1")),
                    ft.DataCell(ft.Text("26-10-2023")),
                    ft.DataCell(ft.Text("Limpieza Dental")),
                    ft.DataCell(ft.Text("Sin Complicaciones"))
                    ]),

                ]
            )
        ]
    )
