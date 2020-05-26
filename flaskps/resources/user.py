from flask import redirect, render_template, request, url_for, session, abort, flash, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.helpers import auth
from flaskps.resources import forms

#Retorna todos los usuarios
def all():
    #Auth check
    auth.authenticated_or_401()
    #Retorno de data
    User.db = get_db()
    return jsonify(User.all())

#Retorna el usuario by id
def get(id_data):
    #Auth check
    auth.authenticated_or_401()
    #Retorno de data
    User.db = get_db()
    return jsonify(User.get(id_data))

#Retorna el perfil del usuario loggeado
def profile():
    #Auth check
    auth.authenticated_or_401()
    #Retorno de data
    user_object = {'name': session['name'], 'lastname': session['lastname']}
    return jsonify(user_object)

#Retorna las rutas del usuario loggeado
def routes():
    #Auth check
    auth.authenticated_or_401()
    #Listado de rutas
    user_routes = []
    #Cargado de información
    User.db = get_db()
    nucleos = {'name': 'Núcleos', 'url': '/dashboard/cores', 'icon': 'fas fa-map-marked-alt'}
    user_routes.append(nucleos)

    if (User.has_permission(session['id'],'estudiante_index')):
        new = {'name': 'Estudiantes', 'url': '/dashboard/students', 'icon': 'fas fa-user-graduate'}
        user_routes.append(new)

    if (User.has_permission(session['id'],'docente_index')):
        new = {'name': 'Docentes', 'url': '/dashboard/teachers', 'icon': 'fas fa-user-friends'}
        user_routes.append(new)
    
    if (User.has_permission(session['id'],'instrumento_index')):
        new = {'name': 'Instrumentos', 'url': '/dashboard/instruments', 'icon': 'fas fa-guitar'}
        user_routes.append(new)
    
    if (User.has_permission(session['id'],'usuario_index')):
        new = {'name': 'Usuarios', 'url': '/dashboard/users', 'icon': 'fas fa-user'}
        user_routes.append(new)
    
    if (User.has_permission(session['id'],'administrativo_index')):
        new = {'name': 'Administrativo', 'url': '/dashboard/admin', 'icon': 'fas fa-cog'}
        user_routes.append(new)
    #Returning data
    return jsonify(user_routes)

#Actualiza el estado (active/inactive) del usuario
def update_user_status():
    #Auth check
    auth.authenticated_or_401()
    User.db = get_db()
    #Chequea permiso
    if (User.has_permission(session['id'],'usuario_update')):
        #Valida campos
        if request.method == "POST" and (request.form['active'] == '0' or request.form['active'] == '1'):
            User.update_user_status(request.form)
            flash("Estado cambiado correctamente" ,'success')
        else:
            flash('No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_usuarios'))
    else:
        abort(401)

#Actualiza la información de un usuario
def update():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.has_permission(session['id'],'usuario_update')):
        if request.method == "POST" and forms.ValidateUserWithOutPassword(request.form).validate():
            #verifica los roles enviados
            if (request.form.get("rol1") == None) and (request.form.get("rol2") == None) and (request.form.get("rol3") == None):
                flash('Debes elegir al menos un rol de usuario', 'error')
            #Chequea la existencia del usuario
            elif User.find_by_username_not_self(request.form['username'],request.form.get("id_data")):
                flash("Ya existe un usuario con ese nombre de usuario" ,'error')
            elif User.find_by_email_not_self(request.form['email'],request.form.get("id_data")):
                flash("Ya existe un usuario con ese email" ,'error')
            else:
                User.update(request.form)
                if request.form.get("rol1") != None:
                    if not User.tiene_rol(request.form['id_data'], 'administrador'):
                        a = '1'
                        User.set_role(request.form.get("id_data"), a)
                else:
                    a = '1'
                    if User.tiene_rol(request.form['id_data'], 'administrador'):
                        User.unset_role(request.form.get("id_data"), a)
                if request.form.get("rol2") != None:
                    if not User.tiene_rol(request.form['id_data'], 'docente'):
                        User.set_role(request.form.get("id_data"), 2)
                else:
                    if User.tiene_rol(request.form['id_data'], 'docente'):
                        User.unset_role(request.form.get("id_data"), 2)
                if request.form.get("rol3") != None:
                    if not User.tiene_rol(request.form['id_data'], 'preceptor'):
                        User.set_role(request.form.get("id_data"), 3)
                else:
                    if User.tiene_rol(request.form['id_data'], 'preceptor'):
                        User.unset_role(request.form.get("id_data"), 3)
                flash("Usuario modificado correctamente" ,'success')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for("get_update_user", id_data=request.form.get("id_data")))
    else:
        abort(401)

#Almacena un usuario
def store():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.has_permission(session['id'],'usuario_new')):
        if request.method == "POST" and forms.ValidateUser(request.form).validate():
            if (request.form['password'] != request.form['password_repeat']):
                flash('Las contraseñas no coinciden', 'error')
            #verifica los roles enviados
            elif (request.form.get("rol1") == None) and (request.form.get("rol2") == None) and (request.form.get("rol3") == None):
                flash('Debes elegir al menos un rol de usuario', 'error')
            #Chequea la existencia del usuario
            elif User.find_by_username(request.form['username']):
                flash("Ya existe un usuario con ese nombre de usuario" ,'error')
            elif User.find_by_email(request.form['email']):
                flash("Ya existe un usuario con ese email" ,'error')
            else:
                User.create(request.form)
                user = User.find_by_email_and_pass(request.form['email'], request.form['password'])
                if request.form.get("rol1") != None:
                    User.set_role(user['id'], 1)
                if request.form.get("rol2") != None:
                    User.set_role(user['id'], 2)
                if request.form.get("rol3") != None:
                    User.set_role(user['id'], 3)
                flash("Usuario agregado correctamente" ,'success')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_usuarios'))
    else:
        abort(401)

def delete(id_data):
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (User.has_permission(session['id'],'usuario_destroy')):
        User.delete_roles(id_data)
        User.delete(id_data)
        flash("Se eliminó el usuario correctamente" ,'success')
        return redirect(url_for('panel_usuarios'))
    else:
        abort(401)
