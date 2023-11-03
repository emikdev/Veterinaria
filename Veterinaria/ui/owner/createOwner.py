import flet as ft
from flet import *
from flet_route import Params,Basket

global name, dni, phone, mail
name = ft.TextField(hint_text="Name")
dni = ft.TextField(hint_text="DNI")
phone = ft.TextField(hint_text="Phone")
mail = ft.TextField(hint_text="Email")

def createOwner(page:ft.Page,params:Params,basket:Basket):

    return ft.View(
        "/ownerls/createOwner",
        controls=[
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls")),
                title= Text("Create Owner"),
                automatically_imply_leading=False,
                ),
            name,
            dni,
            phone,
            mail,
            ft.ElevatedButton("Create Owner")
        ]
    )
