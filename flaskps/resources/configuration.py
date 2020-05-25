from flask import redirect, render_template, request, url_for, flash, session, abort, jsonify
from flaskps.db import get_db
from flaskps.models.configuration import Configuration
from flaskps.models.user import User
from flaskps.resources import forms

def all():
    Configuration.db = get_db()
    return jsonify(Configuration.all())

#Cambiar el estado del sitio a inactivo
def change_site_status():
    #Autenticacion
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'administrativo_update')):
        #Chequea el metodo y valida el formulario
        if request.method == 'POST' and forms.ChangeSiteStatus(request.form).validate():
            ConfigSitio.db = get_db()
            ConfigSitio.change_site_status(request.form['estado_sitio'])
            flash("Se actualizó el estado del sitio correctamente" ,'success')
        else:
            flash('Ingresaste información inválida, solo puedes ingresar: ACTIVO o INACTIVO', 'error')
        return redirect(url_for('panel_adminsitio'))
    else:
        abort(401)

#Actualizar la informacion del sitio (Titulo, descripcion e email)
def update_info_sitio():
    #Autenticacion
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'administrativo_update')):
        #Chequea el metodo y valida el formulario
        if request.method == 'POST' and forms.ChangeSiteInfo(request.form).validate():
            ConfigSitio.db = get_db()
            ConfigSitio.update_info_sitio(request.form)
            flash("Se actualizó la información del sitio correctamente" ,'success')
            return redirect(url_for('panel_adminsitio'))
        else:
            flash('Informacion inválida, solo puede ingresarse un titulo(máximo 255 char), email(máximo 255 char) y descripción(máximo 1000 char)', 'error')
        return redirect(url_for('panel_adminsitio'))
    else:
        abort(401)

#Cambiar paginacion del sitio
def change_site_pagination():
    #Autenticacion
    if not authenticated(session):
        abort(401)
    #Chequea permiso
    User.db = get_db()
    if (User.tiene_permiso(session['id'],'administrativo_update')):
        #Chequea el metodo y valida el formulario
        if request.method == 'POST' and forms.ChangePagination(request.form).validate():
            ConfigSitio.db = get_db()
            ConfigSitio.change_site_pagination(request.form['paginacion'])
            flash("Se actualizó el numero de paginación correctamente" ,'success')
        else:
            flash('La paginacion debe ser un numero entre 1 y 20', 'error')
        return redirect(url_for('panel_adminsitio'))
    else:
        abort(401)

#Metodo sin restriccion de permisos para paginar
def get_pagination():
    ConfigSitio.db = get_db()
    return ConfigSitio.get_pagination()