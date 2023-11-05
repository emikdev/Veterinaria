import flet as ft
from flet import *
from config.database import *
from flet_route import Params,Basket

global ownerid
ownerid = ft.TextField(hint_text="Owner Delete ID")

def deleteOwner(page:ft.Page,params:Params,basket:Basket):
        
    def delete(e):

        owner_id = ownerid.value
        delete_query = f"DELETE FROM owner WHERE id = {owner_id}"
        cursor.execute(delete_query)
        conn.commit()

        page.go("/ownerls")

    return ft.View(
        "/ownerls/deleteOwner",
        controls=[
            ft.AppBar(
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls")),
                title= ft.Text("Delete Owner"),
                automatically_imply_leading=False,
                ),
            ownerid,
            ft.ElevatedButton("Delete Owner", on_click=delete)
        ]
    )

