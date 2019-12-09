from flask import redirect, render_template, request, url_for, session, abort, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.helpers.auth import authenticated
from flaskps.resources import forms

def update_user_status():
    if not authenticated(session):
        abort(401)
    
    #Chequea permiso
    if (User.tiene_permiso(session['id'],'usuario_update')):
        if request.method == "POST" and forms.ValidateStudent(request.form).validate():
            User.db = get_db()
            User.update_user_status(request.form)
            flash("Estudiante agregado correctamente")
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_estudiantes'))
    else:
        abort(401)

def new():
    if not authenticated(session):
        abort(401)

    if request.method == "POST":
        params = request.form
        User.db = get_db()
        User.create(params)
        return redirect(url_for('panel_usuarios'))

def delete():
    if not authenticated(session):
        abort(401)

    params = request.form
    User.db = get_db()
    User.delete(params)
    return redirect(url_for('panel_usuarios'))