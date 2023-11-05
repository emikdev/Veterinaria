# Importar bibliotecas
import flet as ft
from flet import *
from config.database import *
from models.models import *
from flet_route import Params,Basket

# Definir función `createVisit`
def createVisit(page: ft.Page, params: Params, basket: Basket):
    petid = ft.TextField(hint_text=("Pet ID"))
    date = ft.TextField(hint_text="date")
    reason = ft.TextField(hint_text="reason")
    description = ft.TextField(hint_text="description")

    # Definir función interna `create_visit`
    def create_visit(e):
        # Obtener los valores de los campos de texto
        petid_value = petid.value
        date_value = date.value
        reason_value = reason.value
        description_value = description.value

        # Insertar los valores en la tabla `visit`
        query = f"INSERT INTO visit (id_pet, date, reason, description) VALUES ('{petid_value}', '{date_value}', '{reason_value}', '{description_value}')"
        cursor.execute(query)
        conn.commit()

        # Redirigir a la página de lista de visitas
        page.go("/ownerls/petls/visitls")

    # Devolver vista
    return ft.View(
        "/ownerls/petls/visitls/createVisit",
        controls=[
            # Barra de aplicación con botón de retroceso
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls/petls/visitls")),
                title= Text("Create Visit"),
                automatically_imply_leading=False,
            ),
            # Campo de texto para ingresar el ID de la mascota
            petid,
            # Campo de texto para ingresar la fecha
            date,
            # Campo de texto para ingresar el motivo de la visita
            reason,
            # Campo de texto para ingresar una descripción
            description,
            # Botón elevado para crear la visita
            ft.ElevatedButton("Create Visit", on_click=create_visit)
        ]
    )

