from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.docente import Docente
from flaskps.helpers.auth import authenticated
from flaskps.resources import forms

def store():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'docente_new')):
        if request.method == "POST" and forms.ValidateDocente(request.form).validate():
            Docente.db = get_db()
            Docente.store(request.form)
            flash("Docente agregado correctamente")
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_docentes'))
    else:
        abort(401)

def delete(id_data):
    if not authenticated(session):
        abort(401)

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'docente_destroy')):
        Docente.db = get_db()
        Docente.delete(id_data)
        flash("Se eliminó el docente correctamente")
        return redirect(url_for('panel_docentes'))
    else:
        abort(401)

def update():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'docente_update')):
        if request.method == "POST" and forms.ValidateDocente(request.form).validate():
            Docente.db = get_db()
            Docente.update(request.form)
            flash("Se actualizó el docente correctamente")
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_docentes'))
