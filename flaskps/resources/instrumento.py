from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.instrumento import Instrumento
from flaskps.helpers.auth import authenticated
from flaskps.resources import forms

def store():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'instrumento_new')):
        if request.method == "POST" and forms.ValidateUserActive(request.form).validate():
            Instrumento.db = get_db()
            Instrumento.store(request.form)
            flash("Instrumento agregado correctamente")
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_estudiantes'))
    else:
        abort(401)

def delete(id_data):
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'instrumento_destroy')):
        Instrumento.db = get_db()
        Instrumento.delete(id_data)
        flash("Se eliminó el instrumento correctamente")
        return redirect(url_for('panel_estudiantes'))
    else:
        abort(401)

def update():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    if (User.tiene_permiso(session['id'],'instrumento_update')):
        if request.method == "POST" and forms.ValidateStudent(request.form).validate():
            Instrumento.db = get_db()
            Instrumento.update(request.form)
            flash("Se actualizó el instrumento correctamente")
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_estudiantes'))
    else:
        abort(401)
