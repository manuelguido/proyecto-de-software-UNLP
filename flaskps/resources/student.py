from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.student import Student

def store():
    params = request.form
    if request.method == "POST":
        Student.db = get_db()
        Student.store(params)
        flash("Estudiante agregado correctamente")
        #return redirect(url_for('panel'))
        #render_template('auth/panel.html')

def delete(id_data):
    Student.db = get_db()
    Student.delete(id_data)
    flash("Se eliminó el estudiante correctamente")

def update(request):
    params = request.form
    if request.method == 'POST':
        Student.db = get_db()
        Student.update(params)
        flash("Se actualizó el estudiante correctamente")
