from flask import Blueprint, request, render_template, session, url_for, redirect,flash
# from ..controller.userController import userController
from ..models.user import User



user_bp = Blueprint('user_bp', __name__)



@user_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username = data['username']
        password = data['password']        
        user = User.get_user(username, password)
        if user:
            print("entro en user")
            session['logged_in'] = True            
            session['user_id'] = user.id            
            return render_template('index.html', logged_in=True)       
        else:
            return render_template('auth/login.html', error=True)

    return render_template('auth/login.html')

# @user_bp.route('/', methods=['GET'])
# def home():
#     if session.get('logged_in'):
#         return render_template('index.html')
    
    

@user_bp.route('/register', methods=['GET' ,'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        print(username, password, email)

        user = User.create_user(username, password, email)

        return redirect('/')

    return render_template('auth/register.html')


@user_bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('/')

@user_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    logged_in = session.get('logged_in')
    if not logged_in:
        return redirect('/')

    user_id = session.get('user_id')
    user = User.get_user(username=None, password=None )

    if request.method == 'POST':
        data = request.form
        new_email = data['new_email']
        new_password = data['new_password']
        confirm_new_password = data['confirm_new_password']

        if new_password == confirm_new_password:
            User.update_user(user_id, new_email, new_password)
            flash("Se han actualizado los datos exitosamente", "success")
            return redirect('/profile')
        else:
            return "Las contraseñas no coinciden"
    
    return render_template('profile/profile.html', user=user, logged_in=logged_in)



# @user_bp.route('/update_user/<int:id>', methods=['GET', 'POST'])
# def update_user(id):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        print(username, password, email)

        user = userController.update_user(id, username, password, email)

        return redirect(url_for('auth/login.html'))

    return render_template('profile/profile.html')

