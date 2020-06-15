from flask import redirect, render_template, request, url_for, abort, session, flash, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.student import Student
from flaskps.models.assistance import Assistance
from flaskps.models.lesson import Lesson
from flaskps.helpers.auth import authenticated
from flaskps.helpers import auth
from flaskps.resources import forms

#Forms & validation
from wtforms import Form
import wtforms_json
wtforms_json.init()

#---------------------------------------------------#
#   Retorna todos las asistencias de una clase
#---------------------------------------------------#
def get_assistances(lesson_id):
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'administrativo_index')):
        abort(401)
    else:
        Assistance.db = get_db()
        return jsonify(Assistance.all(lesson_id))

#---------------------------------------------------#
#   Crea una asistencia
#---------------------------------------------------#
def add():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        #Chequea permiso
        User.db = get_db()
        if (not User.has_permission(session['id'],'asistencia_new')):
            abort(401)
        else:
            post_data = request.get_json()
            #Form validation
            form = forms.ValidateAssistance.from_json(post_data, skip_unknown_keys=True)
            if (not form.validate()): # or (Assistance.wrong_student(post_data)):
                response_object = {'status': 'error', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
            else:
                Assistance.db = get_db()
                Assistance.add(post_data)
                response_object = {'status': 'success', 'message': 'Asistencia guardada.'}
            return jsonify(response_object)

#---------------------------------------------------#
#   Crea una asistencia
#---------------------------------------------------#
# def update_assistance():
#     #Auth check
#     auth.authenticated_or_401()

#     if request.method == "POST":
#         #Chequea permiso
#         User.db = get_db()
#         if (not User.has_permission(session['id'],'asistencia_new')):
#             abort(401)
#         else:
#             post_data = request.get_json()
#             #Form validation
#             form = forms.ValidateLessonStudent.from_json(post_data, skip_unknown_keys=False)
#             if not form.validate():
#                 response_object = {'status': 'error', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
#             else:
#                 Assistance.db = get_db()
#                 if Assistance.has_student(post_data):
#                     response_object = {'status': 'warning', 'message': 'El estudiante ya está asignado en la clase.'}
#                 else:
#                     Assistance.add_student(post_data)
#                     response_object = {
#                         'status': 'success',
#                         'message': 'Asignaste el estudiante correctamente.'
#                         }
#             return jsonify(response_object)

#---------------------------------------------------#
#   Elimina una asistencia
#---------------------------------------------------#
def remove():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        #Chequea permiso
        User.db = get_db()
        if (not User.has_permission(session['id'],'asistencia_destroy')):
            abort(401)
        else:
            post_data = request.get_json()
            #Form validation
            form = forms.ValidateLessonStudent.from_json(post_data, skip_unknown_keys=False)
            if not form.validate():
                response_object = {'status': 'error', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos.'}
            else:
                Lesson.db = get_db()
                Lesson.remove_student(post_data)
                response_object = {'status': 'success', 'message': 'Desasignaste el estudiante correctamente.'}
                return jsonify(response_object)

#---------------------------------------------------#
#   Información para los formularios
#---------------------------------------------------#
def getFormData(lesson_id):
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'administrativo_new')):
        abort(401)
    else:
        Lesson.db = get_db()
        response_json = {
            'students': Lesson.students(lesson_id)
            }
        return response_json

#---------------------------------------------------#
#   Retorna los estudiantes para una asistencia
#---------------------------------------------------#
def students_for_assistance():
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'asistencia_new')):
        abort(401)
    else:
        post_data = request.get_json()
        Lesson.db = get_db()
        return jsonify(Lesson.students_for_assistance(post_data))
