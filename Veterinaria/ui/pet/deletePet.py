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
                leading=IconButton(icon=ft.icons.ARROW_BACK, tooltip='Back to "Pet List"', on_click=lambda _: page.go("/ownerls/petls")),
                title= Text("Delete Pet"),
                automatically_imply_leading=False,
                ),
            ft.Text("Make sure you enter the correct ID!! THERE'S NO TURNING BACK!!!", size=10, color='#FF0000'),
            petid,
            ft.ElevatedButton("Delete Pet", on_click=delete)
        ]
    )