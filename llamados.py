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

create_message("basura japishh!!",1,2)


def get_server(name):
    query = "SELECT * FROM servers WHERE name = %s"
    conn = bd.conectar()
    cur = conn.cursor()
    val = (name,)
    cur.execute(query,val)
    conn.commit()
    conn.close()
    return cur.fetchone()

def get_channel(name):
    query = "SELECT * FROM channels WHERE name = %s"
    conn = bd.conectar()
    cur = conn.cursor()
    val = (name,)
    cur.execute(query,val)
    conn.commit()
    conn.close()
    return cur.fetchone()

def get_message(content):
    query = "SELECT * FROM messages WHERE content = %s"
    conn = bd.conectar()
    cur = conn.cursor()
    val = (content,)
    cur.execute(query,val)
    conn.commit()
    conn.close()
    return cur.fetchone()

def get_user_by_id(id):
    query = "SELECT * FROM users WHERE id = %s"
    conn = bd.conectar()
    cur = conn.cursor()
    val = (id,)
    cur.execute(query,val)
    conn.commit()
    conn.close()
    return cur.fetchone()