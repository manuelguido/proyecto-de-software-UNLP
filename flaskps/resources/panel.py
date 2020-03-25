from flask import session, redirect, render_template, request, url_for, abort, flash
import requests
import json
#Modelos
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.student import Student
from flaskps.models.docente import Docente
from flaskps.models.instrumento import Instrumento
from flaskps.models.tipo_instrumento import TipoInstrumento
from flaskps.models.nivel import Nivel
from flaskps.models.genero import Genero
from flaskps.models.escuela import Escuela
from flaskps.models.barrio import Barrio
from flaskps.models.nucleo import Nucleo
from flaskps.models.config_sitio import ConfigSitio
from flaskps.models.rol import Rol
from flaskps.models.taller import Taller
from flaskps.models.horario import Horario
from flaskps.models.clase import Clase
from flaskps.models.asistencia import Asistencia
from flaskps.models.responsable import Responsable
from flaskps.models.ciclo import Ciclo
from flaskps.resources import site_controller, forms
from flaskps.helpers.auth import authenticated

#---------------------------
#-  El return [{}] se uso para que no se rompa el servidor. Si el servidor se rompe es por la falla de la api, no del codigo
#--------------------------
#Metodos para las apis
def getLocalidades():
    request_localidad = requests.get(
        'https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad')
    return request_localidad.json()
    #return [{}]

def getDocumentos():
    request_tipo_docs = requests.get(
        'https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento')
    return request_tipo_docs.json()
    #return [{}]

#Modulo estudiantes
def getPanelEstudiantes(page):
    if not authenticated(session):
        abort(401)
    #Obtiene permisos del usuario
    User.db = get_db()
    permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
    #Obtiene estudiantes
    Student.db = get_db()
    lastpage = 1
    #Si se envia una pagina inexistente se aborta
    if (page > Student.total_paginas(site_controller.get_pagination())) or (not int(page) > 0):
        abort (404)
    #Chequea si hubo busquedas
        #Se buscó solo nombre
    if forms.searchByFirstName(request.args).validate():
        students = Student.searchByFirstName(request.args.get('solo_nombre'))
        #Se buscó solo apellido
    elif forms.searchByLastName(request.args).validate():
        students = Student.searchByLastName(request.args.get('solo_apellido'))
    elif forms.searchByBoth(request.args).validate():
        #Se buscó ambos
        students = Student.searchByBoth(request.args.get('ambos_nombre'), request.args.get('ambos_apellido'))
        #No hubo busqueda
    else:
        students = Student.allPaginated(site_controller.get_pagination(),int(page))
        #Ultima pagina de paginado
        lastpage = Student.getLastPage(site_controller.get_pagination(),int(page))
    #Obtiene niveles
    Nivel.db = get_db()
    niveles = Nivel.all()
    #Obtiene generos
    Genero.db = get_db()
    generos = Genero.all()
    #Obtiene escuelas
    Escuela.db = get_db()
    escuelas = Escuela.all()
    #Obtiene barrios
    Barrio.db = get_db()
    barrios = Barrio.all()
    #Obtiene responsables
    Responsable.db = get_db()
    responsables = Responsable.all()
    #Obtiene la información de las apis
    localidades = getLocalidades()
    tipo_docs = getDocumentos()
    #Retorna el template
    return render_template(
        'auth/panel_components/alumnos.html',
        permisos=permisos,
        nombre=session['nombre'],
        apellido=session['apellido'],
        students=students,
        localidades=localidades,
        tipo_docs=tipo_docs,
        niveles=niveles,
        generos=generos,
        escuelas=escuelas,
        barrios=barrios,
        responsables=responsables,
        page=page,
        lastpage=lastpage
    )

