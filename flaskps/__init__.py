from flask import Flask, escape, request, session
from flask import render_template, g, url_for
from flask import flash, redirect
from flask_session import Session
from flaskps.db import get_db
from flaskps.resources import site_controller
from flaskps.resources import auth
from flaskps.resources import user
from flaskps.resources import student
from flaskps.resources import docente
from flaskps.resources import panel
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
app.add_url_rule("/", 'home', site_controller.index)

#Modificar datos de sitio
#Modificación de estado
app.add_url_rule(
    "/update_info_sitio",
    'update_info_sitio',
    site_controller.update_info_sitio,
    methods=['POST','GET']
)
#Cambiar estado del sitio
app.add_url_rule(
    "/change_site_status",
    'change_site_status',
    site_controller.change_site_status,
    methods=['POST']
)
#Cambiar paginacion del sitio
app.add_url_rule(
    "/change_site_pagination",
    'change_site_pagination',
    site_controller.change_site_pagination,
    methods=['POST']
)

#url Panel de administración
app.add_url_rule("/panel_estudiantes", 'panel_estudiantes', panel.getPanelEstudiantes, defaults={'page': 1})
app.add_url_rule("/panel_estudiantes/<int:page>", 'panel_estudiantes', panel.getPanelEstudiantes)
app.add_url_rule("/panel_empleados", 'panel_empleados', panel.getPanelEmpleados, defaults={'page': 1})
app.add_url_rule("/panel_empleados/<int:page>", 'panel_empleados', panel.getPanelEmpleados)
app.add_url_rule("/panel_usuarios", 'panel_usuarios', panel.getPanelUsuarios)
app.add_url_rule("/panel_ciclos", 'panel_ciclos', panel.getPanelCiclos)
app.add_url_rule("/panel_adminsitio", 'panel_adminsitio', panel.getPanelAdminSitio)

# Autenticación
app.add_url_rule("/iniciar_sesion", 'auth_login', auth.login)
app.add_url_rule("/cerrar_sesion", 'auth_logout', auth.logout)
app.add_url_rule(
    "/autenticacion",
    'auth_authenticate',
    auth.authenticate,
    methods=['POST']
)

#ABM Usuarios
#Alta
app.add_url_rule(
    "/user_new",
    'user_new',
    user.new,
    methods=['POST']
)

#Baja
app.add_url_rule(
    "/user_delete/<string:id_data>",
    'user_delete',
    user.delete,
    methods=['GET']
)

#Modificación de estado
app.add_url_rule(
    "/update_user_status",
    'update_user_status',
    user.update_user_status,
    methods=['POST','GET']
)

#ABM Estudiantes
#Alta
app.add_url_rule(
    "/insert_student",
    'insert_student',
    student.store,
    methods=['POST']
)

#Baja
app.add_url_rule(
    "/delete_student/<string:id_data>",
    'delete_student',
    student.delete,
    methods=['GET']
)

#Modificación
app.add_url_rule(
    "/update_student",
    'update_student',
    student.update,
    methods=['POST','GET']
)

#ABM Docentes
#Alta
app.add_url_rule(
    "/insert_docente",
    'insert_docente',
    docente.store,
    methods=['POST']
)

#Baja
app.add_url_rule(
    "/delete_docente/<string:id_data>",
    'delete_docente',
    docente.delete,
    methods=['GET']
)

#Modificación
app.add_url_rule(
    "/update_docente",
    'update_docente',
    docente.update,
    methods=['POST','GET']
)

if __name__ == '__main__':
    app.run(debug=True)