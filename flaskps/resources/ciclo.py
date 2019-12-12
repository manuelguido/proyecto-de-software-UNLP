from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.ciclo import Ciclo
from flaskps.models.taller import Taller
from flaskps.models.responsable import Responsable
from flaskps.helpers.auth import authenticated
from flaskps.resources import forms

def store():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'administrativo_new')):
        if request.method == "POST" and forms.ValidateCiclo(request.form).validate():
            Ciclo.db = get_db()
            if Ciclo.semestreNoExiste(request.form):
                Ciclo.store(request.form)
                flash("Ciclo lectivo agregado correctamente")
            else:
                flash("El semestre ya tiene un ciclo lectivo asignado", 'error')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_ciclos'))
    else:
        abort(401)

def delete(id_data):
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'administrativo_destroy')):
        Ciclo.db = get_db()
        Ciclo.delete(id_data)
        flash("Se eliminó el ciclo lectivo correctamente")
        return redirect(url_for('panel_ciclos'))
    else:
        abort(401)

def ciclo_taller():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'administrativo_new')):
        if request.method == "POST" and forms.ValidateCicloTaller(request.form).validate():
            Ciclo.db = get_db()
            if Ciclo.cicloNoTieneTaller(request.form):
                Ciclo.storeConTaller(request.form)
                flash("Se agrego el taller al ciclo lectivo correctamente")
            else:
                flash("El taller ya esta asignado al ciclo lectivo seleccionado", 'error')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_ciclos'))
    else:
        abort(401)

def taller_docente():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'administrativo_new')):
        if request.method == "POST" and forms.ValidateTallerDocente(request.form).validate():
            Taller.db = get_db()
            if Taller.tallerNoTieneDocente(request.form):
                Taller.storeConDocente(request.form)
                flash("Se agrego el taller al ciclo lectivo correctamente")
            else:
                flash("El taller ya esta asignado al ciclo lectivo seleccionado", 'error')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_ciclos'))
    else:
        abort(401)
