import flet as ft
from flet import *
from flet_route import Params,Basket

global name, species, race, sex, age
name = ft.TextField(hint_text="Name")
species = ft.TextField(hint_text="Species")
race = ft.TextField(hint_text="Race")
sex = ft.TextField(hint_text="Sex")
age = ft.TextField(hint_text="Age")

def createPet(page:ft.Page,params:Params,basket:Basket):

    return ft.View(
        "/ownerls/petls/createPet",
        controls=[
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls/petls")),
                title= Text("Create Pet"),
                automatically_imply_leading=False,
                ),
            name,
            species,
            race,
            sex,
            age,
            ft.ElevatedButton("Create Pet")
        ]
    )