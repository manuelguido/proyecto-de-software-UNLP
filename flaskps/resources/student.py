from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.student import Student
from flaskps.models.responsable import Responsable
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
            flash("Estudiante agregado correctamente" ,'success')
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
    if (User.tiene_permiso(session['id'],'estudiante_destroy')):
        Student.db = get_db()
        Student.delete(id_data)
        flash("Se eliminó el estudiante correctamente" ,'success')
        return redirect(url_for('panel_estudiantes'))
    else:
        abort(401)

def update():
    if not authenticated(session):
        abort(401)

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'estudiante_update')):
        if request.method == "POST" and forms.ValidateStudent(request.form).validate():
            Student.db = get_db()
            Student.update(request.form)
            flash("Se actualizó el estudiante correctamente" ,'success')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_estudiantes'))
    else:
        abort(401)

def deleteEstudianteDocente():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'administrativo_destroy')):
        if request.method == "POST" and forms.ValidateEstudianteDocenteTallerDelete(request.form).validate():
            Student.db = get_db()
            Student.deleteEstudianteTaller(request.form)
            flash("Se desasigno el estudiante del taller correctamente" ,'success')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_estudiantes_docentes'))
    else:
        abort(401)

def storeEstudianteDocente():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'administrativo_new')):
        if request.method == "POST" and forms.ValidateEstudianteDocenteTaller(request.form).validate():
            Student.db = get_db()
            if Student.estudianteNoEnTaller(request.form):
                Student.storeEstudianteTaller(request.form)
                flash("Se asigno el estudiante al taller correctamente" ,'success')
            else:
                flash("El estudiante ya esta asignado al taller", 'error')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_estudiantes_docentes'))
    else:
        abort(401)
