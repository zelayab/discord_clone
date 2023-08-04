from flask import Flask, app, redirect, render_template, request, session
import mysql.connector
from mysql.connector import errors
import datos
import llamados
import bd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

def conectar():
    try:
        conn = mysql.connector.connect(**datos.credenciales)
    except errors.DatabaseError as err:
        print("Error al conectar a la base de datos.", err)
    else:
        return conn

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los datos de inicio de sesión del formulario
        data = request.form
        username = data['username']
        password = data['password']

        # Realizar la consulta SQL para obtener el usuario
        conn = bd.conectar()
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        # Cerrar el cursor después de obtener el resultado de la consulta
        cursor.close()

        if user:
            # Autenticar al usuario
            session['logged_in'] = True
            session['user_id'] = user[0]  # Guardar el ID del usuario en la sesión
            return redirect('/index.html')  # Redirigir al usuario a la página raíz (login)
        else:
            # Usuario no encontrado, mostrar el mensaje de sugerencia de registro
            return render_template('auth/login.html', suggest_register=True)

    return render_template('auth/login.html')

@app.route('/index.html')
def index_html():
    logged_in = session.get('logged_in')
    if not logged_in:
        return redirect('/')

    # Aquí debes obtener las listas server_list, channel_list, y message_list
    # Puedes hacerlo utilizando las funciones que ya has definido para obtener los datos desde la base de datos.
    server_list = llamados.obtener_servidores_desde_db()
    print(server_list[0].name)
    return render_template('index.html', server_list=server_list, logged_in=logged_in)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    return redirect('/')
""" lo primero que renderiza la app al entrar es el login """



""" iniciar app """
if __name__ == '__main__':
    app.run(debug=True)


    