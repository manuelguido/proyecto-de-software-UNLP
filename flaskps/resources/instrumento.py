import os
from flask import redirect, render_template, request, url_for, abort, session, flash
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.instrumento import Instrumento
from flaskps.helpers.auth import authenticated
from flaskps.resources import forms
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "../grupo37/flaskps/static/img/instrumentos"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def store():
    if not authenticated(session):
        abort(401)
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
            Instrumento.db = get_db()
            Instrumento.store(request.form)
            flash("Instrumento agregado correctamente" ,'success')
            return redirect(url_for('panel_instrumentos'))
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
            return redirect(url_for('new_instrumento'))
    else:
        abort(401)

def delete(id_data):
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'instrumento_destroy')):
        Instrumento.db = get_db()
        Instrumento.delete(id_data)
        flash("Se eliminó el instrumento correctamente" ,'success')
        return redirect(url_for('panel_instrumentos'))
    else:
        abort(401)

def update():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'instrumento_update')):
        if request.method == "POST" and forms.ValidateInstrument(request.form).validate():
            Instrumento.db = get_db()
            Instrumento.update(request.form)
            flash("Se actualizó el instrumento correctamente" ,'success')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for("get_update_instrumento", id_data=request.form.get("id_data")))
    else:
        abort(401)
