from flask import Flask, render_template
from flask_cors import CORS
from flask_session import Session
from flaskps.db import get_db
from flaskps.resources import configuration, auth, user, instrument, student, teacher, cycle, core, lesson, assistance, auth
from flaskps.config import Config
from flaskps.helpers import handler

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
# Configuración y estado de sitio
app.add_url_rule("/api/configuration", 'api_configuration', configuration.all, methods=['GET'])

#---------------------------------------------------#
#   API Privada (Regulada con permisos y sesión)
#---------------------------------------------------#
# Nucleos
app.add_url_rule("/api/cores", 'api_nucleos', core.all, methods=['GET'])
app.add_url_rule("/api/core/<int:id_data>", 'api_nucleo', core.get, methods=['GET'])

# Estudiantes
app.add_url_rule("/api/students", 'api_estudiantes', student.all, methods=['GET'])
app.add_url_rule("/api/student/<int:id_data>", 'api_estudiante', student.get, methods=['GET'])

# Docentes
app.add_url_rule("/api/teachers", 'api_teachers', teacher.all, methods=['GET'])
app.add_url_rule("/api/teacher/<int:id_data>", 'api_teacher', teacher.get, methods=['GET'])

# Instrumentos
app.add_url_rule("/api/instruments", 'api_instruments', instrument.all, methods=['GET'])
app.add_url_rule("/api/instrument/<int:id_data>", 'api_instrument', instrument.get, methods=['GET'])

# Usuarios
app.add_url_rule("/api/users", 'api_users', user.all, methods=['GET'])
app.add_url_rule("/api/user/<int:id_data>", 'api_user', user.get, methods=['GET'])
    # Obtener perfil de usuario loggeado
app.add_url_rule("/api/user/profile", 'api_profile', user.profile, methods=['GET'])
    # Obtener roles y rutas de usuario loggeado
app.add_url_rule("/api/user/routes", 'api_routes', user.routes, methods=['GET'])

#---------------------------------------------------#
#   Autenticacion
#---------------------------------------------------#
#Cerrar sesión
app.add_url_rule("/auth/unauthenticate", 'auth_unauthenticate', auth.unauthenticate, methods=['GET'])
#Autenticar usuario
app.add_url_rule("/auth/authenticate", 'auth_authenticate', auth.authenticate, methods=['GET', 'POST'])
#Chequea si el usuario está autenticado
app.add_url_rule("/auth/authenticated", 'auth_authenticated', auth.authenticated, methods=['GET'])

#---------------------------------------------------#
#   Inicio (Vista única)
#---------------------------------------------------#
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")

#---------------------------------------------------#
#   App run
#---------------------------------------------------#
if __name__ == '__main__':
    app.run(debug=True)
