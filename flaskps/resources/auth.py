from flask import redirect, render_template, request, url_for, abort, session, flash, g
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.resources import forms

def login():
    #Si esta autenticado, va derecho al panel
    if authenticated():
        return redirect(url_for('panel_estudiantes'))    
    return render_template('auth/login.html')

def authenticate():
    params = request.form
    #Validacion de formulario
    form = forms.Login(request.form)
    if form.validate():
        #Busco usuario
        User.db = get_db()
        user = User.find_by_email_and_pass(params['email'], params['password'])
    else:
        flash("Ingrese email y contraseña")
        return redirect(url_for('auth_login'))

    #Usuario no existe
    if not user:
        flash("Email o contraseña incorrectos")
        return redirect(url_for('auth_login'))

    #Usuario no activo
    if not user['activo']:
        flash("Usuario desactivado.")
        return redirect(url_for('auth_login'))

    #Variables de sesion
    session['id'] = user['id']
    session['user'] = user['username']
    session['email'] = user['email']
    session['nombre'] = user['first_name']
    session['apellido'] = user['last_name']

    return redirect(url_for('panel_estudiantes'))

def authenticated():
    #Si el usuario esta autenticado retora 1(verdadero), sino retorna 0
    g.user = None
    if 'user' in session:
        g.user = session['user']
        return 1
    return 0

def logout():
    del session['id']
    del session['user']
    del session['email']
    del session['nombre']
    del session['apellido']
    session.clear()

    return redirect(url_for('auth_login'))
