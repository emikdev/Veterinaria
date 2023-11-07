import flet as ft
from flet import *
from config.database import *
from models.models import *
from flet_route import Params,Basket

def createOwner(page:ft.Page,params:Params,basket:Basket):
    name = ft.TextField(hint_text="Name")
    dni = ft.TextField(hint_text="DNI")
    phone = ft.TextField(hint_text="Phone")
    mail = ft.TextField(hint_text="Email")

    def create_owner(e):
        # Obtener los valores de los campos de texto
        name_value = name.value
        dni_value = dni.value
        phone_value = phone.value
        mail_value = mail.value

        # Insertar los valores en la tabla "owner"
        query = f"INSERT INTO owner (name, dni, phone, mail) VALUES ('{name_value}', '{dni_value}', '{phone_value}', '{mail_value}')"
        cursor.execute(query)
        conn.commit()

        # Redirigir a la página de lista de propietarios
        page.go("/ownerls")

    return ft.View(
        "/ownerls/createOwner",
        controls=[
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, tooltip='Back to "Owner List"', on_click=lambda _: page.go("/ownerls")),
                title= Text("Create Owner"),
                automatically_imply_leading=False,
            ),
            name,
            dni,
            phone,
            mail,
            ft.ElevatedButton("Create Owner", on_click=create_owner)
        ]
    )
