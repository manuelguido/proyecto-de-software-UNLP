from flask import redirect, render_template, request, url_for, flash, session, abort
from flaskps.db import get_db
from flaskps.models.config_sitio import ConfigSitio
from flaskps.helpers.auth import authenticated

def index():
    ConfigSitio.db = get_db()
    x = ConfigSitio.index()
    if (x):
        infositio = ConfigSitio.all()
        return render_template(
            'home/index.html',
            infositio=infositio
            )
    else:
        return render_template('home/site_down.html')

def change_site_status():
    if not authenticated(session):
        abort(401)
    
    if request.method == 'POST':
        ConfigSitio.db = get_db()
        ConfigSitio.change_site_status(request.form)
        flash("Se actualizó el estado del sitio correctamente")
        return redirect(url_for('panel_adminsitio'))

def update_info_sitio():
    if not authenticated(session):
        abort(401)
    
    if request.method == 'POST':
        ConfigSitio.db = get_db()
        ConfigSitio.update_info_sitio(request.form)
        flash("Se actualizó la información del sitio correctamente")
        return redirect(url_for('panel_adminsitio'))

def change_site_pagination():
    if not authenticated(session):
        abort(401)

    if request.method == 'POST':
        ConfigSitio.db = get_db()
        ConfigSitio.change_site_pagination(request.form)
        flash("Se actualizó el numero de paginación correctamente")
        return redirect(url_for('panel_adminsitio'))