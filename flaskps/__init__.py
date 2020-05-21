from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_session import Session
from flaskps.db import get_db
from flaskps.resources import site_controller, auth, user, instrumento, student, docente, panel, ciclo, taller, clase, asistencia
from flaskps.config import Config
from flaskps.helpers import handler, auth as helper_auth
from flaskps.models.config_sitio import ConfigSitio

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#Server Side session
app.config['SESSION_TYPE'] = 'filesystem'
#Session(app)
app.config['SECRET_KEY'] = b'6hc/_gsh,./;2ZZx3c6_s,1//'


#---------------------------------------------------#
#   API
#---------------------------------------------------#
@app.route('/api/v1.0/infositio')
def create_task():
    ConfigSitio.db = get_db()
    return jsonify(ConfigSitio.all())

#---------------------------------------------------#
#   Autenticacion
#---------------------------------------------------#
    #Cerrar sesión
app.add_url_rule("/user/unauthenticate", 'auth_unauthenticate', auth.unauthenticate, methods=['GET'])
    #Autenticar usuario
app.add_url_rule("/auth_authenticate", 'auth_authenticate', auth.authenticate, methods=['GET', 'POST'])
    #Usuario ya autenticado
app.add_url_rule("/user/authenticated", 'auth_authenticated', auth.authenticated, methods=['GET'])

#---------------------------------------------------#
#   Inicio
#---------------------------------------------------#
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
