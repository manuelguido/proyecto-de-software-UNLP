from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.estudiante import Estudiante
from flaskps.models.clase import Clase
from flaskps.models.responsable import Responsable
from flaskps.helpers.auth import authenticated
from flaskps.resources import forms

def store():
    if not authenticated(session):
        abort(401)

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'horario_new')):
        if request.method == "POST" and forms.ValidateHorario(request.form).validate():
            Clase.db = get_db()
            if Clase.noExiste(request.form):
                Clase.store(request.form)
                flash("Clase agregado correctamente" ,'success')
            else:
                flash("Ya existe esa clase" ,'error')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_horario'))
    else:
        abort(401)

def delete(id_data):
    if not authenticated(session):
        abort(401)

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'horario_destroy')):
        Clase.db = get_db()
        Clase.delete(id_data)
        flash("Se eliminó la clase correctamente" ,'success')
        return redirect(url_for('panel_horario'))
    else:
        abort(401)
