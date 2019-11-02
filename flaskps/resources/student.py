from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.student import Student

def store(request):
    if request.method == "POST":
        Student.db = get_db()
        Student.store(request.form)
        flash("Estudiante agregado correctamente")

def delete(id_data):
    Student.db = get_db()
    Student.delete(id_data)
    flash("Se eliminó el estudiante correctamente")

def update(request):
    if request.method == 'POST':
        Student.db = get_db()
        Student.update(request)
        flash("Se actualizó el estudiante correctamente")
