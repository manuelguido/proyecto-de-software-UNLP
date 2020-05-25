from flask import redirect, render_template, request, url_for, session, abort, flash, jsonify
from flaskps.db import get_db
from flaskps.models.usuario import Usuario
from flaskps.helpers.auth import authenticated
from flaskps.resources import forms

def update_user_status():
    if not authenticated(session):
        abort(401)
    
    #Chequea permiso
    Usuario.db = get_db()
    if (Usuario.tiene_permiso(session['id'],'usuario_update')):
        if request.method == "POST" and (request.form['activo'] == '0' or request.form['activo'] == '1'):
            Usuario.update_user_status(request.form)
            flash("Estado cambiado correctamente" ,'success')
        else:
            flash('No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_usuarios'))
    else:
        abort(401)

def update():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    Usuario.db = get_db()
    if (Usuario.tiene_permiso(session['id'],'usuario_update')):
        if request.method == "POST" and forms.ValidateUserWithOutPassword(request.form).validate():
            #verifica los roles enviados
            if (request.form.get("rol1") == None) and (request.form.get("rol2") == None) and (request.form.get("rol3") == None):
                flash('Debes elegir al menos un rol de usuario', 'error')
            #Chequea la existencia del usuario
            elif Usuario.find_by_username_not_self(request.form['username'],request.form.get("id_data")):
                flash("Ya existe un usuario con ese nombre de usuario" ,'error')
            elif Usuario.find_by_email_not_self(request.form['email'],request.form.get("id_data")):
                flash("Ya existe un usuario con ese email" ,'error')
            else:
                Usuario.update(request.form)
                if request.form.get("rol1") != None:
                    if not Usuario.tiene_rol(request.form['id_data'], 'administrador'):
                        a = '1'
                        Usuario.set_role(request.form.get("id_data"), a)
                else:
                    a = '1'
                    if Usuario.tiene_rol(request.form['id_data'], 'administrador'):
                        Usuario.unset_role(request.form.get("id_data"), a)
                if request.form.get("rol2") != None:
                    if not Usuario.tiene_rol(request.form['id_data'], 'docente'):
                        Usuario.set_role(request.form.get("id_data"), 2)
                else:
                    if Usuario.tiene_rol(request.form['id_data'], 'docente'):
                        Usuario.unset_role(request.form.get("id_data"), 2)
                if request.form.get("rol3") != None:
                    if not Usuario.tiene_rol(request.form['id_data'], 'preceptor'):
                        Usuario.set_role(request.form.get("id_data"), 3)
                else:
                    if Usuario.tiene_rol(request.form['id_data'], 'preceptor'):
                        Usuario.unset_role(request.form.get("id_data"), 3)
                flash("Usuario modificado correctamente" ,'success')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for("get_update_user", id_data=request.form.get("id_data")))
    else:
        abort(401)

def store():
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    Usuario.db = get_db()
    if (Usuario.tiene_permiso(session['id'],'usuario_new')):
        if request.method == "POST" and forms.ValidateUser(request.form).validate():
            if (request.form['password'] != request.form['password_repeat']):
                flash('Las contraseñas no coinciden', 'error')
            #verifica los roles enviados
            elif (request.form.get("rol1") == None) and (request.form.get("rol2") == None) and (request.form.get("rol3") == None):
                flash('Debes elegir al menos un rol de usuario', 'error')
            #Chequea la existencia del usuario
            elif Usuario.find_by_username(request.form['username']):
                flash("Ya existe un usuario con ese nombre de usuario" ,'error')
            elif Usuario.find_by_email(request.form['email']):
                flash("Ya existe un usuario con ese email" ,'error')
            else:
                Usuario.create(request.form)
                user = Usuario.find_by_email_and_pass(request.form['email'], request.form['password'])
                if request.form.get("rol1") != None:
                    Usuario.set_role(user['id'], 1)
                if request.form.get("rol2") != None:
                    Usuario.set_role(user['id'], 2)
                if request.form.get("rol3") != None:
                    Usuario.set_role(user['id'], 3)
                flash("Usuario agregado correctamente" ,'success')
        else:
            flash('Verifica los campos obligatorios. No ingreses valores no permitidos', 'error')
        return redirect(url_for('panel_usuarios'))
    else:
        abort(401)

def delete(id_data):
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    Usuario.db = get_db()
    if (Usuario.tiene_permiso(session['id'],'usuario_destroy')):
        Usuario.delete_roles(id_data)
        Usuario.delete(id_data)
        flash("Se eliminó el usuario correctamente" ,'success')
        return redirect(url_for('panel_usuarios'))
    else:
        abort(401)

def get_rutas():
    if not authenticated(session):
        abort(401)
    my_objects = [] #Listado de rutas
    nucleos = {'name': 'Núcleos', 'url': '/dashboard/nucleos', 'icon': 'fas fa-map-marked-alt'}
    my_objects.append(nucleos)
    #User
    Usuario.db = get_db()
    
    if (Usuario.tiene_permiso(session['id'],'estudiante_index')):
        new = {'name': 'Estudiantes', 'url': '/dashboard/estudiantes', 'icon': 'fas fa-user-graduate'}
        my_objects.append(new)
    
    if (Usuario.tiene_permiso(session['id'],'docente_index')):
        new = {'name': 'Docentes', 'url': '/dashboard/docentes', 'icon': 'fas fa-user-friends'}
        my_objects.append(new)
    
    if (Usuario.tiene_permiso(session['id'],'instrumento_index')):
        new = {'name': 'Instrumentos', 'url': '/dashboard/instrumentos', 'icon': 'fas fa-guitar'}
        my_objects.append(new)
    
    if (Usuario.tiene_permiso(session['id'],'usuario_index')):
        new = {'name': 'Usuarios', 'url': '/dashboard/usuarios', 'icon': 'fas fa-user'}
        my_objects.append(new)
    
    if (Usuario.tiene_permiso(session['id'],'administrativo_index')):
        new = {'name': 'Administrativo', 'url': '/dashboard/administrativo', 'icon': 'fas fa-cog'}
        my_objects.append(new)
    #Returning data
    return jsonify(my_objects)

def get_perfil():
    if not authenticated(session):
        abort(401)
    user_object = {'name': session['nombre'], 'lastname': session['apellido']}
    return jsonify(user_object)

def get_all():
    if not authenticated(session):
        abort(401)
    Usuario.db = get_db()
    return jsonify(Usuario.all())

def get_usuario(id_data):
    if not authenticated(session):
        abort(401)
    Usuario.db = get_db()
    return jsonify(Usuario.get_usuario(id_data))
