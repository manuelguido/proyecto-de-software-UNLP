from flask import Flask, redirect, url_for, session, render_template, jsonify
from flask_cors import CORS
from flask_session import Session
from flaskps.db import get_db
from flaskps.resources import configuration, auth, user, instrument, student, teacher, cycle, core, lesson, assistance, auth, workshop
from flaskps.config import Config
from flaskps.helpers import handler
# Google auth (oAuth)
from authlib.integrations.flask_client import OAuth
from datetime import timedelta

from flaskps.resources.auth_decorator import login_required

#---------------------------------------------------#
#   App Setup
#---------------------------------------------------#
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#---------------------------------------------------#
#   Sessiones
#---------------------------------------------------#
# #Server Side session
app.config['SESSION_TYPE'] = 'filesystem'
# #Session(app)
app.config['SECRET_KEY'] = b'6hc/_gsh,./;2ZZx3c6_s,1//'
# Session config
app.secret_key = b'6hc/_gsh,./;2ZZx3c6_s,1//'
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)


#---------------------------------------------------#
#   oAuth Setup
#---------------------------------------------------#
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='185154570305-g0kqraggrm7hu87h93k5o3kjjumumfcp.apps.googleusercontent.com',
    client_secret='rKXyFqoisiWI6YRjnOg5j19C',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)

#---------------------------------------------------#
#   API
#---------------------------------------------------#
# Configuración y estado de sitio
app.add_url_rule("/api/configuration", 'api_configuration', configuration.all, methods=['GET'])
app.add_url_rule("/api/configuration/update", 'api_configuration_update', configuration.update, methods=['POST'])

#---------------------------------------------------#
#   API Privada (Regulada con permisos y sesión)
#---------------------------------------------------#
# Nucleos
app.add_url_rule("/api/cores", 'api_cores', core.all, methods=['GET'])
app.add_url_rule("/api/core/<int:id_data>", 'api_core', core.get, methods=['GET'])

# Estudiantes
app.add_url_rule("/api/students", 'api_students', student.all, methods=['GET'])
app.add_url_rule("/api/student/<int:id_data>", 'api_student', student.get, methods=['GET'])
app.add_url_rule("/api/student/create", 'api_student_create', student.create, methods=['POST'])
app.add_url_rule("/api/student/update", 'api_student_update', student.update, methods=['POST'])
app.add_url_rule("/api/student/delete", 'api_student_delete', student.delete, methods=['POST'])
app.add_url_rule("/api/student/form_data", 'api_student_form_data', student.getFormData, methods=['GET'])

# Docentes
app.add_url_rule("/api/teachers", 'api_teachers', teacher.all, methods=['GET'])
app.add_url_rule("/api/teacher/<int:id_data>", 'api_teacher', teacher.get, methods=['GET'])
app.add_url_rule("/api/teacher/create", 'api_teacher_create', teacher.create, methods=['POST'])
app.add_url_rule("/api/teacher/update", 'api_teacher_update', teacher.update, methods=['POST'])
app.add_url_rule("/api/teacher/delete", 'api_teacher_delete', teacher.delete, methods=['POST'])
app.add_url_rule("/api/teacher/form_data", 'api_teacher_form_data', teacher.getFormData, methods=['GET'])

# Instrumentos
app.add_url_rule("/api/instruments", 'api_instruments', instrument.all, methods=['GET'])
app.add_url_rule("/api/instrument/<int:instrument_id>", 'api_instrument', instrument.get, methods=['GET'])
app.add_url_rule("/api/instrument/create", 'api_instrument_create', instrument.create, methods=['POST'])
app.add_url_rule("/api/instrument/update", 'api_instrument_update', instrument.update, methods=['POST'])
app.add_url_rule("/api/instrument/delete", 'api_instrument_delete', instrument.delete, methods=['POST'])
app.add_url_rule("/api/instrument/form_data", 'api_instrument_form_data', instrument.getFormData, methods=['GET'])

