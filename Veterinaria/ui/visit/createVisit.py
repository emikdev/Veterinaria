import flet as ft
from flet import *
from config.database import *
from models.models import *
from flet_route import Params,Basket

def createVisit(page:ft.Page,params:Params,basket:Basket):
    petid = ft.TextField(hint_text=("Pet ID"))
    date = ft.TextField(hint_text="date")
    reason = ft.TextField(hint_text="reason")
    description = ft.TextField(hint_text="description")

    def create_visit(e):
        # Obtener los valores de los campos de texto
        petid_value = petid.value
        date_value = date.value
        reason_value = reason.value
        description_value = description.value
        
        # Insertar los valores en la tabla "owner"
        query = f"INSERT INTO visit (id_pet, date, reason, description) VALUES ('{petid_value}', '{date_value}', '{reason_value}', '{description_value}')"
        cursor.execute(query)
        conn.commit()

        # Redirigir a la página de lista de propietarios
        page.go("/ownerls/petls/visitls")

    return ft.View(
        "/ownerls/petls/visitls/createVisit",
        controls=[
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, tooltip='Back to "Visit List"', on_click=lambda _: page.go("/ownerls/petls/visitls")),
                title= Text("Create Visit"),
                automatically_imply_leading=False,
                ),
            ft.Text("Please make sure that the pet is already registered on the pet list before creating a visit", size=10, color='#FFA500'),
            petid,
            date,
            reason,
            description,
            ft.ElevatedButton("Create Visit", on_click=create_visit)
        ]
    )