from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.docente import Docente
from flaskps.helpers.auth import authenticated

def store():
    if not authenticated(session):
        abort(401)

    params = request.form
    if request.method == "POST":
        Docente.db = get_db()
        Docente.store(params)
        flash("Docente agregado correctamente")
        return redirect(url_for('panel_empleados'))

def delete(id_data):
    if not authenticated(session):
        abort(401)

    Docente.db = get_db()
    Docente.delete(id_data)
    flash("Se eliminó el docente correctamente")
    return redirect(url_for('panel_empleados'))

def update():
    if not authenticated(session):
        abort(401)

    params = request.form
    if request.method == 'POST':
        Docente.db = get_db()
        Docente.update(params)
        flash("Se actualizó el docente correctamente")
        return redirect(url_for('panel_empleados'))
