from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_session import Session
from flaskps.db import get_db
from flaskps.resources import site_controller, auth, usuario, instrumento, estudiante, docente, panel, ciclo, taller, clase, asistencia, nucleo
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

# Nucleos
app.add_url_rule("/api/nucleos", 'api_nucleos', nucleo.get_all, methods=['GET'])
app.add_url_rule("/api/nucleo/<int:id_data>", 'api_nucleo', nucleo.get_nucleo, methods=['GET'])

# Estudiantes
app.add_url_rule("/api/estudiantes", 'api_estudiantes', estudiante.get_all, methods=['GET'])
app.add_url_rule("/api/estudiante/<int:id_data>", 'api_estudiante', estudiante.get_estudiante, methods=['GET'])

# Docentes
app.add_url_rule("/api/docentes", 'api_docentes', docente.get_all, methods=['GET'])
app.add_url_rule("/api/docente/<int:id_data>", 'api_docente', docente.get_docente, methods=['GET'])

# Instrumentos
app.add_url_rule("/api/instrumentos", 'api_instrumentos', instrumento.get_all, methods=['GET'])
app.add_url_rule("/api/instrumento/<int:id_data>", 'api_instrumento', instrumento.get_instrumento, methods=['GET'])

# Usuarios
app.add_url_rule("/api/usuarios", 'api_usuarios', usuario.get_all, methods=['GET'])
app.add_url_rule("/api/usuario/<int:id_data>", 'api_usuario', usuario.get_usuario, methods=['GET'])
    # Obtener perfil de usuario loggead
app.add_url_rule("/api/usuario/perfil", 'api_profile', usuario.get_perfil, methods=['GET'])
    # Obtener roles de usuario loggead
app.add_url_rule("/api/usuario/rutas", 'user_routes', usuario.get_rutas, methods=['GET'])

#---------------------------------------------------#
#   Autenticacion
#---------------------------------------------------#
#Cerrar sesión
app.add_url_rule("/usuario/unauthenticate", 'auth_unauthenticate', auth.unauthenticate, methods=['GET'])
#Autenticar usuario
app.add_url_rule("/auth/authenticate", 'auth_authenticate', auth.authenticate, methods=['GET', 'POST'])
#Usuario ya autenticado
app.add_url_rule("/usuario/authenticated", 'auth_authenticated', auth.authenticated, methods=['GET'])

#---------------------------------------------------#
#   Inicio
#---------------------------------------------------#
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
