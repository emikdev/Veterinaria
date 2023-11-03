import flet as ft
from flet_route import Routing,path
from ua.login import *
from ui.owner.ownerList import *
from ui.pet.petList import *
from ui.visit.visitList import *
from ui.owner.createOwner import *
from ui.pet.createPet import *
from ui.visit.createVisit import *


def main(page: ft.Page):

    app_routes = [
        path(url="/", clear=True, view=login), 
        path(url="/ownerls", clear=False, view=ownerls),
        path(url="/ownerls/petls", clear=False, view=petls),
        path(url="/ownerls/petls/visitls", clear=False, view=visitls),
        path(url="/ownerls/createOwner", clear=False, view=createOwner),
        path(url="/ownerls/petls/createPet", clear=False, view=createPet),
        path(url="/ownerls/petls/visitls/createVisit", clear=False, view=createVisit),

    ]

    Routing(page=page, app_routes=app_routes,)
    page.go(page.route)
    
ft.app(target=main)