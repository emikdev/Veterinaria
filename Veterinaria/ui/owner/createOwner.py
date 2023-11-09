# Se Importan las librerias y paquetes necesarios
import flet as ft
from flet import *
from config.database import *
from models.models import *
from flet_route import Params,Basket

# Se define la funcion contenedora de la View
def createOwner(page:ft.Page,params:Params,basket:Basket):

    # Si recupera la id del usuario que estaba almacenada en el "Session Storage"
    veterinaryid = page.session.get("veterinaryid")

    # Se definen las variables globales y los inputs que se emplearan en la View y el Query
    global vetid_value
    name = ft.TextField(hint_text="Name")
    dni = ft.TextField(hint_text="DNI")
    phone = ft.TextField(hint_text="Phone")
    mail = ft.TextField(hint_text="Email")

    # Se define la funcion encargada de enviar los datos ingresados a la BD
    def create_owner(e):

        # Obtener los valores de los campos de texto
        vetid_value = veterinaryid
        name_value = name.value
        dni_value = dni.value
        phone_value = phone.value
        mail_value = mail.value

        # Se insertan los valores en la tabla "owner"
        query = f"INSERT INTO owner (id_veterinary, name, dni, phone, mail) VALUES ('{vetid_value}', '{name_value}', '{dni_value}', '{phone_value}', '{mail_value}')"
        cursor.execute(query)
        conn.commit()

        # Se redirecciona a "Owner-List"
        page.go("/ownerls")

    # Se retorna el contenido de la View
    return ft.View(
        "/ownerls/createOwner",
        controls=[
            # Se define el contenido de la View
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
