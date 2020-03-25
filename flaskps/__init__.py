from flask import Flask, escape, request, session, jsonify, render_template, url_for, flash, redirect
from flask_cors import CORS
from flask_session import Session
from flaskps.db import get_db
from flaskps.resources import site_controller, auth, user, instrumento, student, docente, panel, ciclo, taller, clase, asistencia
from flaskps.config import Config
from flaskps.helpers import handler, auth as helper_auth

#Nombre de la aplicación
app = Flask(__name__,
            static_folder = "frontend/dist/static",
            template_folder = "frontend/dist")

#Configuracion inicial de la app
app.config.from_object(Config)

#Permite responder cualquier petición por parte de Vue a la API. 
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


#Server Side session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Funciones que se exportan al contexto de Jinja2
app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)

#url Inicio
#app.add_url_rule("/", 'home', site_controller.index)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("home.html")

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

#---------------------------------------------------#
#   Instrumentos
#---------------------------------------------------#
app.add_url_rule("/panel_instrumentos", 'panel_instrumentos', panel.getPanelInstrumentos, defaults={'page': 1}, methods=['POST', 'GET'])
app.add_url_rule("/panel_instrumentos/<int:page>", 'panel_instrumentos', panel.getPanelInstrumentos, methods=['POST', 'GET'])
        #Muestra el instrumento
app.add_url_rule("/panel_instrumento/<int:id_data>", 'panel_instrumento', panel.getInstrumento, methods=['GET'])
        #Para crear un instrumento
app.add_url_rule("/new_instrumento", 'new_instrumento', panel.getNewInstrumento, methods=['POST', 'GET'])
        #Para actualizar un instrumento
app.add_url_rule("/get_update_instrumento/<int:id_data>", 'get_update_instrumento', panel.getUpdateInstrumento, methods=['GET'])

#---------------------------------------------------#
#   Núcleos
#---------------------------------------------------#
app.add_url_rule("/panel_nucleos", 'panel_nucleos', panel.getNucleos, defaults={'page': 1})
app.add_url_rule("/panel_nucleos/<int:page>", 'panel_nucleos', panel.getNucleos)
        #Muestra el nucleo
app.add_url_rule("/panel_nucleo/<int:id_data>", 'panel_nucleo', panel.getNucleo, methods=['GET'])

#---------------------------------------------------#
#   Configuración del sitio
#---------------------------------------------------#
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
# Autenticación
app.add_url_rule("/iniciar_sesion", 'auth_login', auth.login)
app.add_url_rule("/cerrar_sesion", 'auth_logout', auth.logout)
app.add_url_rule(
    "/autenticacion",
    'auth_authenticate',
    auth.authenticate,
    methods=['POST']
)

#---------------------------------------------------#
#   ABM Usuarios
#---------------------------------------------------#
    #Alta
app.add_url_rule("/insert_user", 'insert_user', user.store, methods=['POST'])
    #Baja
app.add_url_rule("/delete_user/<string:id_data>", 'delete_user', user.delete, methods=['GET'])
    #Modificación
app.add_url_rule("/update_user", 'update_user', user.update, methods=['POST','GET'])
app.add_url_rule("/update_user_status", 'update_user_status', user.update_user_status, methods=['POST','GET'])
app.add_url_rule("/get_update_user/<int:id_data>", 'get_update_user', panel.getUpdateUser, methods=['GET'])

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
app.add_url_rule("/insert_instrument", 'insert_instrument', instrumento.store, methods=['POST', 'GET'])
    #Baja
app.add_url_rule("/delete_instrument/<string:id_data>", 'delete_instrument', instrumento.delete, methods=['GET'])
    #Modificación
app.add_url_rule("/update_instrument", 'update_instrument', instrumento.update, methods=['POST'])

#---------------------------------------------------#
#   Ciclos lectivos
#---------------------------------------------------#
    #Panel ciclos
app.add_url_rule("/panel_ciclos", 'panel_ciclos', panel.getPanelCiclos, defaults={'page': 1}) 
app.add_url_rule("/panel_ciclos/<int:page>", 'panel_ciclos', panel.getPanelCiclos)
    #Alta de ciclo
