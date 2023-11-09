# Se importan las librerias y paquetes necesarios
import flet as ft
from flet import *
from config.database import *
from flet_route import Params,Basket

# se declaran las variables e inputs que se emplearan en la View y el Query
global ownerid
ownerid = ft.TextField(hint_text="Owner Delete ID")

# Se define la funcion contenedora de la View
def deleteOwner(page:ft.Page,params:Params,basket:Basket):

    # Se define la variable encargada de eliminar un Dueño    
    def delete(e):

        # Se elimina el dueño de la base de datos
        owner_id = ownerid.value
        delete_query = f"DELETE FROM owner WHERE id = {owner_id}"
        cursor.execute(delete_query)
        conn.commit()

        # Se redirrecciona a "Owner-List"
        page.go("/ownerls")

    # Se retorna el contenido de la View
    return ft.View(
        "/ownerls/deleteOwner",
        controls=[
            # Se define el contenido de la View
            ft.AppBar(
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK, tooltip='Back to "Owner List"', on_click=lambda _: page.go("/ownerls")),
                title= ft.Text("Delete Owner"),
                automatically_imply_leading=False,
                ),
            ft.Text("Make sure you enter the correct ID!! THERE'S NO TURNING BACK!!!", size=10, color='#FF0000'),
            ownerid,
            ft.ElevatedButton("Delete Owner", on_click=delete)
        ]
    )

