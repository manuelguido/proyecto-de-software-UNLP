from flask import redirect, render_template, request, url_for, abort, session, flash, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.teacher import Teacher
from flaskps.helpers import auth
from flaskps.resources import forms

def all():
    #Auth check
    auth.authenticated_or_401()

    Teacher.db = get_db()
    return jsonify(Teacher.all())

def get(id_data):
    #Auth check
    auth.authenticated_or_401()

    Teacher.db = get_db()
    return jsonify(Teacher.get(id_data))


def store():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'docente_new')):
        if request.method == "POST" and forms.ValidateDocente(request.form).validate():
            Teacher.db = get_db()
            Teacher.store(request.form)
            flash("Docente agregado correctamente" ,'success')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_docentes'))
    else:
        abort(401)

def delete(id_data):
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'docente_destroy')):
        Teacher.db = get_db()
        Teacher.delete(id_data)
        flash("Se eliminó el docente correctamente" ,'success')
        return redirect(url_for('panel_docentes'))
    else:
        abort(401)

def update():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'docente_update')):
        if request.method == "POST" and forms.ValidateDocente(request.form).validate():
            Teacher.db = get_db()
            Teacher.update(request.form)
            flash("Se actualizó el docente correctamente" ,'success')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_docentes'))

def deleteDocenteTaller():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'administrativo_destroy')):
        if request.method == "POST" and forms.ValidateDocenteTallerDelete(request.form).validate():
            Teacher.db = get_db()
            Teacher.deleteDocenteTaller(request.form)
            flash("Se desasigno el docente del taller correctamente" ,'success')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_docentes_taller'))
    else:
        abort(401)

def storeDocenteTaller():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'administrativo_new')):
        if request.method == "POST" and forms.ValidateDocenteTaller(request.form).validate():
            Teacher.db = get_db()
            if Teacher.tallerNoTieneDocente(request.form):
                Teacher.storeDocenteTaller(request.form)
                flash("Se agrego el taller al ciclo lectivo correctamente" ,'success')
            else:
                flash("El docente ya esta asignado al taller para el ciclo lectivo seleccionado", 'error')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_docentes_taller'))
    else:
        abort(401)
