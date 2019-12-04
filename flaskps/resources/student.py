from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.student import Student
from flaskps.helpers.auth import authenticated
from flaskps.resources import forms

def store():
    if not authenticated(session):
        abort(401)

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'estudiante_new')):
        if request.method == "POST" and forms.ValidateStudent(request.form).validate():
            Student.db = get_db()
            Student.store(request.form)
            flash("Estudiante agregado correctamente")
        else:
            flash('Los campos deben estar todos completos', 'error')
        return redirect(url_for('panel_estudiantes'))
    else:
        abort(401)

def delete(id_data):
    if not authenticated(session):
        abort(401)

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'estudiante_destroy')):
        Student.db = get_db()
        Student.delete(id_data)
        flash("Se eliminó el estudiante correctamente")
        return redirect(url_for('panel_estudiantes'))
    else:
        abort(401)

def update():
    if not authenticated(session):
        abort(401)

    #Chequea permiso
    if (User.tiene_permiso(session['id'],'estudiante_update')):
        if request.method == "POST" and forms.ValidateStudent(request.form).validate():
            Student.db = get_db()
            Student.update(request.form)
            flash("Se actualizó el estudiante correctamente")
        else:
            flash('Los campos deben estar todos completos', 'error')
        return redirect(url_for('panel_estudiantes'))
    else:
        abort(401)
