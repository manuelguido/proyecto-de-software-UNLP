from flask import redirect, render_template, request, url_for, abort, session, flash, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.student import Student
from flaskps.models.responsable import Responsable
from flaskps.models.neighborhood import Neighborhood
from flaskps.models.level import Level
from flaskps.models.gender import Gender
from flaskps.models.school import School
from flaskps.models.document_type import DocumentType
from flaskps.models.location import Location
from flaskps.models.responsable_type import ResponsableType
from flaskps.models.responsable import Responsable

from flaskps.helpers import auth
from flaskps.resources import forms

def all():
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (User.has_permission(session['id'],'estudiante_index')):
        Student.db = get_db()
        return jsonify(Student.all_reduced())
    else:
        abort(401)

def get(id_data):
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (User.has_permission(session['id'],'estudiante_show')):
        Student.db = get_db()
        return jsonify(Student.get(id_data))
    else:
        abort(401)

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
            Responsable.db = get_db()
            responsable_id = Responsable.create(post_data)
            Student.db = get_db()
            Student.create(post_data, responsable_id)
            response_object = {'status': 'success', 'message': 'Se agregó el nuevo estudiante'}
            # else:
            #     response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos'}
            return jsonify(response_object)

def update():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        #Chequea permiso
        User.db = get_db()
        if (not User.has_permission(session['id'],'estudiante_update')):
            abort(401)
        else:
            post_data = request.get_json()
            # if forms.ValidateStudent(request.form).validate():
            Student.db = get_db()
            Student.update(post_data)
            response_object = {'status': 'success', 'message': 'Se actualizó el estudiante'}
            # else:
            #     response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos'}
            return jsonify(response_object)

def delete():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.has_permission(session['id'],'estudiante_destroy')):
        Student.db = get_db()
        Student.delete(request.get_json()['student_id'])
        response_object = {'status': 'success', 'message': 'Se eliminó el estudiante'}
        return jsonify(response_object)
    else:
        abort(401)

def getFormData():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'estudiante_new')):
        abort(401)
    else:
        Neighborhood.db = get_db()
        Level.db = get_db()
        Gender.db = get_db()
        School.db = get_db()
        DocumentType.db = get_db()
        Location.db = get_db()
        ResponsableType.db = get_db()
        response_json = {
            'neighborhoods': Neighborhood.all(),
            'levels': Level.all(),
            'genders': Gender.all(),
            'schools': School.all(),
            'document_types': DocumentType.all(),
            'locations': Location.all(),
            'responsable_types': ResponsableType.all(),
            }
        return response_json

# def deleteEstudianteDocente():
#     #Auth check
#     auth.authenticated_or_401()

#     #Chequea permiso
#     User.db = get_db()
#     if (User.tiene_permiso(session['id'],'administrativo_destroy')):
#         if request.method == "POST" and forms.ValidateEstudianteDocenteTallerDelete(request.form).validate():
#             Student.db = get_db()
#             Student.deleteEstudianteTaller(request.form)
#             flash("Se desasigno el estudiante del taller correctamente" ,'success')
#         else:
#             flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
#         return redirect(url_for('panel_estudiantes_docentes'))
#     else:
#         abort(401)

# def storeEstudianteDocente():
#     #Auth check
#     auth.authenticated_or_401()

#     #Chequea permiso
#     User.db = get_db()
#     if (User.tiene_permiso(session['id'],'administrativo_new')):
#         if request.method == "POST" and forms.ValidateEstudianteDocenteTaller(request.form).validate():
#             Student.db = get_db()
#             if Student.estudianteNoEnTaller(request.form):
#                 Student.storeEstudianteTaller(request.form)
#                 flash("Se asigno el estudiante al taller correctamente" ,'success')
#             else:
#                 flash("El estudiante ya esta asignado al taller", 'error')
#         else:
#             flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
#         return redirect(url_for('panel_estudiantes_docentes'))
#     else:
#         abort(401)
