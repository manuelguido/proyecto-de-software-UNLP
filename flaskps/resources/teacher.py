from flask import redirect, render_template, request, url_for, abort, session, flash, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.teacher import Teacher
from flaskps.models.neighborhood import Neighborhood
from flaskps.models.level import Level
from flaskps.models.gender import Gender
from flaskps.models.school import School
from flaskps.models.document_type import DocumentType
from flaskps.models.location import Location
from flaskps.helpers import auth
from flaskps.resources import forms

from flaskps.helpers import auth
from flaskps.resources import forms

def all():
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'docente_index')):
        abort(401)
    else:
        Teacher.db = get_db()
        return jsonify(Teacher.all_reduced())

def get(id_data):
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'estudiante_show')):
        abort(401)
    else:
        Teacher.db = get_db()
        return jsonify(Teacher.get(id_data))


def create():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        #Chequea permiso
        User.db = get_db()
        if (not User.has_permission(session['id'],'estudiante_new')):
            abort(401)
        else:
            # if forms.ValidateStudent(request.form).validate():
            post_data = request.get_json()
            Teacher.db = get_db()
            Teacher.create(post_data)
            response_object = {'status': 'success', 'message': 'Se agregó el nuevo docente'}
            # else:
            #     response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos'}
            return jsonify(response_object)

def update():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        #Chequea permiso
        User.db = get_db()
        if (not User.has_permission(session['id'],'docente_update')):
            abort(401)
        else:
            post_data = request.get_json()
            # if forms.ValidateStudent(request.form).validate():
            Teacher.db = get_db()
            Teacher.update(post_data)
            response_object = {'status': 'success', 'message': 'Se actualizó el docente'}
            # else:
            #     response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos'}
            return jsonify(response_object)

def delete():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.has_permission(session['id'],'docente_destroy')):
        Teacher.db = get_db()
        Teacher.delete(request.get_json()['teacher_id'])
        response_object = {'status': 'success', 'message': 'Se eliminó el docente'}
        return jsonify(response_object)
    else:
        abort(401)

def getFormData():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'docente_new')):
        abort(401)
    else:
        Gender.db = get_db()
        DocumentType.db = get_db()
        Location.db = get_db()
        response_json = {
            'genders': Gender.all(),
            'document_types': DocumentType.all(),
            'locations': Location.all(),
            }
        return response_json

# def deleteDocenteTaller():
#     #Auth check
#     auth.authenticated_or_401()

#     #Chequea permiso
#     User.db = get_db()
#     if (User.tiene_permiso(session['id'],'administrativo_destroy')):
#         if request.method == "POST" and forms.ValidateDocenteTallerDelete(request.form).validate():
#             Teacher.db = get_db()
#             Teacher.deleteDocenteTaller(request.form)
#             flash("Se desasigno el docente del taller correctamente" ,'success')
#         else:
#             flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
#         return redirect(url_for('panel_docentes_taller'))
#     else:
#         abort(401)

# def storeDocenteTaller():
#     #Auth check
#     auth.authenticated_or_401()

#     #Chequea permiso
#     User.db = get_db()
#     if (User.tiene_permiso(session['id'],'administrativo_new')):
#         if request.method == "POST" and forms.ValidateDocenteTaller(request.form).validate():
#             Teacher.db = get_db()
#             if Teacher.tallerNoTieneDocente(request.form):
#                 Teacher.storeDocenteTaller(request.form)
#                 flash("Se agrego el taller al ciclo lectivo correctamente" ,'success')
#             else:
#                 flash("El docente ya esta asignado al taller para el ciclo lectivo seleccionado", 'error')
#         else:
#             flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
#         return redirect(url_for('panel_docentes_taller'))
#     else:
#         abort(401)
