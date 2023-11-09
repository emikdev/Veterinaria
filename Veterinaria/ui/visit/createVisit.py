# Se Importan las librerias y paquetes necesarios 
import flet as ft
from flet import *
from config.database import *
from models.models import *
from flet_route import Params,Basket

# Se define la variable que contenedora de la View
def createVisit(page:ft.Page,params:Params,basket:Basket):

    # Se recupera la id del usuario que estaba almacenada en el "Session Storage"
    veterinaryid = page.session.get("veterinaryid")

    # Se declaran las variables e inpust que se emplearan en la View y el Query
    global vetid
    petid = ft.TextField(hint_text=("Pet ID"))
    date = ft.TextField(hint_text="date")
    reason = ft.TextField(hint_text="reason")
    description = ft.TextField(hint_text="description")

    # Se define la funcion encargada de insertar los datos en la tabla
    def create_visit(e):

        # Se obtienen los valores de los campos de texto
        vetid_value = veterinaryid
        petid_value = petid.value
        date_value = date.value
        reason_value = reason.value
        description_value = description.value
        
        # Se insertan los valores en la tabla "owner"
        query = f"INSERT INTO visit (id_veterinary, id_pet, date, reason, description) VALUES ('{vetid_value}', '{petid_value}', '{date_value}', '{reason_value}', '{description_value}')"
        cursor.execute(query)
        conn.commit()

        # Se redirige al usuario a "Visit-List"
        page.go("/ownerls/petls/visitls")

    # Se retorna el contenido de la View
    return ft.View(
        "/ownerls/petls/visitls/createVisit",
        controls=[
            # Se define el contenido de la View
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