#Modulo docentes
def getPanelDocentes(page):
    if auth.authenticated():
        #g.user = session['user'] #En la documentación no detallaban el por qué de esta lína, pero sí que era necesaria para las paginas restringidas
        #Obtiene permisos del usuario
        User.db = get_db()
        permisos = User.get_permisos(session['id'])
        #Obtiene docentes
        Docente.db = get_db()

        lastpage = 1
        #Si se envia una pagina inexistente se aborta
        if (page > Docente.total_paginas(site_controller.get_pagination())) or (not int(page) > 0):
            abort (404)
        #Chequea si hubo busquedas
            #Se buscó solo nombre
        if forms.searchByFirstName(request.args).validate():
            docentes = Docente.searchByFirstName(request.args.get('solo_nombre'))
            #Se buscó solo apellido
        elif forms.searchByLastName(request.args).validate():
            docentes = Docente.searchByLastName(request.args.get('solo_apellido'))
        elif forms.searchByBoth(request.args).validate():
            #Se buscó ambos
            docentes = Docente.searchByBoth(request.args.get('ambos_nombre'), request.args.get('ambos_apellido'))
            #No hubo busqueda
        else:
            docentes = Docente.allPaginated(site_controller.get_pagination(),int(page))
            #Ultima pagina de paginado
            lastpage = Docente.getLastPage(site_controller.get_pagination(),int(page))
        #Obtiene generos
        Genero.db = get_db()
        generos = Genero.all()
        #Obtiene la información de las apis
        localidades = getLocalidades()
        tipo_docs = getDocumentos()
        #Retorna el template
        return render_template(
            'auth/panel_components/docentes.html',
            permisos=permisos,
            nombre=session['nombre'],
            apellido=session['apellido'],
            localidades=localidades,
            tipo_docs=tipo_docs,
            generos=generos,
            docentes=docentes,
            page=page,
            lastpage=lastpage
        )
    return redirect(url_for('auth_login'))

#Modulo usuarios
def getPanelUsuarios(page):
    if auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
        lastpage = 1
        #Obtiene usuarios
        if (page > User.total_paginas(site_controller.get_pagination())) or (not int(page) > 0):
            abort (404)
        #Chequea si hubo busquedas
            #Se buscó solo nombre
        if forms.searchByFirstName(request.args).validate():
            usuarios = User.searchByUserName(request.args.get('solo_nombre'))
            #Se buscó solo activo
        elif forms.searchByActive(request.args).validate():
            usuarios = User.searchByActive(request.args.get('active'))
        else:
            usuarios = User.allPaginated(site_controller.get_pagination(),int(page))
            #Ultima pagina de paginado
            lastpage = User.getLastPage(site_controller.get_pagination(),int(page))
        #Obtiene roles
        Rol.db = get_db()
        roles_lista = Rol.all()
        return render_template(
            'auth/panel_components/usuarios.html',
            permisos=permisos,
            usuarios=usuarios,
            page=page,
            lastpage=lastpage,
            roles_lista=roles_lista
        )

    return redirect(url_for('auth_login'))

def getUpdateUser(id_data):
    if auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        if (User.tiene_permiso(session['id'],'usuario_update')):
            user = User.find_by_id(id_data)
            roles = User.get_rol(id_data)
            #Obtiene roles
            Rol.db = get_db()
            roles_lista = Rol.all()
            #Retorna el template
            return render_template(
                'auth/panel_components/usuario_update.html',
                user=user,
                roles=roles,
                roles_lista=roles_lista
            )
        else:
            abort(401)
    else:
        return redirect(url_for('auth_login'))


#Modulo estudiantes
def getPanelInstrumentos(page):
    if auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        if (User.tiene_permiso(session['id'],'administrativo_index')):
            permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
            #Obtiene estudiantes
            Instrumento.db = get_db()
            lastpage = 1
            #Si se envia una pagina inexistente se aborta
            if (page > Instrumento.total_paginas(site_controller.get_pagination())) or (not int(page) > 0):
                abort (404)
            #Chequea si hubo busquedas
                #Se buscó instrumento
            if forms.searchByFirstName(request.args).validate():
                instrumentos = Instrumento.searchByName(request.args.get('solo_nombre'))
                #No hubo busqueda
            else:
                instrumentos = Instrumento.allPaginated(site_controller.get_pagination(),int(page))
                #Ultima pagina de paginado
                lastpage = Instrumento.getLastPage(site_controller.get_pagination(),int(page))
            #Retorna el template
            return render_template(
                'auth/panel_components/instrumentos.html',
                permisos=permisos,
                nombre=session['nombre'],
                apellido=session['apellido'],
                instrumentos=instrumentos,
                page=page,
                lastpage=lastpage
            )
        else:
            abort(401)
    else:
        return redirect(url_for('auth_login'))

def getInstrumento(id_data):
    if auth.authenticated():
        User.db = get_db()
        if (User.tiene_permiso(session['id'],'instrumento_show')):
            TipoInstrumento.db = get_db()
            tipos = TipoInstrumento.all()
            Instrumento.db = get_db()
            instrumento = Instrumento.getInstrumento(id_data)
            return render_template(
                'auth/panel_components/instrumento.html',
                nombre=session['nombre'],
                apellido=session['apellido'],
                tipos=tipos,
                instrumento=instrumento,
            )
        else:
            abort(401)
    else:
        return redirect(url_for('auth_login'))

