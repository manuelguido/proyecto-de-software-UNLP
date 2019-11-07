from flask import Flask, escape, request, session
from flask import render_template, g, url_for
from flask import flash, redirect
from flask_session import Session
from flaskps.db import get_db
from flaskps.resources import home_controller
from flaskps.resources import auth
from flaskps.resources import student
from flaskps.config import Config
from flaskps.helpers import handler
from flaskps.helpers import auth as helper_auth

app = Flask(__name__)

#Server Side session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Funciones que se exportan al contexto de Jinja2
app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)

#url Inicio
app.add_url_rule("/", 'home', home_controller.index)

#url Panel de administración
app.add_url_rule("/panel", 'panel', auth.getPanel)

# Autenticación
app.add_url_rule("/iniciar_sesion", 'auth_login', auth.login)
app.add_url_rule("/cerrar_sesion", 'auth_logout', auth.logout)
app.add_url_rule(
    "/autenticacion",
    'auth_authenticate',
    auth.authenticate,
    methods=['POST']
)

#CRUD Estudiantes
@app.route('/insert', methods = ['POST'])
def insert():
    student.store(request)
    return redirect(url_for('panel'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    student.delete(id_data)
    return redirect(url_for('panel'))

@app.route('/update',methods=['POST','GET'])
def update():
    student.update(request)
    return redirect(url_for('panel'))


if __name__ == '__main__':
    app.run(debug=True)