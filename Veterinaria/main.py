# Se importan las librerias y paquetes necesarios
import flet as ft
from flet import *
from flet_route import Routing,path

# Se importan las interfaces de la app
from ua.login import *
from ui.owner.ownerList import *
from ui.pet.petList import *
from ui.visit.visitList import *
from ui.owner.createOwner import *
from ui.pet.createPet import *
from ui.visit.createVisit import *
from ui.owner.deleteOwner import *
from ui.pet.deletePet import *
from ui.visit.deleteVisit import *

# Se define la funcion main
def main(page: ft.Page):

    # Se definen parametros de la app
    page.title ="Veterinary Management"
    page.theme_mode ="light"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Se definen las rutas
    app_routes = [
        path(url="/", clear=True, view=login), 
        path(url="/ownerls", clear=False, view=ownerls),
        path(url="/ownerls/petls", clear=False, view=petls),
        path(url="/ownerls/petls/visitls", clear=False, view=visitls),
        path(url="/ownerls/createOwner", clear=False, view=createOwner),
        path(url="/ownerls/petls/createPet", clear=False, view=createPet),
        path(url="/ownerls/petls/visitls/createVisit", clear=False, view=createVisit),
        path(url="/ownerls/deleteOwner", clear=False, view=deleteOwner),
        path(url="/ownerls/petls/deletePet", clear=False, view=deletePet),
        path(url="/ownerls/petls/visitls/deleteVisit", clear=False, view=deleteVisit),

    ]

    # Se crea el sistema de redireccion
    Routing(page=page, app_routes=app_routes,)
    page.go(page.route)
    
# Se carga la funcion main lanzando la app
ft.app(target=main)

 # view=ft.AppView.WEB_BROWSER