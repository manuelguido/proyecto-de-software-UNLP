from flask import Flask, redirect, url_for, session, render_template, jsonify
from flask_cors import CORS
from flask_session import Session
from flaskps.db import get_db
from flaskps.resources import configuration, auth, user, instrument, student, teacher, cycle, core, lesson, assistance, auth
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

#---------------------------------------------------#
#   API Privada (Regulada con permisos y sesión)
#---------------------------------------------------#
# Nucleos
app.add_url_rule("/api/cores", 'api_cores', core.all, methods=['GET'])
app.add_url_rule("/api/core/<int:id_data>", 'api_core', core.get, methods=['GET'])

# Estudiantes
app.add_url_rule("/api/students", 'api_students', student.all, methods=['GET'])
app.add_url_rule("/api/student/<int:id_data>", 'api_student', student.get, methods=['GET'])

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
    # Obtener roles y rutas de usuario loggeado
app.add_url_rule("/api/user/has_role", 'api_has_role', user.has_role, methods=['GET'])

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
