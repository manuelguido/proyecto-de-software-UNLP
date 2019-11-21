from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.student import Student
from flaskps.helpers.auth import authenticated

def store():
    if not authenticated(session):
        abort(401)

    params = request.form
    if request.method == "POST":
        Student.db = get_db()
        Student.store(params)
        flash("Estudiante agregado correctamente")
        return redirect(url_for('panel'))

def delete(id_data):
    if not authenticated(session):
        abort(401)

    Student.db = get_db()
    Student.delete(id_data)
    flash("Se eliminó el estudiante correctamente")
    return redirect(url_for('panel'))

def update():
    if not authenticated(session):
        abort(401)

    params = request.form
    if request.method == 'POST':
        Student.db = get_db()
        Student.update(params)
        flash("Se actualizó el estudiante correctamente")
        return redirect(url_for('panel'))
