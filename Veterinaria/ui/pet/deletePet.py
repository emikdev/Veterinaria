# Se importan las librerias y paquetes necesarios
import flet as ft
from flet import *
from config.database import *
from flet_route import Params,Basket

# Se crean las variables globales y e inputs que se emplearan en la View y el Query
global petid
petid = ft.TextField(hint_text="Pet Delete ID")

# Se define la funcion contenedora de la View
def deletePet(page:ft.Page,params:Params,basket:Basket):

    # Se crea la funcion encargada de eliminar la Mascota
    def delete(e):

        # Se elimina la mascota de la BD
        pet_id = petid.value
        delete_query = f"DELETE FROM pet WHERE id = {pet_id}"
        cursor.execute(delete_query)
        conn.commit()

        # Se redirecciona al usuario a "Pet-List"
        page.go("/ownerls/petls")

    # Se retorna el contenido de la View
    return ft.View(
        "/ownerls/petls/deletePet",
        controls=[
            # Se define el contenido de la View
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