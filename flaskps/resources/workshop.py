from flask import request, abort, session, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.workshop import Workshop
from flaskps.models.cycle import Cycle
from flaskps.models.cycle_workshop import CycleWorkshop
from flaskps.helpers import auth
from flaskps.resources import forms

#Forms & validation
from wtforms import Form
import wtforms_json
wtforms_json.init()

#---------------------------------------------------#
#   Retorna todos los talleres
#---------------------------------------------------#
def all():
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'administrativo_index')):
        abort(401)
    else:
        Workshop.db = get_db()
        return jsonify(Workshop.all())

#---------------------------------------------------#
#   Retorna todos los ciclos lectivos asignados
#---------------------------------------------------#
def all_cycle_workshop():
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'administrativo_index')):
        abort(401)
    else:
        CycleWorkshop.db = get_db()
        return jsonify(CycleWorkshop.all())

#---------------------------------------------------#
#   Retorna el taller por su id
#---------------------------------------------------#
def get(workshop_id):
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'administrativo_show')):
        abort(401)
    else:
        Workshop.db = get_db()
        return jsonify(Workshop.get(workshop_id))

#---------------------------------------------------#
#   Retorna el taller por su id
#---------------------------------------------------#
def get_cycle_workshop(cycle_workshop_id):
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'administrativo_show')):
        abort(401)
    else:
        CycleWorkshop.db = get_db()
        return jsonify(CycleWorkshop.get(cycle_workshop_id))

#---------------------------------------------------#
#   Crea un taller
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
            form = forms.ValidateWorkshop.from_json(post_data, skip_unknown_keys=True)
            if not form.validate():
                response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
            else:
                Workshop.db = get_db()
                if Workshop.workshop_exists(post_data):
                    response_object = {'status': 'warning', 'message': 'El taller ya existe.'}
                else:
                    Workshop.create(post_data)
                    response_object = {'status': 'success', 'message': 'Creaste el taller correctamente.'}
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
            form = forms.ValidateWorkshop.from_json(post_data, skip_unknown_keys=True)
            if not form.validate():
                response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
            else:
                Workshop.db = get_db()
                if Workshop.workshop_exists_not_self(post_data):
                    response_object = {'status': 'warning', 'message': 'El taller ya existe.'}
                else:
                    Workshop.update(post_data)
                    response_object = {'status': 'success', 'message': 'Actualizaste el taller correctamente.'}
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
            form = forms.ValidateWorkshopId.from_json(post_data, skip_unknown_keys=False)
            if not form.validate():
                response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
            else:
                Workshop.db = get_db()
                Workshop.delete(post_data['workshop_id'])
                response_object = {'status': 'success', 'message': 'Eliminaste el taller correctamente.'}
                return jsonify(response_object)

#---------------------------------------------------#
#   Información para asignar talleres a ciclos
#---------------------------------------------------#
def getFormData():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'administrativo_new')):
        abort(401)
    else:
        Cycle.db = get_db()
        Workshop.db = get_db()
        response_json = {
            'cycles': Cycle.all(),
            'workshops': Workshop.all(),
            }
        return response_json

#---------------------------------------------------#
#   Elimina un ciclo lectivo
#---------------------------------------------------#
def assign():
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
            form = forms.ValidateCycleWorkshop.from_json(post_data, skip_unknown_keys=True)
            if not form.validate():
                response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
            else:
                CycleWorkshop.db = get_db()
                if CycleWorkshop.cycle_workshop_exists(post_data):
                    response_object = {'status': 'warning', 'message': 'El taller ya se encuentra asignado al ciclo lectivo.'}
                else:
                    newone = CycleWorkshop.create(post_data)
                    response_object = {
                        'status': 'success',
                        'message': 'Asignaste el taller al ciclo lectivo correctamente.',
                        'new_cylce_workshop': newone
                        }
                return jsonify(response_object)


#---------------------------------------------------#
#   Elimina un ciclo lectivo
#---------------------------------------------------#
def unassign():
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
            form = forms.ValidateCycleWorkshopId.from_json(post_data, skip_unknown_keys=True)
            if not form.validate():
                response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
            else:
                CycleWorkshop.db = get_db()
                CycleWorkshop.delete(post_data['cycle_workshop_id'])
                response_object = {'status': 'success', 'message': 'Desasignaste el taller correctamente.'}
                return jsonify(response_object)