def getNewInstrumento():
    if auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        if (User.tiene_permiso(session['id'],'instrumento_new')):
            #Obtener tipo
            TipoInstrumento.db = get_db()
            tipos = TipoInstrumento.all()
            #Retorna el template
            return render_template(
                'auth/panel_components/instrumento_new.html',
                nombre=session['nombre'],
                apellido=session['apellido'],
                tipos=tipos,
            )
        else:
            abort(401)
    else:
        return redirect(url_for('auth_login'))

def getUpdateInstrumento(id_data):
    if auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        if (User.tiene_permiso(session['id'],'instrumento_update')):
            TipoInstrumento.db = get_db()
            tipos = TipoInstrumento.all()
            Instrumento.db = get_db()
            instrumento = Instrumento.getInstrumento(id_data)   
            #Retorna el template
            return render_template(
                'auth/panel_components/instrumento_update.html',
                nombre=session['nombre'],
                apellido=session['apellido'],
                tipos=tipos,
                instrumento=instrumento,
            )
        else:
            abort(401)
    else:
        return redirect(url_for('auth_login'))

#Modulos nucleos
def getNucleos(page):
    if auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        Nucleo.db = get_db()
        #Si se envia una pagina inexistente se aborta
        if (page > Nucleo.total_paginas(site_controller.get_pagination())) or (not int(page) > 0):
            abort (404)
        nucleos = Nucleo.allPaginated(site_controller.get_pagination(),int(page))
        fullnucleos = Nucleo.all()
        #Ultima pagina de paginado
        lastpage = Nucleo.getLastPage(site_controller.get_pagination(),int(page))
        return render_template(
            'auth/panel_components/nucleos.html',
            nombre=session['nombre'],
            apellido=session['apellido'],
            page=page,
            lastpage=lastpage,
            nucleos=nucleos,
            fullnucleos=fullnucleos,
        )
    else:
        return redirect(url_for('auth_login'))

def getNucleo(id_data):
    if auth.authenticated():
        #Nucleo
        Nucleo.db = get_db()
        nucleo = Nucleo.getNucleo(id_data)
        return render_template(
            'auth/panel_components/nucleo.html',
            nombre=session['nombre'],
            apellido=session['apellido'],
            nucleo=nucleo
        )
    else:
        return redirect(url_for('auth_login'))

#Modulos ciclos lectivos
def getPanelCiclos(page):
    Ciclo.db = get_db()
    if auth.authenticated():# or not auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
        if (page > Ciclo.total_paginas(site_controller.get_pagination())) or (not int(page) > 0):
            abort (404)
        ciclos = Ciclo.all()
        pciclos = Ciclo.allPaginated(site_controller.get_pagination(),int(page))
        lastpage = Ciclo.getLastPage(site_controller.get_pagination(),int(page))
        return render_template(
            'auth/panel_components/ciclos_lectivos.html',
            permisos=permisos,
            ciclos=ciclos,
            pciclos=pciclos, #ciclos paginados
            page=page,
            lastpage=lastpage
        )
    return redirect(url_for('auth_login'))

def getUpdateCiclo(id_data):
    if auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        if (User.tiene_permiso(session['id'],'administrativo_update')):
            Ciclo.db = get_db()
            ciclo = Ciclo.getCiclo(id_data)   
            #Retorna el template
            return render_template(
                'auth/panel_components/ciclos_lectivos_update.html',
                ciclo=ciclo,
            )
        else:
            abort(401)
    else:
        return redirect(url_for('auth_login'))

#Modulos talleres
def getPanelTalleres(page):
    if auth.authenticated():# or not auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        Ciclo.db = get_db()
        Taller.db = get_db()
        permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
        if (page > Taller.total_paginas(site_controller.get_pagination())) or (not int(page) > 0):
            abort (404)
        lastpage = Taller.getLastPage(site_controller.get_pagination(),int(page))
        talleres = Taller.all()
        ciclos = Ciclo.all()
        ciclotalleres = Taller.allCicloTallerPaginated(site_controller.get_pagination(),int(page))
        return render_template(
            'auth/panel_components/talleres.html',
            permisos=permisos,
            page=page,
            lastpage=lastpage,
            talleres=talleres,
            ciclos=ciclos,
            ciclotalleres=ciclotalleres
        )
    return redirect(url_for('auth_login'))

