from flask import redirect, render_template, request, url_for, abort, session, flash, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.lesson import Lesson
from flaskps.models.cycle_workshop import CycleWorkshop
from flaskps.models.workshop_type import WorkshopType
from flaskps.models.level import Level
from flaskps.helpers import auth
from flaskps.resources import forms

#---------------------------------------------------#
#   Retorna todos las clases
#---------------------------------------------------#
def all():
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'administrativo_index')):
        abort(401)
    else:
        Lesson.db = get_db()
        return jsonify(Lesson.all())

#---------------------------------------------------#
#   Retorna al clase por su id
#---------------------------------------------------#
def get(lesson_id):
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'administrativo_show')):
        abort(401)
    else:
        Lesson.db = get_db()
        return jsonify(Lesson.get(lesson_id))

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
            post_data = request.form
            #Form validation
            form = forms.ValidateLesson(post_data, skip_unknown_keys=True)
            if not form.validate():
                response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
            else:
                Lesson.db = get_db()
                if Lesson.lesson_exists(post_data):
                    response_object = {'status': 'warning', 'message': 'La clase ya existe.'}
                else:
                    Lesson.create(post_data)
                    response_object = {'status': 'success', 'message': 'Creaste la clase correctamente.'}
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
            post_data = request.form
            #Form validation
            form = forms.ValidateLesson(post_data, skip_unknown_keys=True)
            if not form.validate():
                response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
            else:
                Lesson.db = get_db()
                if Lesson.lesson_exists_not_self(post_data):
                    response_object = {'status': 'warning', 'message': 'La clase ya existe.'}
                else:
                    Lesson.update(post_data)
                    response_object = {'status': 'success', 'message': 'Actualizaste la clase correctamente.'}
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
            post_data = request.form
            #Form validation
            form = forms.ValidateCycleId(post_data, skip_unknown_keys=True)
            if not form.validate():
                response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
            else:
                Lesson.db = get_db()
                Lesson.delete(post_data['lesson_id'])
                response_object = {'status': 'success', 'message': 'Eliminaste la clase correctamente.'}
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
        CycleWorkshop.db = get_db()
        WorkshopType.db = get_db()
        Level.db = get_db()
        response_json = {
            'cycle_workshops': CycleWorkshop.all(),
            'workshop_types': WorkshopType.all(),
            'levels': Level.all()
            }
        return response_json
