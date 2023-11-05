import flet as ft
from flet import *
from config.database import *
from flet_route import Params,Basket

global petid
petid = ft.TextField(hint_text="Pet Delete ID")

def deletePet(page:ft.Page,params:Params,basket:Basket):

    def delete(e):

        pet_id = petid.value
        delete_query = f"DELETE FROM pet WHERE id = {pet_id}"
        cursor.execute(delete_query)
        conn.commit()

        page.go("/ownerls/petls")

    return ft.View(
        "/ownerls/petls/deletePet",
        controls=[
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls/petls")),
                title= Text("Delete Pet"),
                automatically_imply_leading=False,
                ),
            petid,
            ft.ElevatedButton("Delete Pet", on_click=delete)
        ]
    )