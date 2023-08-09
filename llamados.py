import mysql.connector 
from mysql.connector import errors
import models
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

# funcionando
def create_server(name,description):
    query = "INSERT INTO servers (name,description) VALUES (%s,%s)"
    conn = bd.conectar()
    cur = conn.cursor()
    val = (name,description)
    cur.execute(query,val)
    conn.commit()
    conn.close()
    print(cur.rowcount, "Servidor creado")
# funcionando
def create_channel(name,server_id):
    query = "INSERT INTO channels (name,server_id) VALUES (%s,%s)"
    conn = bd.conectar()
    cur = conn.cursor()
    val = (name,server_id)
    cur.execute(query,val)
    conn.commit()
    conn.close()
    print(cur.rowcount, "Canal creado")  
# funcionando
def create_message(content,user_id,channel_id):
    query = "INSERT INTO messages (content,user_id,channel_id) VALUES (%s,%s,%s)"
    conn = bd.conectar()
    cur = conn.cursor()
    val = (content,user_id,channel_id)
    cur.execute(query,val)
    conn.commit()
    conn.close()
    print(cur.rowcount, "Mensaje creado")

def get_user(username):
    query = "SELECT * FROM users WHERE username = %s"
    conn = bd.conectar()
    cur = conn.cursor()
    val = (username,)
    cur.execute(query,val)
    conn.commit()
    conn.close()
    return cur.fetchone()

def get_servers_from_db():
    conn = bd.conectar()
    cursor = conn.cursor()
    query = "SELECT id, name, owner_id, description FROM servers"
    cursor.execute(query)
    resultados = cursor.fetchall()
    servidores = []
    for resultado in resultados:
        id = resultado[0]
        name = resultado[1]
        owner_id = resultado[2]
        description = resultado[3]
        servidor = models.Server(name, owner_id, description)
        servidor.id = id
        servidores.append(servidor)
    cursor.close()
    return servidores


def get_channels_from_db():
    conn = bd.conectar()
    cursor = conn.cursor()
    query = "SELECT id, name, server_id FROM channels"
    cursor.execute(query)
    resultados = cursor.fetchall()
    canales = []
    for resultado in resultados:
        id = resultado[0]
        name = resultado[1]
        server_id = resultado[2]
        canal = models.Channel(name, server_id)
        canal.id = id
        canales.append(canal)
    cursor.close()
    return canales

def get_messages_from_db():
    conn = bd.conectar()
    cursor = conn.cursor()
    query = "SELECT * FROM messages"
    cursor.execute(query)
    resultados = cursor.fetchall()
    mensajes = []
    for resultado in resultados:
        id = resultado[0]
        content = resultado[1]
        user_id = resultado[2]
        channel_id = resultado[3]
        mensaje = models.Message(content, user_id, channel_id)
        mensaje.id = id
        mensajes.append(mensaje)
    cursor.close()
    return mensajes
# mostrar los get_servers_from_db y get_channels_from_db

