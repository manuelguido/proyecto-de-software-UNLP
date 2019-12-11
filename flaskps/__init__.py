from flask import Flask, escape, request, session
from flask import render_template, g, url_for
from flask import flash, redirect
from flask_session import Session
from flaskps.db import get_db
from flaskps.resources import site_controller
from flaskps.resources import auth
from flaskps.resources import user
from flaskps.resources import instrumento
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

#---------------------------------------------------#
#   Panel de administracion
#---------------------------------------------------#
    #Seccion Estudiantes
app.add_url_rule("/panel_estudiantes", 'panel_estudiantes', panel.getPanelEstudiantes, defaults={'page': 1}, methods=['POST', 'GET'])
app.add_url_rule("/panel_estudiantes/<int:page>", 'panel_estudiantes', panel.getPanelEstudiantes, methods=['POST', 'GET'])

#app.add_url_rule("/search_student", 'search_student', student.searchEstudiantes, defaults={'page': 1})
#app.add_url_rule("/search_student/<int:page>", 'search_student', student.searchEstudiantes)

    #Seccion Empleados
app.add_url_rule("/panel_docentes", 'panel_docentes', panel.getPanelDocentes, defaults={'page': 1})
app.add_url_rule("/panel_docentes/<int:page>", 'panel_docentes', panel.getPanelDocentes)

    #Seccion Usuarios 
app.add_url_rule("/panel_usuarios", 'panel_usuarios', panel.getPanelUsuarios, defaults={'page': 1})
app.add_url_rule("/panel_usuarios/<int:page>", 'panel_usuarios', panel.getPanelUsuarios)

    #Seccion Instrumentos
app.add_url_rule("/panel_instrumentos", 'panel_instrumentos', panel.getPanelInstrumentos, defaults={'page': 1}, methods=['POST', 'GET'])
app.add_url_rule("/panel_instrumentos/<int:page>", 'panel_instrumentos', panel.getPanelInstrumentos, methods=['POST', 'GET'])
        #Muestra el instrumento
app.add_url_rule("/panel_instrumento/<int:id_data>", 'panel_instrumento', panel.getInstrumento, methods=['GET'])
        #Para crear un instrumento
app.add_url_rule("/new_instrumento", 'new_instrumento', panel.getNewInstrumento, methods=['POST', 'GET'])
app.add_url_rule("/get_update_instrumento/<int:id_data>", 'get_update_instrumento', panel.getUpdateInstrumento, methods=['GET'])


    #Seccion ciclos
app.add_url_rule("/panel_ciclos", 'panel_ciclos', panel.getPanelCiclos)

    #Seccion configuracion de sitio
app.add_url_rule("/panel_adminsitio", 'panel_adminsitio', panel.getPanelAdminSitio)


#---------------------------------------------------#
#   Modificar datos del sitio
#---------------------------------------------------#
    #Modificación de estado
app.add_url_rule("/update_info_sitio", 'update_info_sitio', site_controller.update_info_sitio,methods=['POST','GET'])
    #Cambiar estado del sitio
app.add_url_rule("/change_site_status", 'change_site_status', site_controller.change_site_status, methods=['POST'])
    #Cambiar paginacion del sitio
app.add_url_rule("/change_site_pagination", 'change_site_pagination', site_controller.change_site_pagination, methods=['POST'])


#---------------------------------------------------#
#   Autenticacion
#---------------------------------------------------#
    #Mostrar pagina de login
app.add_url_rule("/iniciar_sesion", 'auth_login', auth.login)
    #Cerrar sesión
app.add_url_rule("/cerrar_sesion", 'auth_logout', auth.logout)
    #Autenticar usuario
app.add_url_rule("/autenticacion", 'auth_authenticate', auth.authenticate, methods=['POST'])


#---------------------------------------------------#
#   ABM Usuarios
#---------------------------------------------------#
    #Alta
app.add_url_rule("/user_new", 'user_new', user.new, methods=['POST'])
    #Baja
app.add_url_rule("/user_delete/<string:id_data>", 'user_delete', user.delete, methods=['GET'])
    #Modificación
app.add_url_rule("/update_user_status", 'update_user_status', user.update_user_status, methods=['POST','GET'])


#---------------------------------------------------#
#   ABM Estudiantes
#---------------------------------------------------#
    #Alta
app.add_url_rule("/insert_student", 'insert_student', student.store, methods=['POST'])
    #Baja
app.add_url_rule("/delete_student/<string:id_data>", 'delete_student', student.delete, methods=['GET'])
    #Modificación
app.add_url_rule("/update_student", 'update_student', student.update, methods=['POST','GET'])


#---------------------------------------------------#
#   ABM Docentes
#---------------------------------------------------#
    #Alta
app.add_url_rule("/insert_docente", 'insert_docente', docente.store, methods=['POST'])
    #Baja
app.add_url_rule("/delete_docente/<string:id_data>", 'delete_docente', docente.delete, methods=['GET'])
    #Modificación
app.add_url_rule("/update_docente", 'update_docente', docente.update, methods=['POST','GET'])


#---------------------------------------------------#
#   ABM Instrumentos
#---------------------------------------------------#
    #Alta
app.add_url_rule("/insert_instrument", 'insert_instrument', instrumento.store, methods=['POST'])
    #Baja
app.add_url_rule("/delete_instrument/<string:id_data>", 'delete_instrument', instrumento.delete, methods=['GET'])
    #Modificación
app.add_url_rule("/update_instrument", 'update_instrument', instrumento.update, methods=['POST'])


#---------------------------------------------------#
#   Error views
#---------------------------------------------------#
@app.errorhandler(404)
def error404(error):
    return render_template('error/error404.html')

@app.errorhandler(401)
def error401(error):
    return render_template('error/error401.html')

if __name__ == '__main__':
    app.run(debug=True)