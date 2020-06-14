from flask import redirect, render_template, request, url_for, abort, session, flash, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.lesson import Lesson
from flaskps.models.schedule import Schedule
from flaskps.models.core import Core
from flaskps.models.day import Day

from flaskps.models.cycle_workshop import CycleWorkshop
from flaskps.models.workshop_type import WorkshopType
from flaskps.models.level import Level
from flaskps.helpers import auth
from flaskps.resources import forms

#Forms & validation
from wtforms import Form
import wtforms_json
wtforms_json.init()

#---------------------------------------------------#
#   Retorna todos las clases
#---------------------------------------------------#
def get_schedules(lesson_id):
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'horario_index')):
        abort(401)
    else:
        Schedule.db = get_db()
        return jsonify(Schedule.all(lesson_id))

#---------------------------------------------------#
#   Retorna al clase por su id
#---------------------------------------------------#
def get(lesson_id):
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'horario_show')):
        abort(401)
    else:
        Lesson.db = get_db()
        return jsonify(Lesson.get(lesson_id))

#---------------------------------------------------#
#   Crea un horario
#---------------------------------------------------#
def add():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        #Chequea permiso
        User.db = get_db()
        if (not User.has_permission(session['id'],'horario_new')):
            abort(401)
        else:
            post_data = request.get_json()
            #Form validation
            form = forms.ValidateSchedule.from_json(post_data, skip_unknown_keys=True)
            if not form.validate():
                response_object = {'status': 'error', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
            else:
                Schedule.db = get_db()
                if Schedule.schedule_exists(post_data):
                    response_object = {'status': 'warning', 'message': 'La clase ya tiene ese horario.'}
                else:
                    newschedule = Schedule.add(post_data)
                    response_object = {'status': 'success', 'message': 'Agregaste el horario correctamente.'}
                    response_object = {
                        'status': 'success',
                        'message': 'Agregaste el horario correctamente.',
                        'new_schedule': newschedule
                        }
            return jsonify(response_object)

#---------------------------------------------------#
#   Elimina un horario
#---------------------------------------------------#
def remove():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        #Chequea permiso
        User.db = get_db()
        if (not User.has_permission(session['id'],'horario_destroy')):
            abort(401)
        else:
            post_data = request.get_json()
            #Form validation
            form = forms.ValidateScheduleId.from_json(post_data, skip_unknown_keys=True)
            if not form.validate():
                response_object = {'status': 'error', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
            else:
                Schedule.db = get_db()
                Schedule.remove(post_data['schedule_id'])
                response_object = {'status': 'success', 'message': 'Eliminaste el horario correctamente.'}
                return jsonify(response_object)

#---------------------------------------------------#
#   Información para los formularios
#---------------------------------------------------#
def getFormData():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'horario_new')):
        abort(401)
    else:
        Core.db = get_db()
        Day.db = get_db()
        response_json = {
            'cores': Core.all(),
            'days': Day.all()
            }
        return response_json
