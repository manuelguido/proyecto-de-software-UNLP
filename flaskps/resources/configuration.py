from flask import redirect, render_template, request, url_for, flash, session, abort, jsonify
from flaskps.db import get_db
from flaskps.models.configuration import Configuration
from flaskps.models.user import User
from flaskps.resources import forms
from flaskps.helpers import auth

#Forms & validation
from wtforms import Form
import wtforms_json
wtforms_json.init()

def all():
    Configuration.db = get_db()
    return jsonify(Configuration.all())

#Actualizar la informacion del sitio (Titulo, descripcion e email)
def update():
    #Auth check
    auth.authenticated_or_401()

    if request.method == 'POST':
        #Chequea permiso
        User.db = get_db()
        if (not User.has_permission(session['id'],'configuration_all')):
            abort(401)
        else:
            #Chequea el metodo y valida el formulario
            post_data = request.get_json()
            form = forms.ValidateConfiguration.from_json(post_data, skip_unknown_keys=False)
            if form.validate():
                Configuration.db = get_db()
                Configuration.update(post_data)
                response_object = {'status': 'success', 'message': 'Se actualizó la información del sitio correctamente'}
            else:
                response_object = {'status': 'error', 'message': 'Informacion inválida, solo puede ingresarse un titulo(máximo 255 char), email(máximo 255 char) y descripción(máximo 1000 char)'}
            return jsonify(response_object)
