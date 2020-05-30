from flask import redirect, render_template, request, url_for, abort, session, flash, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.student import Student
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
        return jsonify({})

def get(id_data):
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (User.has_permission(session['id'],'estudiante_show')):
        Student.db = get_db()
        return jsonify(Student.get(id_data))
    else:
        return jsonify({})

def store():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        #Chequea permiso
        User.db = get_db()
        if (User.has_permission(session['id'],'estudiante_new')):
            if forms.ValidateStudent(request.form).validate():
                Student.db = get_db()
                Student.store(request.form)
                response_object = {'status': 'success', 'message': 'Se agregó el nuevo estudiante'}
            else:
                response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos'}
        else:
            abort(401)
        return jsonify(response_object)

def delete(id_data):
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.has_permission(session['id'],'estudiante_destroy')):
        Student.db = get_db()
        Student.delete(id_data)
        response_object = {'status': 'success', 'message': 'Se eliminó el estudiante'}
        return jsonify(response_object)
    else:
        abort(401)

def update():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        #Chequea permiso
        User.db = get_db()
        if (User.has_permission(session['id'],'estudiante_update')):
            if forms.ValidateStudent(request.form).validate():
                Student.db = get_db()
                Student.update(request.form)
                response_object = {'status': 'success', 'message': 'Se actualizó el estudiante'}
            else:
                response_object = {'status': 'warning', 'message': 'Verifica los campos obligatorios y no ingreses valores no permitidos'}
            return jsonify(response_object)
        else:
            abort(401)

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
