from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.docente import Docente

def store():
    permisos = User.get_permisos(session['id'])
    params = request.form
    if request.method == "POST":
        Docente.db = get_db()
        Docente.store(params)
        flash("Docente agregado correctamente")
        return redirect(url_for('panel'))

def delete(id_data):
    Docente.db = get_db()
    Docente.delete(id_data)
    flash("Se eliminó el docente correctamente")
    return redirect(url_for('panel'))

def update():
    params = request.form
    if request.method == 'POST':
        Docente.db = get_db()
        Docente.update(params)
        flash("Se actualizó el docente correctamente")
        return redirect(url_for('panel'))
