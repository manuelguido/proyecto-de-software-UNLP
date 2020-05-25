from flask import redirect, render_template, request, url_for, abort, session, flash, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.cycle import Cycle
from flaskps.models.workshop import Workshop
from flaskps.models.responsable import Responsable
from flaskps.helpers import auth
from flaskps.resources import forms

def all():
    #Auth check
    auth.authenticated_or_401()

    Cycle.db = get_db()
    return jsonify(Cycle.all())

def get(id_data):
    #Auth check
    auth.authenticated_or_401()

    Cycle.db = get_db()
    return jsonify(Cycle.get(id_data))

def store():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'administrativo_new')):
        if request.method == "POST" and forms.ValidateCiclo(request.form).validate():
            if int(request.form['año']) < int(1990) or int(request.form['año']) > int(2025):
                flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
            else:
                Cycle.db = get_db()
                if not Cycle.semestreExiste(request.form):
                    Cycle.store(request.form)
                    flash("Ciclo lectivo agregado correctamente" ,'success')
                else:
                    flash("El semestre ya tiene un ciclo lectivo asignado", 'error')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_ciclos'))
    else:
        abort(401)

def delete(id_data):
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'administrativo_destroy')):
        Cycle.db = get_db()
        Cycle.delete(id_data)
        flash("Se eliminó el ciclo lectivo correctamente" ,'success')
        return redirect(url_for('panel_ciclos'))
    else:
        abort(401)

def update():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'administrativo_update')):
        if request.method == "POST" and forms.ValidateCiclo(request.form).validate():
            Cycle.db = get_db()
            Cycle.update(request.form)
            flash("Se actualizó el ciclo lectivo correctamente" ,'success')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
            return redirect(url_for("get_update_ciclo", id_data=request.form.get("id_data")))
        return redirect(url_for('panel_ciclos'))
    else:
        abort(401)
