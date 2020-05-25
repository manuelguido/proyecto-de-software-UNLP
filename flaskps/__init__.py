from flask import Flask, render_template
from flask_cors import CORS
from flask_session import Session
from flaskps.db import get_db
from flaskps.resources import configuration, auth, user, instrument, student, teacher, cycle, core, lesson, assistance
from flaskps.config import Config
from flaskps.helpers import handler, auth

#---------------------------------------------------#
#   Configuración de app
#---------------------------------------------------#
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#---------------------------------------------------#
#   Sessiones
#---------------------------------------------------#
#Server Side session
app.config['SESSION_TYPE'] = 'filesystem'
#Session(app)
app.config['SECRET_KEY'] = b'6hc/_gsh,./;2ZZx3c6_s,1//'

#---------------------------------------------------#
#   API
#---------------------------------------------------#
app.add_url_rule("/api/configuration", 'api_configuration', configuration.all, methods=['GET'])

#---------------------------------------------------#
#   API Privada (Regulada con permisos)
#---------------------------------------------------#

# Nucleos
app.add_url_rule("/api/nucleos", 'api_nucleos', core.all, methods=['GET'])
app.add_url_rule("/api/nucleo/<int:id_data>", 'api_nucleo', core.get, methods=['GET'])

# Estudiantes
app.add_url_rule("/api/estudiantes", 'api_estudiantes', student.all, methods=['GET'])
app.add_url_rule("/api/estudiante/<int:id_data>", 'api_estudiante', student.get, methods=['GET'])

# Docentes
app.add_url_rule("/api/docentes", 'api_docentes', teacher.all, methods=['GET'])
app.add_url_rule("/api/docente/<int:id_data>", 'api_docente', teacher.get, methods=['GET'])

# Instrumentos
app.add_url_rule("/api/instrumentos", 'api_instrumentos', instrument.all, methods=['GET'])
app.add_url_rule("/api/instrumento/<int:id_data>", 'api_instrumento', instrument.get, methods=['GET'])

# Usuarios
app.add_url_rule("/api/usuarios", 'api_usuarios', user.all, methods=['GET'])
app.add_url_rule("/api/usuario/<int:id_data>", 'api_usuario', user.get, methods=['GET'])
    # Obtener perfil de usuario loggead
app.add_url_rule("/api/usuario/perfil", 'api_profile', user.profile, methods=['GET'])
    # Obtener roles de usuario loggead
app.add_url_rule("/api/usuario/rutas", 'user_routes', user.routes, methods=['GET'])

#---------------------------------------------------#
#   Autenticacion
#---------------------------------------------------#

#Cerrar sesión
app.add_url_rule("/auth/unauthenticate", 'auth_unauthenticate', auth.unauthenticate, methods=['GET'])
#Autenticar usuario
app.add_url_rule("/auth/authenticate", 'auth_authenticate', auth.authenticate, methods=['GET', 'POST'])
#Usuario ya autenticado
app.add_url_rule("/auth/authenticated", 'auth_authenticated', auth.authenticated, methods=['GET'])

#---------------------------------------------------#
#   Inicio (Vista única)
#---------------------------------------------------#

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")

#---------------------------------------------------#
#   Inicio (Vista única)
#---------------------------------------------------#


if __name__ == '__main__':
    app.run(debug=True)
