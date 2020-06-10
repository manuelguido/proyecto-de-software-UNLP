from flask import redirect, render_template, request, url_for, session, abort, flash, jsonify
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.role import Role
from flaskps.helpers import auth
from flaskps.resources import forms

#Forms & validation
from wtforms import Form
import wtforms_json
wtforms_json.init()

#---------------------------------------------------#
#   Retorna todos los usuarios
#---------------------------------------------------#
def all():
    #Auth check
    auth.authenticated_or_401()
    
    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'usuario_index')):
        abort(401)
    else:
        User.db = get_db()
        return jsonify(User.all())

#---------------------------------------------------#
#   Retorna el usuario por su id
#---------------------------------------------------#
def get(id_data):
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'usuario_show')):
        abort(401)
    else:
        #Retorno de data
        User.db = get_db()
        user = User.get(id_data)
        roles = user_roles(user['user_id'])

        return_user = {
            'active': user['active'],
            'email': user['email'],
            'google_user': user['google_user'],
            'lastname': user['lastname'],
            'name': user['name'],
            'user_id': user['user_id'],
            'username':	user['username'],
            'is_admin': roles['is_admin'],
            'is_teacher': roles['is_teacher'],
            'is_preceptor': roles['is_preceptor']
        }
        return jsonify(return_user)

#---------------------------------------------------#
#   Crea un usuario
#---------------------------------------------------#
def create():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        User.db = get_db()
        if (not User.has_permission(session['id'],'usuario_new')):
            abort(401)
        else:
            post_data = request.get_json() #Obtención de información
            errors = [] #Errores

            #Chequeo username
            if User.find_by_username(post_data['username']):                
                errors.append({'name': 'username', 'message': 'El nombre de usuario ingresado ya existe'})
            #Chequeo email
            if User.find_by_email(post_data['email']):
                errors.append({'name': 'email', 'message': 'El email ingresado ya existe'})
            #Chequeo passwords
            if (post_data['password'] != post_data['password_confirm']):
                errors.append({'name': 'password', 'message': 'Las contraseñas ingresadas no coinciden'})

            form = forms.ValidateUser.from_json(post_data, skip_unknown_keys=True)
            if (form.validate() and len(errors) == 0):
                User.create(post_data)
                new_user = User.find_by_email(post_data['email'])
                update_roles(new_user['user_id'], post_data)
                response_object = {'status': 'success', 'message': 'Se agregó el nuevo usuario'}
            else:
                if (not form.validate()):
                    err = {'name': 'fields', 'message': 'Verifica los campos obligatorios y no ingreses nombres no permitidos.'}
                    errors.append(err)
                response_object = errors
            return jsonify(response_object)

#---------------------------------------------------#
#   Actualiza la información del usuario
#---------------------------------------------------#
def update():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        User.db = get_db()
        if (User.has_permission(session['id'],'usuario_update')):
            abort(401)
        else:
            post_data = request.get_json() #Obtención de información
            errors = [] #Errores

            #Chequeo username
            if User.find_by_username_not_self(post_data):                
                errors.append({'name': 'username', 'message': 'El nombre de usuario ingresado ya existe'})
            #Chequeo email
            if User.find_by_email_not_self(post_data):
                errors.append({'name': 'email', 'message': 'El email ingresado ya existe'})

            form = forms.ValidateUserWithOutPassword.from_json(post_data, skip_unknown_keys=True)
            if (form.validate() and len(errors) == 0):
                User.update(post_data)
                new_user = User.find_by_email(post_data['email'])
                update_roles(new_user['user_id'], post_data)
                response_object = {'status': 'success', 'message': 'Se actualizó el nuevo usuario'}
            else:
                if (not form.validate()):
                    err = {'name': 'fields', 'message': 'Verifica los campos obligatorios y no ingreses nombres no permitidos.'}
                    errors.append(err)
                response_object = errors
            return jsonify(response_object)

#---------------------------------------------------#
#   Elimina un usuario
#---------------------------------------------------#
def delete():
    #Auth check
    auth.authenticated_or_401()

    #Chequea permiso
    User.db = get_db()
    if (not User.has_permission(session['id'],'usuario_destroy')):
        abort(401)
    else:
        user_id = int(request.get_json()['user_id'])
        if (int(session['id']) == user_id):
            response_object = {'status': 'warning', 'message': 'No te puedes eliminar a ti mismo'}
        else:
            User.delete(user_id)
            User.remove_roles(user_id)
            response_object = {'status': 'success', 'message': 'Se eliminó el usuario'}
        return jsonify(response_object)

