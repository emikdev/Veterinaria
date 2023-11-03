import flet as ft
from flet import *
from flet_route import Params,Basket

global date, motive, description
date = ft.TextField(hint_text="date")
motive = ft.TextField(hint_text="motive")
description = ft.TextField(hint_text="description")

def createVisit(page:ft.Page,params:Params,basket:Basket):

    return ft.View(
        "/ownerls/petls/visitls/createVisit",
        controls=[
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls/petls/visitls")),
                title= Text("Create Visit"),
                automatically_imply_leading=False,
                ),
            date,
            motive,
            description,
            ft.ElevatedButton("Create Visit")
        ]
    )