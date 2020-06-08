import os
from flask import redirect, render_template, request, url_for, abort, session, flash, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.instrument import Instrument
from flaskps.models.instrument_type import InstrumentType
from flaskps.helpers import auth
from flaskps.resources import forms
from werkzeug.utils import secure_filename

#For naming files randomly
import random
import string
from datetime import date, datetime

#Forms & validation
from wtforms import Form
import wtforms_json
wtforms_json.init()

# UPLOAD_FOLDER = "../grupo37/flaskps/static/img/instruments/"
UPLOAD_FOLDER = "instrument_files/"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#---------------------------------------------------#
#   Retorna todos los insrtumentos
#---------------------------------------------------#
def all():
    #Auth check
    auth.authenticated_or_401()
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'instrumento_index')):
        abort(401)
    else:
        Instrument.db = get_db()
        return jsonify(Instrument.all())

#---------------------------------------------------#
#   Retorna el usuario por su id
#---------------------------------------------------#
def get(instrument_id):
    #Auth check
    auth.authenticated_or_401()
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'instrumento_show')):
        abort(401)
    else:
        Instrument.db = get_db()
        return jsonify(Instrument.get(instrument_id))

#---------------------------------------------------#
#   Crea un nuevo instrumento
#---------------------------------------------------#
def create():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        #Chequea permiso
        User.db = get_db()
        if (not User.has_permission(session['id'],'instrumento_new')):
            abort(401)
        else:
            form = forms.ValidateInstrument(request.form, skip_unknown_keys=True)
            if form.validate():
                file = request.files['image']
                if file: # and allowed_file(file.filename):
                    filename = new_file_name(file)
                    file.save(os.path.abspath(filename))
                    # file.save(os.path.abspath(UPLOAD_FOLDER2+filename))
                    Instrument.db = get_db()
                    Instrument.create(request.form, filename)

                    response_object = {'status': 'success', 'message': 'Se agregó el nuevo instrumento'}
                else:
                    response_object = {'status': 'warning', 'message': 'Debes subir una imagen para el instrumento.'}
            else:
                response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses nombres no permitidos.'}
            return jsonify(response_object)

#---------------------------------------------------#
#   Actualiza un instrumento
#---------------------------------------------------#
def update():
#Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        #Chequea permiso
        User.db = get_db()
        if (not User.has_permission(session['id'],'instrumento_update')):
            abort(401)
        else:
            post_data = request.form
            form = forms.ValidateInstrument(post_data, skip_unknown_keys=True)
            if not form.validate():
                response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses nombres no permitidos.'}
            else:
                file = request.files['image']
                Instrument.db = get_db()
                instrument = Instrument.get(post_data['instrument_id'])

                if file: # and allowed_file(file.filename):    
                    #Borrado de imagen anterior
                    # try:
                        #Borrado de imagen anterior y carga de nueva
                    os.remove(os.path.abspath(UPLOAD_FOLDER+instrument['image']))
                    filename = new_file_name(file)
                    file.save(os.path.abspath(UPLOAD_FOLDER+filename))
                    # except:
                        #Solo carga de nueva
                        # filename = new_file_name(file)
                        # file.save(os.path.abspath(UPLOAD_FOLDER+filename))
                    # post_data['image'] = filename
                else:
                    filename = instrument['image']
        
                Instrument.update(post_data, filename)
                response_object = {'status': 'success', 'message': 'Se actualizó el instrumento'}

            return jsonify(response_object)

#---------------------------------------------------#
#   Elimina un instrumento
#---------------------------------------------------#
def delete():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'instrumento_destroy')):
        abort(401)
    else:
        Instrument.db = get_db()
        #Obtención de información
        post_data = request.get_json()
        #Obtiene el instrumento
        instrument = Instrument.get(post_data['instrument_id'])
        #Borrado de imagen
        try:
            #Borrado de imagen e instrumento
            os.remove(os.path.abspath(UPLOAD_FOLDER+instrument['image']))
            Instrument.delete(post_data['instrument_id'])
        except:
            #Solo borrado de instrumento
            Instrument.delete(post_data['instrument_id'])

        return jsonify({'status': 'success', 'message': 'Se eliminó el instrumento correctamente'})

#---------------------------------------------------#
#   Información para los formularios
#---------------------------------------------------#
def getFormData():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'instrumento_new')):
        abort(401)
    else:
        InstrumentType.db = get_db()
        response_json = {'instrument_types': InstrumentType.all()}
        return response_json

#---------------------------------------------------#
#   Crea un nombre de archivo para un instrumento
#---------------------------------------------------#
def new_file_name(file):
    today = str(date.today().strftime("%Y-%m-%d-"))
    now = str(datetime.now().strftime("%H-%M-%S-"))
    random_string = str(''.join(random.choice(string.ascii_letters) for i in range(10)))
    original_filename = str(secure_filename(file.filename))
    return str(today+now+random_string+original_filename)