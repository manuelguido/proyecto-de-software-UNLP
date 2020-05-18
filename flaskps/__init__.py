from flask import Flask, escape, request, session
from flask import render_template, g, url_for
from flask import flash, redirect
from flask_session import Session
from flaskps.db import get_db
from flaskps.resources import site_controller
from flaskps.resources import auth
from flaskps.resources import user
from flaskps.resources import instrumento
from flaskps.resources import student
from flaskps.resources import docente
from flaskps.resources import panel
from flaskps.resources import ciclo
from flaskps.resources import taller
from flaskps.resources import clase
from flaskps.resources import asistencia
from flaskps.config import Config
from flaskps.helpers import handler
from flaskps.helpers import auth as helper_auth

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)