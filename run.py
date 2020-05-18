from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_session import Session
from flaskps.db import get_db
from flaskps.resources import site_controller, auth, user, instrumento, student, docente, panel, ciclo, taller, clase, asistencia
from flaskps.config import Config
from flaskps.helpers import handler, auth as helper_auth
from flaskps.models.config_sitio import ConfigSitio

app = Flask(__name__,
            static_folder = "./frontend/dist/static",
            template_folder = "./frontend/dist")