app.add_url_rule("/insert_ciclo", 'insert_ciclo', ciclo.store, methods=['POST', 'GET'])
    #Baja de ciclo
app.add_url_rule("/delete_ciclo/<string:id_data>", 'delete_ciclo', ciclo.delete, methods=['GET'])
    #Modificacion de ciclo
app.add_url_rule("/get_update_ciclo/<int:id_data>", 'get_update_ciclo', panel.getUpdateCiclo, methods=['GET'])
app.add_url_rule("/update_ciclo", 'update_ciclo', ciclo.update, methods=['POST'])

#---------------------------------------------------#
#   Talleres a ciclos
#---------------------------------------------------#
    #Panel de tallers 
app.add_url_rule("/panel_talleres", 'panel_talleres', panel.getPanelTalleres, defaults={'page': 1}) 
app.add_url_rule("/panel_talleres/<int:page>", 'panel_talleres', panel.getPanelTalleres)
    #Alta de taller a ciclo
app.add_url_rule("/insert_taller_ciclo", 'insert_taller_ciclo', taller.storeTallerCiclo, methods=['POST', 'GET'])
    #Baja de taller a ciclo
app.add_url_rule("/delete_taller_ciclo/", 'delete_taller_ciclo', taller.deleteTallerCiclo, methods=['POST'])

#---------------------------------------------------#
#   Docentes a talleres
#---------------------------------------------------#
    #Panel de docentes taller
app.add_url_rule("/panel_docentes_taller", 'panel_docentes_taller', panel.getPanelDocentesTaller, defaults={'page': 1}) 
app.add_url_rule("/panel_docentes_taller/<int:page>", 'panel_docentes_taller', panel.getPanelDocentesTaller)
    #Alta de docente a taller
app.add_url_rule("/insert_docente_taller", 'insert_docente_taller', docente.storeDocenteTaller, methods=['POST', 'GET'])
    #Baja de docente a taller
app.add_url_rule("/delete_docente_taller/", 'delete_docente_taller', docente.deleteDocenteTaller, methods=['POST'])

#---------------------------------------------------#
#   Alumnos a Docentes en talleres
#---------------------------------------------------#
    #Panel de docentes taller
app.add_url_rule("/panel_estudiantes_docentes", 'panel_estudiantes_docentes', panel.getPanelEstudiantesDocentes, defaults={'page': 1}) 
app.add_url_rule("/panel_estudiantes_docentes/<int:page>", 'panel_estudiantes_docentes', panel.getPanelEstudiantesDocentes)
    #Alta de docente a taller
app.add_url_rule("/insert_estudiante_docente", 'insert_estudiante_docente', student.storeEstudianteDocente, methods=['POST', 'GET'])
    #Baja de docente a taller
app.add_url_rule("/delete_estudiante_docente/", 'delete_estudiante_docente', student.deleteEstudianteDocente, methods=['POST'])

#---------------------------------------------------#
#   Horarios y Asistencia
#---------------------------------------------------#
    #Horarios
app.add_url_rule("/panel_horario", 'panel_horario', panel.getPanelHorario)
    #Alta de clase
app.add_url_rule("/insert_clase", 'insert_clase', clase.store, methods=['POST', 'GET'])
    #Baja de clase
app.add_url_rule("/delete_clase/<string:id_data>", 'delete_clase', clase.delete, methods=['GET', 'POST'])

    #Asistencia
app.add_url_rule("/panel_asistencia", 'panel_asistencia', panel.getPanelAsistencia) 
    #Ver asistencia
app.add_url_rule("/ver_asistencias/<string:id_data>", 'ver_asistencias', panel.getAsistencias, methods=['POST', 'GET']) 

    #Paasr asistencia
app.add_url_rule("/marcar_asistencia", 'marcar_asistencia', asistencia.storeAsistencia, methods=['POST', 'GET'])
app.add_url_rule("/marcar_inasistencia", 'marcar_inasistencia', asistencia.storeInasistencia, methods=['POST', 'GET'])


@app.route('/api/v1.0/mensaje')
def create_task():
    return jsonify('Hola mundo desde Flask')


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