# Usuarios
app.add_url_rule("/api/users", 'api_users', user.all, methods=['GET'])
app.add_url_rule("/api/user/<int:id_data>", 'api_user', user.get, methods=['GET'])
app.add_url_rule("/api/user/create", 'api_user_create', user.create, methods=['POST'])
app.add_url_rule("/api/user/update", 'api_user_update', user.update, methods=['POST'])
app.add_url_rule("/api/user/delete", 'api_user_delete', user.delete, methods=['POST'])
app.add_url_rule("/api/user/profile", 'api_profile', user.profile, methods=['GET']) # Obtener perfil de usuario loggeado
app.add_url_rule("/api/user/routes", 'api_routes', user.routes, methods=['GET']) # Obtener roles y rutas de usuario loggeado
app.add_url_rule("/api/user/has_role", 'api_has_role', user.has_role, methods=['GET']) # Obtener roles y rutas de usuario loggeado

# Ciclos lectivos (Cycles)
app.add_url_rule("/api/cycles", 'api_cycles', cycle.all, methods=['GET'])
app.add_url_rule("/api/cycle/<int:cycle_id>", 'api_cycle', cycle.get, methods=['GET'])
app.add_url_rule("/api/cycle/create", 'api_cycle_create', cycle.create, methods=['POST'])
app.add_url_rule("/api/cycle/update", 'api_cycle_update', cycle.update, methods=['POST'])
app.add_url_rule("/api/cycle/delete", 'api_cycle_delete', cycle.delete, methods=['POST'])
app.add_url_rule("/api/cycle/form_data", 'api_cycle_form_data', cycle.getFormData, methods=['GET'])

# Talleres (Workshops)
app.add_url_rule("/api/workshops", 'api_workshops', workshop.all, methods=['GET'])
app.add_url_rule("/api/workshop/<int:workshop_id>", 'api_workshop', workshop.get, methods=['GET'])
app.add_url_rule("/api/workshop/create", 'api_workshop_create', workshop.create, methods=['POST'])
app.add_url_rule("/api/workshop/update", 'api_workshop_update', workshop.update, methods=['POST'])
app.add_url_rule("/api/workshop/delete", 'api_workshop_delete', workshop.delete, methods=['POST'])

# Talleres y ciclos lectivos (Workshop cycles) (Asignación)
app.add_url_rule("/api/workshop_cycles", 'api_workshop_cycles', workshop.all_cycle_workshop, methods=['GET'])
app.add_url_rule("/api/workshop/assign", 'api_workshop_assign', workshop.assign, methods=['POST'])
app.add_url_rule("/api/workshop/unassign", 'api_workshop_unassign', workshop.unassign, methods=['POST'])
app.add_url_rule("/api/workshop_cycles/form_data", 'api_workshop_cycles_form_data', workshop.getFormData, methods=['GET'])

# Clases (Lessons)
app.add_url_rule("/api/cycles", 'api_lessons', lesson.all, methods=['GET'])
app.add_url_rule("/api/cycle/<int:cycle_id>", 'api_lesson', lesson.get, methods=['GET'])
app.add_url_rule("/api/cycle/create", 'api_lesson_create', lesson.create, methods=['POST'])
app.add_url_rule("/api/cycle/update", 'api_lesson_update', lesson.update, methods=['POST'])
app.add_url_rule("/api/cycle/delete", 'api_lesson_delete', lesson.delete, methods=['POST'])
app.add_url_rule("/api/cycle/form_data", 'api_lesson_form_data', lesson.getFormData, methods=['GET'])

#---------------------------------------------------#
#   Autenticacion
#---------------------------------------------------#
#Cerrar sesión
app.add_url_rule("/auth/unauthenticate", 'auth_unauthenticate', auth.unauthenticate, methods=['GET'])
#Autenticar usuario
app.add_url_rule("/auth/authenticate", 'auth_authenticate', auth.authenticate, methods=['POST'])
#Chequea si el usuario está autenticado
app.add_url_rule("/auth/authenticated", 'auth_authenticated', auth.authenticated, methods=['GET'])

#---------------------------------------------------#
#   Inicio (Vista única)
#---------------------------------------------------#
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")

@app.route('/google_login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    # session['profile'] = user_info
    auth.login_by_google(user_info)
    # session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    return redirect('/dashboard')

if __name__ == '__main__':
    app.run(debug=True)
