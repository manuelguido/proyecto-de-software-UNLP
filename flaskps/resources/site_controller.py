from flask import redirect, render_template, request, url_for, flash
from flaskps.db import get_db
from flaskps.models.info_sitio import InfoSitio
from flaskps.helpers.auth import authenticated

def index():
    x = InfoSitio.index()
    if (x):
        return render_template('home/index.html')
    else:
        return render_template('home/site_down.html')

def change_site_status():
    if not authenticated(session):
        abort(401)
    
    params = request.form
    if request.method == 'POST':
        InfoSitio.db = get_db()
        InfoSitio.change_site_status(params)
        flash("Se actualizó el estado del sitio correctamente")
        return redirect(url_for('panel'))

def change_site_pagination():
    if not authenticated(session):
        abort(401)

    params = request.form
    if request.method == 'POST':
        InfoSitio.db = get_db()
        InfoSitio.change_site_pagination(params)
        flash("Se actualizó el numero de paginación correctamente")
        return redirect(url_for('panel'))