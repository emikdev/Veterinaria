import flet as ft # Importa la Libreria de Flet
from config.database import * # Importa el contenido de "database.py"

def main(page: ft.Page): # Crea la funcion main
    global user, key # Se definen las variables "User" y "Key" de tipo Global

    page.window_width = 400 # Define el ancho de la ventana
    page.window_height = 900 # Define el alto de la ventana

    def login(event): # Crea la funcion "Login"

        # Obtener el usuario y la contraseña ingresados por el usuario

        username = user.value
        password = key.value

        # Consultar la base de datos para buscar el usuario

        sql = "SELECT password FROM users WHERE user = %s"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()

        # Condicional para realiar la consulta a la base de datos

        if result is not None: # Si se encuentra el usuario en la base de datos, verificar la contraseña

            stored_password = result[0]

            if password == stored_password: # Si la contraseña se encuentra se muestra el siguiente mensaje

                page.add(ft.Text('Inicio de sesión exitoso'))

            else: # Si la contraseña no se encuentra se muestra el siguiente mensaje

                page.add(ft.Text('Contraseña incorrecta'))

        else: # Si el usuario no se encuentra en la base de datos se muestra el siguinete mensaje

            page.add(ft.Text('Usuario no encontrado'))

    def newuser(event): # Crea la funcion "NewUser"

        # Obtener el usuario y la contraseña ingresados por el usuario

        username = user.value
        password = key.value

        # Consultar la base de datos para verificar si el usuario ya existe

        check_sql = "SELECT user FROM users WHERE user = %s"
        cursor.execute(check_sql, (username,))
        existing_user = cursor.fetchone()

        if existing_user is not None: # Verifica que el usuario no exista

            # Si el usuario ya existe en la base de datos se muestra el siguiente mensaje
            page.add(ft.Text('Este Username ya se encuentra registrado, porfavor ingrese otro'))

        else:

            # Si el usuario no existe, lo registra

            insert_sql = "INSERT INTO users (user, password) VALUES (%s, %s)"
            params = (username, password)
            cursor.execute(insert_sql, params)
            conn.commit()
            page.add(ft.Text('Usuario registrado correctamente')) # Una ve reguistrado el usuario muestra el siguiente mensaje

    page.title = "Login" # Define el titulo de la ventana
    user = ft.TextField(hint_text="Username") # Crea un input con la etiqueta "Username"
    key = ft.TextField(hint_text="Password") # Crea un input con la etiqueta "Password"
    page.add(user) # Se muestra en pantalla el input "user"
    page.add(key) # Se muestra en pantalla el input "key"
    page.add(ft.ElevatedButton(text="Iniciar Sesión", on_click=login)) # Se crea un boton con la etiqueta "Iniciar Secion" que llama la funcion "Login" al ser pulsado
    page.add(ft.ElevatedButton(text="Registrarse", on_click=newuser)) # Se crea un boton con la etiqueta "Registrarse" que llama la funcion "NewUser" al ser pulsado

ft.app(target=main) # Llama la funcion "Main"
