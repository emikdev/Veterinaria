# Importar las bibliotecas necesarias
import flet as ft
from flet_route import Routing, path

# Importar las funciones de las vistas
from ua.login import login
from ui.owner.ownerList import ownerls
from ui.pet.petList import petls
from ui.visit.visitList import visitls
from ui.owner.createOwner import createOwner
from ui.pet.createPet import createPet
from ui.visit.createVisit import createVisit
from ui.owner.deleteOwner import deleteOwner
from ui.pet.deletePet import deletePet
from ui.visit.deleteVisit import deleteVisit

# Definir la función principal
def main(page: ft.Page):

    # Crear una lista de rutas
    app_routes = [
        # Ruta para la página de inicio
        path(url="/", clear=True, view=login),
        # Ruta para la lista de propietarios
        path(url="/ownerls", clear=False, view=ownerls),
        # Ruta para la lista de mascotas de un propietario
        path(url="/ownerls/petls", clear=False, view=petls),
        # Ruta para la lista de visitas de una mascota
        path(url="/ownerls/petls/visitls", clear=False, view=visitls),
        # Ruta para el formulario de creación de un propietario
        path(url="/ownerls/createOwner", clear=False, view=createOwner),
        # Ruta para el formulario de creación de una mascota
        path(url="/ownerls/petls/createPet", clear=False, view=createPet),
        # Ruta para el formulario de creación de una visita
        path(url="/ownerls/petls/visitls/createVisit", clear=False, view=createVisit),
        # Ruta para el formulario de eliminación de un propietario
        path(url="/ownerls/deleteOwner", clear=False, view=deleteOwner),
        # Ruta para el formulario de eliminación de una mascota
        path(url="/ownerls/petls/deletePet", clear=False, view=deletePet),
        # Ruta para el formulario de eliminación de una visita
        path(url="/ownerls/petls/visitls/deleteVisit", clear=False, view=deleteVisit),
    ]

    # Registrar las rutas
    Routing(page=page, app_routes=app_routes,)

    # Dirigir a la página correspondiente
    page.go(page.route)

# Iniciar la aplicación
ft.app(target=main)
