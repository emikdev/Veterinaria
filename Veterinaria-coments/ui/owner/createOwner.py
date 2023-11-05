# Importa las bibliotecas necesarias
import flet as ft
from flet import *
from config.database import *
from models.models import *
from flet_route import Params, Basket

# Define una función para crear un nuevo propietario
def createOwner(page:ft.Page,params:Params,basket:Basket):
    # Crea campos de texto para recopilar información del propietario
    name = ft.TextField(hint_text="Nombre")
    dni = ft.TextField(hint_text="DNI")
    phone = ft.TextField(hint_text="Teléfono")
    mail = ft.TextField(hint_text="Correo electrónico")

    # Define una función de devolución de llamada para manejar el clic del botón "Crear propietario"
    def create_owner(e):
        # Obtén los valores de los campos de texto
        name_value = name.value
        dni_value = dni.value
        phone_value = phone.value
        mail_value = mail.value

        # Construye la consulta SQL para insertar los datos del propietario en la tabla "owner"
        query = f"INSERT INTO owner (name, dni, phone, mail) VALUES ('{name_value}', '{dni_value}', '{phone_value}', '{mail_value}')"

        # Ejecuta la consulta para insertar los datos del propietario en la base de datos
        cursor.execute(query)
        conn.commit()

        # Redirige al usuario a la página de lista de propietarios
        page.go("/ownerls")

    # Crea la vista para la página "Crear propietario"
    return ft.View(
        "/ownerls/createOwner",
        controls=[
            # Agrega una barra de aplicaciones con un botón de retroceso y un título
            ft.AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: page.go("/ownerls")),
                title= Text("Crear propietario"),
                automatically_imply_leading=False,
            ),

            # Agrega los campos de texto para nombre, DNI, teléfono y correo electrónico
            name,
            dni,
            phone,
            mail,

            # Agrega un botón elevado con la etiqueta "Crear propietario" y la función de devolución de llamada adjunta
            ft.ElevatedButton("Crear propietario", on_click=create_owner)
        ]
    )
