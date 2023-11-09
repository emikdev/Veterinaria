# Se importar las librerias y paquetes necesarios
import flet as ft
import flet_route
from flet import *
from flet_route import Params,Basket
from config.database import *

# Se realiza la definicion de variables locales
global user, key, veterinaryid

# Se crean los imputs que se emplearan en la View
user = ft.TextField(hint_text="Username", width=350)
key = ft.TextField(hint_text="Password", width=350)

# Se define la funcion contenedora de la View
def login(page:ft.Page,params:Params,basket:Basket):

    # Se define la funion encargada de validar el usuario
    def log(e): # Crea la funcion "Login"

        # Obtener el usuario y la contraseña ingresados por el usuario
        username = user.value
        password = key.value

        # Consultar la base de datos para buscar el usuario
        sql = "SELECT password FROM veterinary WHERE username = %s"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()

        # Condicional para realiar la consulta a la base de datos
        if result is not None: # Si se encuentra el usuario en la base de datos, verificar la contraseña

            stored_password = result[0]

            if password == stored_password: # Si la contraseña se encuentra se muestra el siguiente mensaje

                # Al iniciar sesion se obtiene la ID del usuario
                query = "SELECT id FROM veterinary WHERE username = %s AND password = %s"
                cursor.execute(query, (username, password))
                resultado = cursor.fetchone()
                veterinaryid = resultado[0]

                # Se guarda la ID del usuario en el "Session Storage"
                page.session.set("veterinaryid", veterinaryid)
                
                # Se redirecciona al usuario del login al panel
                page.go("/ownerls")

            else: # Si la contraseña no se encuentra se muestra el siguiente mensaje

                print("Contraseña incorrecta")

        else: # Si el usuario no se encuentra en la base de datos se muestra el siguinete mensaje

            print("Usuario Inexistente")

    # Se retornma el conmtenido de la View
    return ft.View(
        "/",
        controls=[
            # Se define el conmtenido de la View
            ft.Text("Login", size=50),
            user,   
            key,
            ft.Text("Please enter the Username and Password corresponding to your branch", size=10, color='#FFA500'),
            ft.ElevatedButton("Login", on_click=log)
        ]
    )