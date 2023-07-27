import mysql.connector
from mysql.connector import errors
import datos

def conectar():
    try:
        conn = mysql.connector.connect(**datos.credenciales)
    except errors.DatabaseError as err:
        print("Error al conectar a la base de datos.", err)
    else:
        return conn
    



    