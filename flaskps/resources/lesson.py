from flask import redirect, render_template, request, url_for, abort, session, flash, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.student import Student
from flaskps.models.lesson import Lesson
from flaskps.models.responsable import Responsable
from flaskps.helpers import auth
from flaskps.resources import forms

def all():
    #Auth check
    auth.authenticated_or_401()

    Lesson.db = get_db()
    return jsonify(Lesson.all())

def get(id_data):
    #Auth check
    auth.authenticated_or_401()

    Lesson.db = get_db()
    return jsonify(Lesson.get(id_data))

def store():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'horario_new')):
        if request.method == "POST" and forms.ValidateHorario(request.form).validate():
            Lesson.db = get_db()
            # if Lesson.noExiste(request.form):
                # Lesson.store(request.form)
                # flash("Clase agregado correctamente" ,'success')
            # else:
                # flash("Ya existe esa clase" ,'error')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_horario'))
    else:
        abort(401)

def delete(id_data):
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'horario_destroy')):
        Lesson.db = get_db()
        Lesson.delete(id_data)
        flash("Se eliminó la clase correctamente" ,'success')
        return redirect(url_for('panel_horario'))
    else:
        abort(401)
