import flet as ft
from flet import *
from config.database import *
from flet_route import Params, Basket

# Declara una variable global para almacenar el ID del propietario a eliminar
global ownerid
ownerid = ft.TextField(hint_text="ID de propietario a eliminar")

# Define una función para manejar la eliminación de un propietario
def deleteOwner(page:ft.Page,params:Params,basket:Basket):

    # Define una función de devolución de llamada para manejar el clic del botón "Eliminar propietario"
    def delete(e):

        # Obtén el ID del propietario del campo de texto
        owner_id = ownerid.value

        # Construye la consulta SQL para eliminar el propietario de la base de datos
        delete_query = f"DELETE FROM owner WHERE id = {owner_id}"

        # Ejecuta la consulta para eliminar el propietario de la base de datos
        cursor.execute(delete_query)
        conn.commit()

        # Redirige al usuario a la página de lista de propietarios
        page.go("/ownerls")

    return ft.View(
        "/ownerls/deleteOwner",
        controls=[
            # Agrega una barra de aplicaciones con un botón de retroceso y un título
            ft.AppBar(
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls")),
                title= ft.Text("Eliminar propietario"),
                automatically_imply_leading=False,
            ),

            # Agrega el campo de texto para ingresar el ID del propietario a eliminar
            ownerid,

            # Agrega un botón elevado con la etiqueta "Eliminar propietario" y la función de devolución de llamada adjunta
            ft.ElevatedButton("Eliminar propietario", on_click=delete)
        ]
    )
