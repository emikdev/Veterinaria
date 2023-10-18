import flet # Importa la libreria Flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors # Importa los componentes a utilizar


def main(page: Page): # Se crea la funcion principal

    page.title = "Veterinary management" # Se le asigna un titulo a la pestaña

    print("Initial route:", page.route) # Se muestra el texto en la onsola

    # Funcion para realizar los cambios de ruta que sean necesarios

    def route_change(e):

            # Interfaz "Admin Panel"

        print("Route change:", e.route)
        page.views.clear()
        
        page.views.append(  
            View(
                "/", # Dirreccion de la UI
                [   # Contenido de la UI
                    AppBar(title=Text("Admin Panel")), # Titulo de la appbar
                    ElevatedButton("Owner List", on_click=owner_list), # Boton que llama la funcion "owner_list"
                    ElevatedButton("Pet List", on_click=pet_list), # Boton que llama la funcion "pet_list"
                    ElevatedButton("Logout", on_click=logout) # Boton que llama la funcion "logout"
                ],
            )
        )

            # Interfaz "Owner-List"

        if page.route == "/ownerls" or page.route == "/ownerls/owner": # Condicion que al cumplirse carga la UI de "ownerls"
            page.views.append(
                View(
                    "/ownerls", # Dirrecion de la UI
                    [   # Contenido de la UI
                        AppBar(title=Text("Owner-List"), bgcolor=colors.SURFACE_VARIANT), # Titulo de la appbar
                        Text("Correct load owner list!", style="bodyMedium"), # Mensaje de la carga de los dueños
                        ElevatedButton(
                            "Open owner", on_click=owner # Boton para abrir un usuario
                        ),
                    ],
                )
            )

            # Interfaz "Owner-Information"

        if page.route == "/ownerls/owner":  # Condicion que al cumplirse carga la UI de "owner"
            page.views.append(
                View(
                    "/ownerls/owner", # Dirrecion de la UI
                    [   # Contenido de la UI
                        AppBar(
                            title=Text("Owner-Information"), bgcolor=colors.SURFACE_VARIANT # Titulo de la appbar
                        ),
                        Text("Correct load owner information!"), # Mensaje de la carga correcta de la informacion
                    ],
                )
            )

            # Interfaz "Pet-List"

        if page.route == "/petls" or page.route == "/petls/pet": # Condicion que al cumplirse carga la UI de "ownerls"
            page.views.append(
                View(
                    "/petls", # Dirrecion de la UI
                    [   # Contenido de la UI
                        AppBar(title=Text("Pet-List"), bgcolor=colors.SURFACE_VARIANT), # Titulo de la appbar
                        Text("Correct load pet list!", style="bodyMedium"), # Mensaje de la carga de las mascotas
                        ElevatedButton(
                            "Open pet", on_click=pet # Boton para abrir una mascota
                        ),
                    ],
                )
            )

            # Interfaz "Pet-Information"

        if page.route == "/petls/pet":  # Condicion que al cumplirse carga la UI de "pet"
            page.views.append(
                View(
                    "/petls/pet", # Dirrecion de la UI
                    [   # Contenido de la UI
                        AppBar(
                            title=Text("Pet-Information"), bgcolor=colors.SURFACE_VARIANT # Titulo de la appbar
                        ),
                        Text("Correct load pet information!"), # Mensaje de la carga correcta de la informacion
                        ElevatedButton(
                            "Visit-List", on_click=visit_list # Boton para abrir la lista de visitas de la mascota
                        ),
                    ],
                )
            )

            # Interfaz "Visit-List"

        if page.route == "/petls/pet/visitls" or page.route == "/petls/pet/visitls/visit": # Condicion que al cumplirse carga la UI de "ownerls"
            page.views.append(
                View(
                    "/petls/pet/visitls", # Dirrecion de la UI
                    [   # Contenido de la UI
                        AppBar(title=Text("Visit-List"), bgcolor=colors.SURFACE_VARIANT), # Titulo de la appbar
                        Text("Correct load visit list!", style="bodyMedium"), # Mensaje de la carga de las visitas
                        ElevatedButton(
                            "Open visit", on_click=visit # Boton para abrir una visita
                        ),
                    ],
                )
            )

            # Interfaz "Visit-Information"

        if page.route == "/petls/pet/visitls/visit":  # Condicion que al cumplirse carga la UI de "owner"
            page.views.append(
                View(
                    "/petls/pet/visitls/visit", # Dirrecion de la UI
                    [   # Contenido de la UI
                        AppBar(
                            title=Text("Visit-Information"), bgcolor=colors.SURFACE_VARIANT # Titulo de la appbar
                        ),
                        Text("Correct load visit information!"), # Mensaje de la carga correcta de la informacion
                    ],
                )
            )

        page.update()

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

        # Funciones para Owner's UI

    def owner(e): # Funcion para redirreccionar a la UI "owner"
        page.go("/ownerls/owner")

    def owner_list(e): # Funcion para redirreccionar a la UI "ownerls"
        page.go("/ownerls")

        # Funciones para Pet's UI

    def pet(e): # Funcion para redirreccionar a la UI "pet"
        page.go("/petls/pet")

    def pet_list(e): # Funcion para redirreccionar a la UI "petls"
        page.go("/petls")

        # Funciones para Visit's UI

    def visit(e): # Funcion para redirreccionar a la UI "visit"
        page.go("/petls/pet/visitls/visit")

    def visit_list(e): # Funcion para redirreccionar a la UI "visitls"
        page.go("/petls/pet/visitls")

        # Funcion para el boton de logout

    def logout(e): # Funcion deslogearse
        page.go("/")

    page.go(page.route)

flet.app(target=main, view=flet.WEB_BROWSER) # Se ejecuta la app en el entorno de navegador web
