import flet as ft
from flet import *
from config.database import *
from flet_route import Params,Basket

global visitid
visitid = ft.TextField(hint_text="Visit Delete ID")

def deleteVisit(page:ft.Page,params:Params,basket:Basket):

    def delete(e):

        visit_id = visitid.value
        delete_query = f"DELETE FROM visit WHERE id = {visit_id}"
        cursor.execute(delete_query)
        conn.commit()

        page.go("/ownerls/petls/visitls")

    return ft.View(
        "/ownerls/petls/deleteVisit/deleteVisit",
        controls=[
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, tooltip='Back to "Visit List"', on_click=lambda _: page.go("/ownerls/petls/visitls")),
                title= Text("Delete Visit"),
                automatically_imply_leading=False,
                ),
            ft.Text("Make sure you enter the correct ID!! THERE'S NO TURNING BACK!!!", size=10, color='#FF0000'),
            visitid,
            ft.ElevatedButton("Delete Visit", on_click=delete)
        ]
    )