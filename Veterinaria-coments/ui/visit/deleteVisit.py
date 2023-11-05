# Importar bibliotecas
import flet as ft
from flet import *
from config.database import *
from flet_route import Params,Basket

# Definir variable global
global visitid

# Crear campo de texto
visitid = ft.TextField(hint_text="ID de la visita a eliminar")

# Definir función `deleteVisit`
def deleteVisit(page: ft.Page, params: Params, basket: Basket):

    # Definir función interna `delete`
    def delete(e):
        # Obtener el valor del campo de texto
        visit_id = visitid.value

        # Construir consulta SQL para eliminar la visita
        delete_query = f"DELETE FROM visit WHERE id = {visit_id}"

        # Ejecutar consulta SQL y confirmar transacción
        cursor.execute(delete_query)
        conn.commit()

        # Redireccionar a la página de lista de visitas
        page.go("/ownerls/petls/visitls")

    # Devolver vista
    return ft.View(
        "/ownerls/petls/deleteVisit",
        controls=[
            # Barra de aplicación con botón de retroceso
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls/petls/visitls")),
                title= Text("Eliminar visita"),
                automatically_imply_leading=False,
            ),
            # Campo de texto para ingresar el ID de la visita
            visitid,
            # Botón elevado para eliminar la visita
            ft.ElevatedButton("Eliminar visita", on_click=delete)
        ]
    )