#Modulos docentes talleres
def getPanelDocentesTaller(page):
    if auth.authenticated():# or not auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        Ciclo.db = get_db()
        Docente.db = get_db()
        permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
        if (page > Docente.total_paginas_taller(site_controller.get_pagination())) or (not int(page) > 0):
            abort (404)
        lastpage = Docente.getLastPageDocenteTaller(site_controller.get_pagination(),int(page))
        ciclotalleres = Ciclo.allCicloTaller()
        docentes = Docente.all()
        docente_responsable_taller = Docente.allDocenteTallerPaginated(site_controller.get_pagination(),int(page))
        return render_template(
            'auth/panel_components/docentes_taller.html',
            permisos=permisos,
            page=page,
            lastpage=lastpage,
            ciclotalleres=ciclotalleres,
            docentes=docentes,
            docente_responsable_taller=docente_responsable_taller
        )
    return redirect(url_for('auth_login'))

#Modulos alumnos docentes
def getPanelEstudiantesDocentes(page):
    if auth.authenticated():# or not auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        Student.db = get_db()
        permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
        if (page > Student.total_paginas_taller(site_controller.get_pagination())) or (not int(page) > 0):
            abort (404)
        lastpage = Student.getLastPageTaller(site_controller.get_pagination(),int(page))
        Docente.db = get_db()
        docente_responsable_taller = Docente.allDocenteTaller()
        estudiantes_talleres = Student.allEstudianteTallerPaginated(site_controller.get_pagination(),int(page))
        estudiantes = Student.all()
        return render_template(
            'auth/panel_components/alumnos_docentes.html',
            permisos=permisos,
            page=page,
            lastpage=lastpage,
            docente_responsable_taller=docente_responsable_taller,
            estudiantes_talleres=estudiantes_talleres,
            estudiantes=estudiantes
        )
    return redirect(url_for('auth_login'))

def getPanelHorario():
    if auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        if (User.tiene_permiso(session['id'],'horario_index')):
            permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
            #Obtiene informacion del sitio (Estado y paginacion)
            Horario.db = get_db()
            horarios = Horario.all()
            Clase.db = get_db()
            clases = Clase.all()
            Nucleo.db = get_db()
            nucleos = Nucleo.all()
            Docente.db = get_db()
            docente_responsable_taller = Docente.allDocenteTaller()
            return render_template(
                'auth/panel_components/clases.html',
                permisos=permisos,
                horarios=horarios,
                clases=clases,
                nucleos=nucleos,
                docente_responsable_taller=docente_responsable_taller
            )
        else:
            abort(401)
    else:
        return redirect(url_for('auth_login'))

def getPanelAsistencia():
    if auth.authenticated():
        #Obtiene permisos del usuario
        User.db = get_db()
        if (User.tiene_permiso(session['id'],'horario_index')):
            permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
            Clase.db = get_db()
            clases = Clase.all()
            Student.db = get_db()
            estudiantes_talleres = Student.allEstudianteTaller()
            return render_template(
                'auth/panel_components/asistencia.html',
                permisos=permisos,
                clases=clases,
                estudiantes_talleres=estudiantes_talleres,
                #docente_responsable_taller=docente_responsable_taller,
            )
        else:
            abort(401)
    else:
        return redirect(url_for('auth_login'))

def getAsistencias(id_data):
    if auth.authenticated():
        Clase.db = get_db()
        clase = Clase.findClass(id_data)
        Student.db = get_db()
        estudiantes = Student.findByClass(clase['id'])
        Asistencia.db = get_db()
        asistencias_estudiantes = Asistencia.getAsistencias(clase)
        return render_template(
            'auth/panel_components/asistencias.html',
            clase=clase,
            estudiantes=estudiantes,
            asistencias_estudiantes=asistencias_estudiantes,
        )
    else:
        return redirect(url_for('auth_login'))


#Modulo administracion del sitio
def getPanelAdminSitio():
    if auth.authenticated():
        User.db = get_db()
        if (User.tiene_permiso(session['id'],'administrativo_index')):
            permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario

            g.user = session['user'] #En la documentación no detallaban el por qué de esta lína, pero sí que era necesaria para las paginas restringidas
            #Obtiene permisos del usuario
            User.db = get_db()
            permisos = User.get_permisos(session['id']) #Session user es el email unico del usuario
            #Obtiene informacion del sitio (Estado y paginacion)
            ConfigSitio.db = get_db()
            infositio = ConfigSitio.all()

            return render_template(
                'auth/panel_components/administracion_sitio.html',
                permisos=permisos,
                nombre=session['nombre'],
                apellido=session['apellido'],
                infositio = infositio
            )
        else:
            abort(401)
    else:
        return redirect(url_for('auth_login'))
