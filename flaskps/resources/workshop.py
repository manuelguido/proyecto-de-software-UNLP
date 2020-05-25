from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.usuario import Usuario
from flaskps.models.ciclo import Ciclo
from flaskps.models.taller import Taller
from flaskps.models.responsable import Responsable
from flaskps.helpers.auth import authenticated
from flaskps.resources import forms

def deleteTallerCiclo():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    Usuario.db = get_db()
    if (Usuario.tiene_permiso(session['id'],'administrativo_destroy')):
        if request.method == "POST" and forms.ValidateCicloTaller(request.form).validate():
            Taller.db = get_db()
            Taller.deleteTallerCiclo(request.form)
            flash("Se desasigno el taller del ciclo lectivo correctamente" ,'success')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_talleres'))
    else:
        abort(401)

def storeTallerCiclo():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    Usuario.db = get_db()
    if (Usuario.tiene_permiso(session['id'],'administrativo_new')):
        if request.method == "POST" and forms.ValidateCicloTaller(request.form).validate():
            Ciclo.db = get_db()
            Taller.db = get_db()
            if Ciclo.cicloNoTieneTaller(request.form):
                Taller.storeConTaller(request.form)
                flash("Se agrego el taller al ciclo lectivo correctamente" ,'success')
            else:
                flash("El taller ya esta asignado al ciclo lectivo seleccionado", 'error')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_talleres'))
    else:
        abort(401)
