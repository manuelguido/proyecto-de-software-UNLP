from flask import redirect, render_template, request, url_for, abort, session, flash, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.cycle import Cycle
from flaskps.models.workshop import Workshop
from flaskps.models.semester import Semester
from flaskps.helpers import auth
from flaskps.resources import forms

#Forms & validation
from wtforms import Form
import wtforms_json
wtforms_json.init()

#---------------------------------------------------#
#   Retorna todos los ciclos lectivos
#---------------------------------------------------#
def all():
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'administrativo_index')):
        abort(401)
    else:
        Cycle.db = get_db()
        return jsonify(Cycle.all())

#---------------------------------------------------#
#   Retorna el ciclo lectivo por su id
#---------------------------------------------------#
def get(cycle_id):
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'administrativo_show')):
        abort(401)
    else:
        Cycle.db = get_db()
        return jsonify(Cycle.get(cycle_id))

#---------------------------------------------------#
#   Crea un ciclo lectivo
#---------------------------------------------------#
def create():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        #Chequea permiso
        User.db = get_db()
        if (not User.has_permission(session['id'],'administrativo_new')):
            abort(401)
        else:
            post_data = request.get_json()
            #Form validation
            form = forms.ValidateCycle.from_json(post_data, skip_unknown_keys=False)
            if not form.validate():
                response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
            else:
                Cycle.db = get_db()
                if Cycle.cycle_exists(post_data):
                    response_object = {'status': 'warning', 'message': 'El semestre ya tiene un ciclo lectivo asignado.'}
                else:
                    Cycle.create(post_data)
                    response_object = {'status': 'success', 'message': 'Creaste el ciclo lectivo correctamente.'}
            return jsonify(response_object)

#---------------------------------------------------#
#   Actualiza un ciclo lectivo
#---------------------------------------------------#
def update():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        #Chequea permiso
        User.db = get_db()
        if (not User.has_permission(session['id'],'administrativo_update')):
            abort(401)
        else:
            post_data = request.get_json()
            #Form validation
            form = forms.ValidateCycle.from_json(post_data, skip_unknown_keys=True)
            if not form.validate():
                response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
            else:
                Cycle.db = get_db()
                if Cycle.cycle_exists_not_self(post_data):
                    response_object = {'status': 'warning', 'message': 'El semestre ya tiene un ciclo lectivo asignado.'}
                else:
                    Cycle.update(post_data)
                    response_object = {'status': 'success', 'message': 'Actualizaste el ciclo lectivo correctamente.'}
            return jsonify(response_object)

#---------------------------------------------------#
#   Elimina un ciclo lectivo
#---------------------------------------------------#
def delete():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        #Chequea permiso
        User.db = get_db()
        if (not User.has_permission(session['id'],'administrativo_destroy')):
            abort(401)
        else:
            post_data = request.get_json()
            #Form validation
            form = forms.ValidateCycleId.from_json(post_data, skip_unknown_keys=True)
            if not form.validate():
                response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
            else:
                Cycle.db = get_db()
                Cycle.delete(post_data['cycle_id'])
                response_object = {'status': 'success', 'message': 'Eliminaste el ciclo lectivo correctamente.'}
                return jsonify(response_object)

#---------------------------------------------------#
#   Información para los formularios
#---------------------------------------------------#
def getFormData():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'administrativo_new')):
        abort(401)
    else:
        Semester.db = get_db()
        response_json = {'semesters': Semester.all()}
        return response_json