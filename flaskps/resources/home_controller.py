from flask import redirect, render_template, request, url_for
from flaskps.db import get_db
from flaskps.models.info_sitio import InfoSitio

def index():
    x = InfoSitio.index()
    if (x):
        return render_template('home/index.html')
    else:
        return render_template('home/site_down.html')