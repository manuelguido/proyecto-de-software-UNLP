import os
from flask import redirect, render_template, request, url_for, abort, session, flash, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.instrument import Instrument
from flaskps.helpers import auth
from flaskps.resources import forms
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "../grupo37/flaskps/static/img/instrumentos"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def all():
    #Auth check
    auth.authenticated_or_401()

    Instrument.db = get_db()
    return jsonify(Instrument.all())

def get(id_data):
    #Auth check
    auth.authenticated_or_401()

    Instrument.db = get_db()
    return jsonify(Instrument.get(id_data))


def store():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'instrumento_new')):
        if request.method == "POST" and forms.ValidateInstrument(request.form).validate():
            #file = request.files['img']
            #if file:# and allowed_file(file.filename):
            #    filename = secure_filename(file.filename)
            #    file.save(os.path.abspath(UPLOAD_FOLDER+filename))
            #else:
            #    flash('Imagen inválida. Solo se permite JPG o PNG', 'error')
            #    return redirect(url_for('new_instrumento'))
            Instrument.db = get_db()
            Instrument.store(request.form)
            flash("Instrumento agregado correctamente" ,'success')
            return redirect(url_for('panel_instrumentos'))
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
            return redirect(url_for('new_instrumento'))
    else:
        abort(401)

def delete(id_data):
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'instrumento_destroy')):
        Instrument.db = get_db()
        Instrument.delete(id_data)
        flash("Se eliminó el instrumento correctamente" ,'success')
        return redirect(url_for('panel_instrumentos'))
    else:
        abort(401)

def update():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'instrumento_update')):
        if request.method == "POST" and forms.ValidateInstrument(request.form).validate():
            Instrument.db = get_db()
            Instrument.update(request.form)
            flash("Se actualizó el instrumento correctamente" ,'success')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for("get_update_instrumento", id_data=request.form.get("id_data")))
    else:
        abort(401)
