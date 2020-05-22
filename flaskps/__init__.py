from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_session import Session
from flaskps.db import get_db
from flaskps.resources import site_controller, auth, user, instrumento, student, docente, panel, ciclo, taller, clase, asistencia, nucleo
from flaskps.config import Config
from flaskps.helpers import handler, auth as helper_auth
from flaskps.models import config_sitio

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#Server Side session
app.config['SESSION_TYPE'] = 'filesystem'
#Session(app)
app.config['SECRET_KEY'] = b'6hc/_gsh,./;2ZZx3c6_s,1//'


#---------------------------------------------------#
#   API
#---------------------------------------------------#
@app.route('/api/info_sitio')
def create_task():
    config_sitio.ConfigSitio.db = get_db()
    return jsonify(config_sitio.ConfigSitio.all())

#---------------------------------------------------#
#   Private API
#---------------------------------------------------#
app.add_url_rule("/api/nucleos", 'api_nucleos', nucleo.get_all, methods=['GET'])
app.add_url_rule("/api/nucleo/<int:id_data>", 'api_nucleo', nucleo.get_nucleo, methods=['GET'])

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
#   Usuario
#---------------------------------------------------#
    #Obtener perfil de usuario
app.add_url_rule("/api/user/profile", 'api_profile', user.get_profile, methods=['GET'])
    #Obtener roles de usuario
app.add_url_rule("/api/user/routes", 'user_routes', user.routes)

#---------------------------------------------------#
#   Inicio
#---------------------------------------------------#
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
