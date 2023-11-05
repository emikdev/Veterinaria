# Importar bibliotecas
import flet as ft
from flet import *
from config.database import *
from flet_route import Params,Basket

# Definir variable global
global petid

# Crear campo de texto
petid = ft.TextField(hint_text="Pet Delete ID")

# Definir función `deletePet`
def deletePet(page:ft.Page,params:Params,basket:Basket):

    # Definir función interna `delete`
    def delete(e):
        # Recuperar valor del campo de texto
        pet_id = petid.value

        # Construir consulta SQL
        delete_query = f"DELETE FROM pet WHERE id = {pet_id}"

        # Ejecutar consulta SQL
        cursor.execute(delete_query)

        # Confirmar transacción
        conn.commit()

        # Redireccionar a página `/ownerls/petls`
        page.go("/ownerls/petls")

    # Devolver vista
    return ft.View(
        "/ownerls/petls/deletePet",
        controls=[
            # Barra de aplicación con botón de retroceso
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls/petls")),
                title= Text("Delete Pet"),
                automatically_imply_leading=False,
            ),
            # Campo de texto para ingresar el ID de la mascota a eliminar
            petid,
            # Botón elevado para eliminar la mascota
            ft.ElevatedButton("Delete Pet", on_click=delete)
        ]
    )