#---------------------------------------------------#
#   Actualiza/Crea los roles del usuario
#---------------------------------------------------#
def update_roles(user_id, post_data):
    admin_id = 1 #Role.get_id_by_name('Administrador')
    teacher_id = 2 #Role.get_id_by_name('Docente')
    preceptor_id = 3 #Role.get_id_by_name('Preceptor')

    if (post_data['is_admin']):
        User.add_role(user_id, admin_id)
    else:
        User.remove_role(user_id, admin_id)

    if (post_data['is_teacher']):
        User.add_role(user_id, teacher_id)
    else:
        User.remove_role(user_id, teacher_id)

    if (post_data['is_preceptor']):
        User.add_role(user_id, preceptor_id)
    else:
        User.remove_role(user_id, preceptor_id)

    return True

#---------------------------------------------------#
#   Actualiza el estado (active/inactive) del usuario
#---------------------------------------------------#
def update_user_status():
    #Auth check
    auth.authenticated_or_401()

    if request.method == "POST":
        User.db = get_db()        
        #Chequea permiso
        if (User.has_permission(session['id'],'usuario_update')):
            #Valida campos
            if (request.form['active'] == '0' or request.form['active'] == '1'):
                User.update_user_status(request.form)
                return {'status': 'success', 'message': 'Se actualizó el estado del usuario'}
        else:
            abort(401)

#---------------------------------------------------#
#   Retorna el perfil del usuario loggeado
#---------------------------------------------------#
def profile():
    #Auth check
    auth.authenticated_or_401()
    #Retorno de data
    user_object = {'name': session['name'], 'lastname': session['lastname']}
    return jsonify(user_object)

#---------------------------------------------------#
#   Retorna verdadero si el usuario tiene al menos un rol
#---------------------------------------------------#
def has_role():
    #Auth check
    auth.authenticated_or_401()
    #User routes
    User.db = get_db()
    roles_object = {'status': True}
    if not User.has_roles(session['id']):
        roles_object = {'status': False}
    return jsonify(roles_object)

#---------------------------------------------------#
#   Retorna las rutas del usuario loggeado
#---------------------------------------------------#
def routes():
    def get_routes():
        user_routes = []
        #Cargado de información
        nucleos = {'name': 'Núcleos', 'url': '/cores', 'icon': 'fas fa-map-marker-alt'}
        user_routes.append(nucleos)

        if (User.has_permission(session['id'],'estudiante_index')):
            new = {'name': 'Estudiantes', 'url': '/students', 'icon': 'fas fa-user-graduate'}
            user_routes.append(new)

        if (User.has_permission(session['id'],'docente_index')):
            new = {'name': 'Docentes', 'url': '/teachers', 'icon': 'fas fa-user'}
            user_routes.append(new)

        if (User.has_permission(session['id'],'instrumento_index')):
            new = {'name': 'Instrumentos', 'url': '/instruments', 'icon': 'fas fa-guitar'}
            user_routes.append(new)

        if (User.has_permission(session['id'],'administrativo_index')):
            new = {'name': 'Ciclos lectivos', 'url': '/cycles', 'icon': 'far fa-calendar-alt'}
            user_routes.append(new)
            new = {'name': 'Talleres', 'url': '/workshops', 'icon': 'fas fa-school'}
            user_routes.append(new)
            new = {'name': 'Clases', 'url': '/lessons', 'icon': 'fas fa-chalkboard-teacher'}
            user_routes.append(new)

        if (User.has_permission(session['id'],'usuario_index')):
            new = {'name': 'Usuarios', 'url': '/users', 'icon': 'fas fa-user-friends'}
            user_routes.append(new)

        if (User.has_permission(session['id'],'configuration_all')):
            new = {'name': 'Administrativo', 'url': '/configuration', 'icon': 'fas fa-cog'}
            user_routes.append(new)
        return user_routes

    #Auth check
    auth.authenticated_or_401()
    #Listado de rutas
    routes = []
    User.db = get_db()
    if (not User.has_roles(session['id'])):
        return jsonify(routes)
    else:
        routes = get_routes()

        #Returning data
        return jsonify(routes)

#---------------------------------------------------#
#   Actualiza el estado (active/inactive) del usuario
#---------------------------------------------------#
def user_roles(user_id):
    admin_id = 1 #Role.get_id_by_name('Administrador')
    teacher_id = 2 #Role.get_id_by_name('Docente')
    preceptor_id = 3 #Role.get_id_by_name('Preceptor')

    is_admin = 0
    is_teacher = 0
    is_preceptor = 0

    if User.has_role(user_id, admin_id):
        is_admin = 1
    if User.has_role(user_id, teacher_id):
        is_teacher = 1
    if User.has_role(user_id, preceptor_id):
        is_preceptor = 1
    response = {}
    response['is_admin'] = is_admin
    response['is_teacher'] = is_teacher
    response['is_preceptor'] = is_preceptor
    return response