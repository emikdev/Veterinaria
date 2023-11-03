import mysql.connector # Importa la libreria MySql-Connector

    # Se crea la coneccion con la base de datos y se la sentencia a traves de la cual se accedera a la Base de Datos

conn = mysql.connector.connect(
    host="localhost", user="root", password="root", database="veterinary"
)

cursor = conn.cursor()