import flet as ft
from flet import *
from config.database import *
from flet_route import Params,Basket

global user, key

user = ft.TextField(hint_text="Username")
key = ft.TextField(hint_text="Password")

def login(page:ft.Page,params:Params,basket:Basket):

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

                print("Inicio de sesion exitoso!!")
                page.go("/ownerls")

            else: # Si la contraseña no se encuentra se muestra el siguiente mensaje

                print("Contraseña incorrecta")


        else: # Si el usuario no se encuentra en la base de datos se muestra el siguinete mensaje

            print("Usuario Inexistente")


    return ft.View(
        "/",
        controls=[
            user,   
            key,
            ft.ElevatedButton("Iniciar Sesion", on_click=lambda _: page.go("/ownerls"))
        ]
    )