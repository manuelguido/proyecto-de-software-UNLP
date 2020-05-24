from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.estudiante import Estudiante
from flaskps.models.asistencia import Asistencia
from flaskps.helpers.auth import authenticated
from flaskps.resources import forms

def storeAsistencia():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'estudiante_new')):
        if request.method == "POST" and forms.ValidateAsistencia(request.form).validate():
            Asistencia.db = get_db()
            if Asistencia.noExiste(request.form):
                Asistencia.storeAsistencia(request.form)
                flash("Se guardó la asistencia" ,'success')
            else:
                flash('Ya se tomo esa asistencia', 'error')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for("ver_asistencias", id_data=request.form.get("clase_id")))
    else:
        abort(401)

def storeInasistencia():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'estudiante_new')):
        if request.method == "POST" and forms.ValidateAsistencia(request.form).validate():
            Asistencia.db = get_db()
            if Asistencia.noExiste(request.form):
                Asistencia.storeInasistencia(request.form)
                flash("Se guardó la inasistencia" ,'success')
            else:
                flash('Ya se tomo esa asistencia', 'error')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for("ver_asistencias", id_data=request.form.get("clase_id")))
    else:
        abort(401)
