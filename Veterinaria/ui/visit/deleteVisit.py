# Se importan las librerias y paquetes necesarios
import flet as ft
from flet import *
from config.database import *
from flet_route import Params,Basket

# Se define las variables e inputs que se emplearan en la View y el Query
global visitid
visitid = ft.TextField(hint_text="Visit Delete ID")

# Se define la funcion contenedora de la View
def deleteVisit(page:ft.Page,params:Params,basket:Basket):

    # Se define la variable encargada de eliminar la Visita
    def delete(e):

        # Se elimina la Visita de la BD
        visit_id = visitid.value
        delete_query = f"DELETE FROM visit WHERE id = {visit_id}"
        cursor.execute(delete_query)
        conn.commit()

        # Se redirecciona el usuario a "Visit-List"
        page.go("/ownerls/petls/visitls")

    # Se retorna el cotenido de la View
    return ft.View(
        "/ownerls/petls/deleteVisit/deleteVisit",
        controls=[
            # Se define el contenido de la View
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