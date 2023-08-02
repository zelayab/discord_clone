import mysql.connector 
from mysql.connector import errors
import datos
import bd
# funcionando
def create_user (username,password,email):
    query = "INSERT INTO users (username,password,email) VALUES (%s,%s,%s)"
    conn = bd.conectar()
    cur = conn.cursor()
    val = (username,password,email)
    cur.execute(query,val)    
    conn.commit()
    conn.close()    
    print(cur.rowcount, "Usuario creado")


def create_server(name,description):
    query = "INSERT INTO servers (name,description) VALUES (%s,%s)"
    conn = bd.conectar()
    cur = conn.cursor()
    val = (name,description)
    cur.execute(query,val)
    conn.commit()
    conn.close()
    print(cur.rowcount, "Servidor creado")

def create_channel(name,server_id):
    query = "INSERT INTO channels (name,server_id) VALUES (%s,%s)"
    conn = bd.conectar()
    cur = conn.cursor()
    val = (name,server_id)
    cur.execute(query,val)
    conn.commit()
    conn.close()
    print(cur.rowcount, "Canal creado")  



create_server("Server1","Descripcion1")