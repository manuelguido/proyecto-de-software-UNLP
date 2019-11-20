from flask import redirect, render_template, request, url_for, abort, session, flash, g
from flaskps.db import get_db
from flaskps.models.user import User

def authenticated():
    #Si el usuario esta autenticado retora 1(verdadero), sino retorna 0
    g.user = None
    if 'user' in session:
        g.user = session['user']
        return 1
    return 0

def login():
    #Si esta autenticado, va derecho al panel
    if authenticated():
        return redirect(url_for('panel'))    
    return render_template('auth/login.html')


def authenticate():
    params = request.form

    User.db = get_db()
    user = User.find_by_email_and_pass(params['email'], params['password'])

    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for('auth_login'))

    session['id'] = user['id']
    session['user'] = user['username']
    session['email'] = user['email']
    session['nombre'] = user['first_name']
    session['apellido'] = user['last_name']

    return redirect(url_for('panel'))


def logout():
    del session['id']
    del session['user']
    del session['email']
    del session['nombre']
    del session['apellido']
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for('auth_login'))
