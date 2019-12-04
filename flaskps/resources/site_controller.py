from flask import redirect, render_template, request, url_for, flash, session, abort
from flaskps.db import get_db
from flaskps.models.config_sitio import ConfigSitio
from flaskps.models.user import User
from flaskps.helpers.auth import authenticated
from flaskps.resources import forms

#Mostrar el index del sitio
def index():
    ConfigSitio.db = get_db()
    estadositio = ConfigSitio.index() 
    if (estadositio):
        infositio = ConfigSitio.all()
        return render_template(
            'home/index.html',
            estadositio=estadositio,
            infositio=infositio
            )
    else:
        return render_template(
            'home/site_down.html',
            estadositio=estadositio
            )

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
            flash("Se actualizó el estado del sitio correctamente")
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
            flash("Se actualizó la información del sitio correctamente")
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
            flash("Se actualizó el numero de paginación correctamente")
        else:
            flash('La paginacion debe ser un numero entre 1 y 20', 'error')
        return redirect(url_for('panel_adminsitio'))
    else:
        abort(401)

#Metodo sin restriccion de permisos para paginar
def get_pagination():
    ConfigSitio.db = get_db()
    return ConfigSitio.get_pagination()